#!/usr/bin/env python3
"""Minimal Hadoop Streaming reducer: sum fare_amount per key (input sorted/grouped).
Reads lines of the form: key\tvalue
Outputs: key\ttotal_fare (formatted with 2 decimals)
Also emits a small sample of received keys to stderr for demonstration.
"""
import sys

current_key = None
current_sum = 0.0
sample_keys = []
lines_seen = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) < 2:
        # try splitting by whitespace
        parts = line.split()
        if len(parts) < 2:
            continue
    key = parts[0]
    try:
        val = float(parts[1])
    except Exception:
        continue

    # record sample of keys seen
    if len(sample_keys) < 5 and (not sample_keys or sample_keys[-1] != key):
        sample_keys.append(key)

    lines_seen += 1

    if current_key is None:
        current_key = key
        current_sum = val
    elif key == current_key:
        current_sum += val
    else:
        # emit previous
        try:
            sys.stdout.write(f"{current_key}\t{current_sum:.2f}\n")
        except Exception:
            pass
        current_key = key
        current_sum = val

# final emit
if current_key is not None:
    try:
        sys.stdout.write(f"{current_key}\t{current_sum:.2f}\n")
    except Exception:
        pass

# write small sample to stderr showing what shuffle input looked like
if sample_keys:
    try:
        sys.stderr.write('#REDUCER_SHUFFLE_SAMPLE\n')
        for k in sample_keys:
            sys.stderr.write(k + '\n')
    except Exception:
        pass
