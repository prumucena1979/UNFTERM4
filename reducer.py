#!/usr/bin/env python3
import sys
from collections import defaultdict


current_pul = None
current_total_fare = 0.0


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        pul, fare_str = line.split('\t', 1)
        fare = float(fare_str)
    except ValueError:
        # Skip bad records
        continue

    if current_pul == pul:
        # Accumulate fare for the current key
        current_total_fare += fare
    else:
        if current_pul:
            # Output the result for the previous key
            print(f"{current_pul}\t{current_total_fare}")

        # Start new key
        current_pul = pul
        current_total_fare = fare


if current_pul:
    print(f"{current_pul}\t{current_total_fare}")
