# 🚦 ETL Data Pipeline with Apache Airflow

This project demonstrates how to build an **ETL (Extract, Transform, Load)** data pipeline using **Apache Airflow** and the **BashOperator** to automate the ingestion and processing of road traffic data from various toll plazas.

## 🧩 Project Scenario

As a **Data Engineer** at a data analytics consulting firm, you've been tasked with **analyzing traffic congestion on national highways**. Each highway is managed by a different toll operator, each using a unique IT system and data format.

Your goal is to:
- Collect traffic data provided in **multiple formats** (CSV, TSV, and fixed-width text files).
- **Standardize** and **consolidate** this data into a single, unified dataset.
- Load the cleaned data into a **staging area** for further analysis.

## 🎯 Objectives

The Apache Airflow DAG will:

- 📥 **Extract** data from:
  - A **CSV** file
  - A **TSV** file
  - A **fixed-width text** file
- 🔄 **Transform** the data into a standardized format
- 📤 **Load** the transformed data into a **staging area**

## 🛠️ Tech Stack

- **Apache Airflow**: Orchestrating the ETL process
- **BashOperator**: Running bash commands for file operations and data extraction
- **Python**: For custom data transformation scripts
- **Pandas**: For data manipulation and transformation
- **Shell scripting**: Automating processes and managing files

## 🚀 Getting Started

To run this project locally:

1. **Clone the repository:**

   ```bash
   git clone <repo_url>
   cd ETL_Data_Pipeline
   ```

2. **Set up a Python virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Apache Airflow:**

   - Install Apache Airflow:
     ```bash
     pip install apache-airflow
     ```

   - Initialize the Airflow database:
     ```bash
     airflow db init
     ```

5. **Set up the Airflow home directory:**

   ```bash
   export AIRFLOW_HOME=/home/project/airflow
   echo $AIRFLOW_HOME
   ```

   Ensure that your Airflow home directory is properly set up and contains a `dags` folder.

6. **Place your DAG file in the Airflow DAGs folder:**

   Copy the `etl_pipeline.py` file to the `dags` directory.

   ```bash
   cp dags/etl_pipeline.py $AIRFLOW_HOME/dags
   ```

7. **Submit the DAG to Airflow:**

   To verify if the DAG was successfully added, run the following:

   ```bash
   airflow dags list
   ```

   Look for `etl_pipeline` in the list of DAGs.

8. **Trigger the DAG:**

   To manually trigger the ETL pipeline DAG:

   ```bash
   airflow dags trigger etl_pipeline
   ```

9. **Monitor the DAG Run:**

   You can monitor the progress of your DAG through the Airflow Web UI, accessible at:

   ```plaintext
   http://localhost:8080
   ```

   Alternatively, you can view DAG run status via the CLI:

   ```bash
   airflow dags list-runs -d etl_pipeline
   ```

   This command will show the status of the DAG runs, whether they are successful, failed, or running.

10. **View Tasks in the DAG:**

    To list all the tasks in your DAG:

    ```bash
    airflow tasks list etl_pipeline
    ```

    You should see tasks like `extract_data`, `transform_data`, and `load_data`.

---


