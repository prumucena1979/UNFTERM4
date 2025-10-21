Advanced Data Analytics – Assignment (DAMO630)

This repository contains the deliverables for a Master's level assignment in the Master of Data Analytics program. The work was completed for the course "Advanced Data Analytics" (DAMO630) and demonstrates techniques in synthetic data generation, evaluation, and large-scale data analysis using Hadoop and PySpark.

Overview
--------
The project is organized into two ordered Business Challenges. Work proceeds from Business Challenge 01 through Business Challenge 02 in the notebook(s):

- Business Challenge 01 — Synthetic Data Generation & Evaluation
	- Objectives: build baseline and advanced synthetic data using classical noise baselines and SDV models (GaussianCopula, CTGAN), save metadata and models for reproducibility, and evaluate generated data using statistical and utility metrics (quality reports, diagnostic reports, TSTR, duplication/privacy checks).
	- Key artifacts: notebooks and code that fit SDV models, sample synthetic outputs, and evaluation scripts.

- Business Challenge 02 — NYC Taxi Trip Data (Big Data Analysis)
	- Objectives: demonstrate HDFS connectivity and data preparation, show a small MapReduce (Hadoop Streaming) example, and perform PySpark analytics including frequent pattern mining (FPGrowth) and clustering (K-Means) to extract operational insights from taxi trip data.
	- Key artifacts: PySpark notebook cells that connect to HDFS, parquet readers, minimal CSV exports for streaming, mapper/reducer scripts for Hadoop Streaming, and PySpark pipelines for FPGrowth and K-Means.

Requirements
------------
See `requirements.txt` for the Python package requirements used during development. Example key packages:

- numpy, pandas, scikit-learn, matplotlib, seaborn
- sdv, sdmetrics, rdt, copulas, torch
- pyspark

Install with:

pip install -r requirements.txt

Datasets
--------
- `Datasets/HealthInsurance.csv` — used for Business Challenge 01 (synthetic data experiments)
- NYC Taxi Trip Data (parquet on HDFS) — referenced in Business Challenge 02; the notebook expects the taxi parquet file to be available on the student's Hadoop VM at `/data/tlc/trips/yellow_tripdata_2023-05.parquet` or similar. HDFS access is required to fully run BC02 cells.

How the notebook is structured
-----------------------------
- Cells relating to Business Challenge 01 appear first and implement synthetic data generation and evaluation steps.
- Cells for Business Challenge 02 follow and assume access to a Hadoop VM (NameNode at `hdfs://hadoop-VirtualBox:9000`). BC02 includes:
	- environment constants and SparkSession setup (idempotent),
	- HDFS probe using the Spark JVM API,
	- Parquet load and exploration (schema, counts, sample),
	- optional CSV export for Hadoop Streaming,
	- sample `mapper.py` and `reducer.py` for Hadoop Streaming (to compute total fare per pickup zone),
	- PySpark FPGrowth example for frequent location pairs,
	- PySpark K-Means clustering pipeline for trip segmentation.

Notes & running tips
--------------------
- To run Business Challenge 02 you need:
	- a running Hadoop VM reachable from the notebook kernel (example host: `hadoop-VirtualBox`, RPC port `9000`),
	- the taxi parquet file uploaded to HDFS (`/data/tlc/trips/yellow_tripdata_2023-05.parquet`),
	- a Spark-enabled Python kernel configured with the same Java/PYSPARK settings (see notebook cells that set JAVA_HOME and SPARK_HOME for local runs).

- The notebook includes idempotent SparkSession creation and JVM-based HDFS checks so you can re-run cells safely.

Contributing / Notes
--------------------
- This repository holds a student assignment — please treat it as an educational artifact. If you re-run or adapt the notebooks make sure to not overwrite system HDFS paths unintentionally.

License / Attribution
---------------------
- (Add your preferred license or university attribution here)

How to run BC02 locally (Hadoop + Spark)
--------------------------------------
This section provides a short, repeatable checklist to run Business Challenge 02 locally from a Windows PowerShell environment that can reach your Hadoop VM. Adjust paths to match your local JDK and Spark installs.

Prerequisites
 - A running Hadoop VM (example hostname used in the notebook: `hadoop-VirtualBox`) with NameNode RPC port `9000` (adjust in the notebook if your VM uses a different port).
 - The taxi parquet file uploaded to HDFS at `/data/tlc/trips/yellow_tripdata_2023-05.parquet`.
 - A local Python environment with the packages in `requirements.txt` installed.

1) PowerShell (session) — set environment variables for the current shell

```powershell
$env:JAVA_HOME = 'C:\Program Files\Eclipse Adoptium\jdk-17.0.16.8-hotspot'
$env:SPARK_HOME = 'C:\spark'
$env:PATH = "$env:JAVA_HOME\bin;$env:SPARK_HOME\bin;$env:PATH"
# Optional: point PySpark driver to the current Python
$env:PYSPARK_DRIVER_PYTHON = (Get-Command python).Source
$env:PYSPARK_PYTHON = (Get-Command python).Source
# Ensure Hadoop user used by the notebooks is 'hadoop' (used for demo/demo VM setups)
$env:HADOOP_USER_NAME = 'hadoop'
```

Note: Replace the JDK path with your installed JDK if different (some notebooks used `C:\Program Files\Java\jdk-17` in examples).

2) Install Python packages (inside the same environment/session)

```powershell
pip install -r requirements.txt
```

3) Start Jupyter from the same environment

```powershell
jupyter lab   # or jupyter notebook
```

4) Upload the parquet file to HDFS (run on the Hadoop VM shell, not on your Windows host)

```bash
# On the Hadoop VM shell (example)
# place the parquet file in the VM, then:
hdfs dfs -mkdir -p /data/tlc/trips
hdfs dfs -put yellow_tripdata_2023-05.parquet /data/tlc/trips/
hdfs dfs -ls /data/tlc/trips
```

Tips
- If you use `setx` to persist environment variables in Windows, open a new shell afterwards; session variables (shown above) are enough for a running Jupyter server.
- The notebook includes idempotent SparkSession creation and JVM-based HDFS checks — run the BC02 cells in sequence.
- If your NameNode uses a different host/port, set `NN_HOST` and `NN_PORT` in the BC02 environment cell before starting Spark.

If you want, I can add an example PowerShell `run_bc02.ps1` script to the repo that sets these variables and launches Jupyter automatically.
