#!/usr/bin/env python3
"""Minimal Hadoop Streaming mapper for total fare by pickup location.
Emits: key\tvalue where key is PULocationID or Borough/Zone if lookup used.
"""
import sys
import csv
import argparse
from typing import Optional, Dict, Tuple


def load_zone_map(path: str) -> Dict[str, Tuple[str, str]]:
    """Lightweight loader: returns mapping of LocationID -> (Borough, Zone)
    Keys are strings for safe comparison with CSV fields.
    """
    out = {}
    try:
        with open(path, newline='', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            for r in reader:
                # Typical columns: LocationID, Borough, Zone
                lid = r.get('LocationID') or r.get('locationid') or r.get('location_id')
                bor = r.get('Borough') or r.get('borough') or r.get('Borough')
                zone = r.get('Zone') or r.get('zone') or r.get('zone_name')
                if lid:
                    out[str(lid).strip()] = (str(bor).strip() if bor else '', str(zone).strip() if zone else '')
    except Exception:
        # fail silently; mapper will continue without lookup
        pass
    return out


parser = argparse.ArgumentParser(description='Mapper for total fare by pickup location')
parser.add_argument('--zone-lookup-path', default=None, help='Optional local CSV path with taxi zone lookup')
args = parser.parse_args()

zone_map = {}
if args.zone_lookup_path:
    zone_map = load_zone_map(args.zone_lookup_path)

# read from stdin, parse CSV defensively
reader = csv.DictReader(sys.stdin)

sample_out = []
count = 0
for row in reader:
    # prefer PULocationID
    key = None
    # case-insensitive access via keys lowercased
    lc = {k.lower(): k for k in row.keys()}
    # helpers
    def get(colname):
        k = lc.get(colname.lower())
        return row.get(k) if k else None

    puloc = get('PULocationID') or get('pu_location_id') or get('pulocationid')
    pickup_borough = get('pickup_borough') or get('borough')
    pickup_zone = get('pickup_zone') or get('zone')

    fare_raw = get('fare_amount') or get('fare')
    try:
        fare = float(fare_raw) if fare_raw not in (None, '') else None
    except Exception:
        fare = None

    if fare is None or not (fare > 0):
        continue  # ignore invalid/negative fares

    if puloc:
        puloc_s = str(puloc).strip()
        if zone_map and puloc_s in zone_map:
            borough, zone = zone_map[puloc_s]
            # prefer borough then zone then id
            if borough:
                key = borough
            elif zone:
                key = zone
            else:
                key = puloc_s
        else:
            key = puloc_s
    else:
        # fallback to pickup_borough or pickup_zone
        if pickup_borough:
            key = str(pickup_borough).strip()
        elif pickup_zone:
            key = str(pickup_zone).strip()
        else:
            continue

    print(f"{key}\t{fare}")
    if len(sample_out) < 5:
        sample_out.append(f"{key}\t{fare}")
    count += 1

# emit small sample to stderr for demonstration
if sample_out:
    sys.stderr.write("#MAPPER_SAMPLE\n")
    for s in sample_out:
        sys.stderr.write(s + "\n")

