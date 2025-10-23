# DAMO630 – Advanced Data Analytics: Assignment 1

## Project Overview: Privacy and Urban Mobility Analytics

This repository contains the solution for **Assignment 1** of the DAMO630 – Advanced Data Analytics course at the University of Niagara Falls Canada (UNF). The assignment addresses two distinct, yet critical, areas of modern data analytics: **Privacy-Preserving Analytics with Synthetic Data** and **Big Data Mining for Urban Mobility**.

The solution is presented in the Jupyter Notebook: `Group#03_DAMO630_29_Assignment01_Refined.ipynb`.

| Detail | Value |
| :--- | :--- |
| **Course** | DAMO630 – Advanced Data Analytics |
| **Institution** | University of Niagara Falls Canada (UNF) |
| **Assignment** | Assignment 1 |
| **Group** | Group #03 |
| **Date** | October 2025 |

---

## Business Challenge 1: Privacy-Preserving Analytics with Synthetic Data

**Goal:** To generate and evaluate synthetic patient data for research collaboration, ensuring compliance with privacy regulations (e.g., HIPAA, GDPR) while maintaining data utility.

### Technical Tasks and Methodology

| Task | Description | Key Tools |
| :--- | :--- | :--- |
| **Task I: Exploratory Analysis** | Analyze distributions, identify privacy-sensitive attributes, and visualize feature correlations of the real patient dataset. | Pandas, Matplotlib, Seaborn |
| **Task II: Baseline Generation** | Apply a classical method (e.g., noise injection or Faker-based rules) to create a synthetic dataset and compare its distributions to the real data. | NumPy, Pandas |
| **Task III: Advanced SDV Generation** | Train two advanced synthetic data models, **CTGAN** and **GaussianCopula**, using the Synthetic Data Vault (SDV) library. | SDV (CTGAN, GaussianCopula) |
| **Task IV: Evaluation** | Evaluate the generated synthetic datasets across three dimensions: **Statistical Similarity** (e.g., KS test, correlation preservation), **Utility** (TSTR: Train on Synthetic, Test on Real), and **Privacy** (row-level duplication check). | SDMetrics, Scikit-learn (RandomForest) |

**Key Insight:** The evaluation metrics provide a quantitative basis for determining the trustworthiness of the synthetic data for external sharing, balancing the trade-off between privacy preservation and analytical utility.

---

## Business Challenge 2: Mining NYC Taxi Trip Data with PySpark

**Goal:** To uncover travel patterns and segment riders from a large-scale NYC Taxi Trip dataset using Big Data frameworks (Hadoop/HDFS) and PySpark, providing actionable insights for city planners and transportation companies.

### Technical Tasks and Methodology

This challenge directly addresses **Learning Outcomes 3 (Big Data Workflows)** and **4 (Mining Techniques)**. The implementation utilizes a pseudo-distributed Hadoop environment with PySpark for large-scale processing.

#### 1. BC2.I: Big Data Setup & Data Preparation (LO3)

*   **Objective:** Establish connectivity to the HDFS NameNode and load the NYC Yellow Taxi Trip data (May 2023 Parquet file) into a Spark DataFrame.
*   **Execution:** Configuration of `HADOOP_USER_NAME` and `spark.hadoop.fs.defaultFS` to ensure HDFS compatibility. Initial data inspection (schema, count, statistics) is performed.
*   **MapReduce Input Preparation:** A minimal CSV containing only `PULocationID` and `fare_amount` is extracted and written back to HDFS as input for the legacy MapReduce task.

#### 2. BC2.II: Hadoop Streaming / MapReduce (LO3)

*   **Objective:** Compute the total fare revenue per pickup location using the foundational **MapReduce** paradigm.
*   **Execution:** Custom Python scripts (`mapper.py` and `reducer.py`) are defined to process the CSV input from HDFS. The `mapper` extracts the key-value pair (`PULocationID`, `fare_amount`), and the `reducer` aggregates the total fare for each key.
*   **Justification:** This task demonstrates an understanding of the classic distributed processing model. The notebook includes a discussion on the limitations of MapReduce (speed, disk I/O) compared to modern, in-memory frameworks like Spark.

#### 3. BC2.III: Frequent Pattern Mining (FPGrowth) (LO4)

*   **Objective:** Identify frequent travel patterns (origin-destination pairs) and strong association rules using PySpark MLlib's **FPGrowth** algorithm.
*   **Execution:** Trips are treated as "baskets" containing the `PULocationID` and `DOLocationID`. FPGrowth is applied to find frequent itemsets and derive association rules, which are quantified by **support**, **confidence**, and **lift**.
*   **Urban Mobility Insight:** Rules with high lift indicate non-random, strong travel flows (e.g., specific commuting corridors or airport routes), which are critical for infrastructure planning and service optimization.

#### 4. BC2.IV: Rider Segmentation (K-Means Clustering) (LO4)

*   **Objective:** Segment taxi trips into distinct rider personas based on key trip characteristics using **K-Means Clustering**.
*   **Execution:** Features (`trip_distance`, `fare_amount`, `pickup_hour`, `passenger_count`) are prepared using **VectorAssembler** and **StandardScaler** to ensure proper scaling. K-Means is applied (e.g., with k=3).
*   **Rider Personas:** The resulting cluster centers are analyzed by calculating the mean of the original features for each cluster. This allows for the interpretation of distinct rider personas (e.g., "Short-Distance Commuters," "Airport Travelers," "Late-Night Riders") and the suggestion of tailored services or pricing strategies.

---

## How to Run the Notebook

The notebook is designed to be executed in a specific Big Data environment.

1.  **Environment Setup:** Ensure you have a running pseudo-distributed Hadoop cluster (HDFS and YARN) with PySpark configured. The notebook assumes the HDFS NameNode is accessible via `hdfs://hadoop-VirtualBox:9000`.
2.  **Data Placement:** The NYC Taxi Trip data (`yellow_tripdata_2023-05.parquet`) must be uploaded to the HDFS path `/data/tlc/trips/`.
3.  **Execution:** Open `Group#03_DAMO630_29_Assignment01_Refined.ipynb` and run the cells sequentially. The notebook is self-contained and includes all necessary PySpark setup and imports.
4.  **MapReduce Step:** The MapReduce task (BC2.II) requires the `mapper.py` and `reducer.py` scripts (defined in the notebook) to be saved and executed on the Hadoop VM using the provided shell command.

```bash
# Example MapReduce execution command (run on the Hadoop VM)
hdfs dfs -cat /user/hadoop/taxi/yellow_2023-05_mincsv/part-* | \
  python3 mapper.py | sort | python3 reducer.py > total_fare_by_pu.txt
```
