Advanced Data Analytics – Synthetic Data & Big Data (DAMO630)

This repository contains notebooks and code for DAMO630 – Advanced Data Analytics (MDA, University of Niagara Falls Canada).

Goals:

* Generate and evaluate synthetic data (classical methods + SDV models like CTGAN/GaussianCopula).

* Apply evaluation metrics: statistical similarity, utility (TSTR), privacy checks.

* Use HDFS, MapReduce, and PySpark to analyze NYC Taxi data.

* Perform frequent pattern mining (FPGrowth) and clustering (K-Means) to extract business insights.

*** Requirements

See requirements.txt:

numpy>=1.26,<3.0
pandas>=2.0,<3.0
scikit-learn>=1.5,<2.0
matplotlib>=3.8,<4.0
seaborn>=0.13,<1.0
sdv>=1.10,<2.0
sdmetrics>=0.12,<1.0
rdt>=1.12,<2.0
copulas>=0.10,<1.0
torch>=2.1,<3.0
pyspark>=3.5,<4.0
hdfs>=2.7,<3.0


* Install with:

pip install -r requirements.txt

Datasets

Health Insurance CSV

NYC Taxi Trip Data

Deliverables

* Challenge 1: Synthetic data generation + evaluation.
* Challenge 2: NYC Taxi analysis with Big Data tools (PENDING)
