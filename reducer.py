#!/usr/bin/env python3
import sys
from collections import defaultdict

acc = defaultdict(float)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        key, val = line.split('\t')
        acc[key] += float(val)
    except:
        continue

for k, v in acc.items():
    print(f"{k}\t{v}")
