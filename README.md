# 🚦 ETL Data Pipeline with Apache Airflow

This project demonstrates how to build an ETL (Extract, Transform, Load) data pipeline using **Apache Airflow** and the **BashOperator** to automate the ingestion of road traffic data from various toll plazas.

## 🧩 Project Scenario

As a **Data Engineer** at a data analytics consulting firm, you've been assigned a mission to **analyze traffic congestion on national highways**. Each highway is managed by a different toll operator, each using a unique IT system and data format.

Your goal is to:
- Collect traffic data provided in **multiple formats** (CSV, TSV, and fixed-width text files).
- **Standardize** and **consolidate** this data into a single, unified dataset.
- Load the cleaned data into a **staging area** for further analysis.

## 🎯 Objectives

In this project, the Apache Airflow DAG will:

- 📥 Extract data from:
  - A **CSV** file
  - A **TSV** file
  - A **fixed-width text** file
- 🔄 Transform the data into a standardized format
- 📤 Load the transformed data into a **staging area**

## 🛠️ Tech Stack

- **Apache Airflow**
- **BashOperator**
- **Python (for data transformation scripts)**
- **Pandas**
- **Shell scripting**

## 📁 Project Structure

```
ETL_Data_Pipeline/
│
├── dags/
│   └── etl_pipeline.py        # Main DAG definition
├── data/
│   ├── traffic_data.csv
│   ├── traffic_data.tsv
│   └── traffic_data_fixed.txt
├── scripts/
│   └── transform_data.py      # Transformation logic
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

To run this project locally:

1. Clone the repo and set up a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Set up Apache Airflow and add the DAG file to your DAGs folder.
4. Trigger the DAG from the Airflow UI.


