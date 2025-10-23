#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Input is a comma-separated line (PULocationID,fare_amount)
    parts = line.split(',')
    if len(parts) < 2:
        continue

    pul, fare = parts[0].strip(), parts[1].strip()

    try:
        # Ensure fare is a valid number
        f = float(fare)
    except ValueError:
        continue

    # Output: PULocationID \t fare_amount
    print(f"{pul}\t{f}")
