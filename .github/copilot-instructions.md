# Copilot Instructions for DAMO630 Advanced Data Analytics Project

## Project Overview
- This repository contains Jupyter notebooks and code for synthetic data generation/evaluation and big data analytics (PySpark, HDFS, MapReduce) for the DAMO630 course at University of Niagara Falls Canada.
- There are two main challenges:
  1. Generate and evaluate synthetic data using classical and SDV models (CTGAN, GaussianCopula).
  2. Analyze NYC Taxi data using PySpark and big data tools (challenge 2 is pending).

## Key Files & Structure
- `Group#03_DAMO630_29_Assignment01.ipynb`: Main notebook for all tasks (EDA, synthetic data, evaluation, PySpark setup).
- `Datasets/HealthInsurance.csv`: Main dataset for synthetic data tasks.
- `requirements.txt`: All required Python packages with version constraints.
- `README.md`: Project goals, requirements, and deliverables.

## Developer Workflows
- **Environment Setup:**
  - Install dependencies: `pip install -r requirements.txt`
  - For PySpark tasks, ensure Java 17 (Temurin JDK) is installed and set `JAVA_HOME` accordingly in the notebook.
- **Notebook Execution:**
  - Run cells sequentially in `Group#03_DAMO630_29_Assignment01.ipynb`.
  - Some cells require manual adjustment (e.g., set the target column for TSTR evaluation).
- **Data Paths:**
  - Use relative paths (e.g., `Datasets/HealthInsurance.csv`) for data loading.

## Patterns & Conventions
- **Imports:** All major imports are grouped at the top of the notebook.
- **Synthetic Data:**
  - Use SDV's `GaussianCopulaSynthesizer` and `CTGANSynthesizer` for advanced synthetic data.
  - Baseline synthetic data is generated with random noise for comparison.
- **Evaluation:**
  - Quality and diagnostic reports use `sdmetrics`.
  - Utility is measured with TSTR (Train on Synthetic, Test on Real) using RandomForest models.
  - Privacy is checked by computing exact duplicate rates.
- **PySpark Setup:**
  - Java environment is configured within the notebook (see code comments for details).
  - PySpark version is checked and errors are reported with tips for installation.

## Integration Points
- **External Dependencies:**
  - SDV, SDMetrics, PySpark, and related libraries are required (see `requirements.txt`).
  - Java 17 is required for PySpark (set in notebook, not in environment variables globally).
- **Manual Steps:**
  - Some notebook cells require user input or adjustment (e.g., specifying the target column for classification/regression tasks).

## Example: Loading Data
```python
# Load Health Insurance dataset
df = pd.read_csv("Datasets/HealthInsurance.csv")
```

## Example: Setting Up Java for PySpark
```python
import os
os.environ["JAVA_HOME"] = r"C:\\Program Files\\Eclipse Adoptium\\jdk-17"
os.environ["PATH"] = os.environ["JAVA_HOME"] + r"\\bin;" + os.environ["PATH"]
```

## Additional Notes
- All code and data are in a single notebook for ease of grading and reproducibility.
- Follow the structure and comments in the notebook for each business challenge.
- For new tasks, add new sections to the main notebook and update the README if needed.
