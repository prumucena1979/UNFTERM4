#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) < 2:
        continue
    pul, fare = parts[0].strip(), parts[1].strip()
    try:
        f = float(fare)
    except:
        continue
    print(f"{pul}\t{f}")
