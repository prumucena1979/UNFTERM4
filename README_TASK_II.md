BC2 — Task II: MapReduce (Hadoop Streaming) — Minimal Guide

Purpose
-------
Compute total fare revenue per pickup location (PULocationID) using Hadoop Streaming (mapper + reducer).

Files
-----
- mapper.py — streaming mapper that emits key\tfare (key = PULocationID)
- reducer.py — streaming reducer that sums fares per key

Assumptions
-----------
- Input CSV file contains columns including PULocationID and fare_amount (case-insensitive).
- Files live in HDFS under /user/hadoop/taxi/ (e.g., yellow_tripdata_2019-01.csv)
- Python 3 is available on the Hadoop nodes for streaming.

Local testing (sample, not HDFS)
-------------------------------
# Adjust local path to your sample file
head -n 5000 /path/local/yellow_tripdata_2019-01.csv \
  | python mapper.py 2> mapper_samples.log \
  | head

# Simulate shuffle+reduce locally (sort by key)
head -n 5000 /path/local/yellow_tripdata_2019-01.csv \
  | python mapper.py 2> mapper_samples.log \
  | sort -k1,1 \
  | python reducer.py 2> reducer_shuffle_samples.log \
  | head

Hadoop Streaming (HDFS)
-----------------------
# Prepare HDFS directories (idempotent)
hdfs dfs -mkdir -p /user/hadoop/taxi
hdfs dfs -mkdir -p /user/hadoop/out_task2

# Remove previous output (if any)
hdfs dfs -rm -r -f /user/hadoop/out_task2/streaming_out

# Run streaming
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -D mapreduce.job.name="BC2-TaskII-TotalFareByPickup" \
  -files mapper.py,reducer.py \
  -input  hdfs:///user/hadoop/taxi/yellow_tripdata_2019-01.csv \
  -output hdfs:///user/hadoop/out_task2/streaming_out \
  -mapper  "python mapper.py" \
  -reducer "python reducer.py"

# Inspect results
hdfs dfs -cat /user/hadoop/out_task2/streaming_out/part-* | head

Notes & Limitations
-------------------
- The mapper ignores rows with invalid or non-positive fare_amount.
- Aggregation key is PULocationID. If your dataset lacks PULocationID, mapper will skip those rows.
- MapReduce (Hadoop Streaming) requires data to be serialized to disk during shuffle and reduce — slower than Spark for iterative and in-memory operations.
- For production, additional error handling, input validation, and partition tuning are recommended.

