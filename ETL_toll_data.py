# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

# defining DAG arguments

default_args = {
    'owner': 'Meriam',
    'start_date': days_ago(0),
    'email': ['meriemjardakmj@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval='@daily',  # Runs daily
)

# defining the tasks
# 1. Task to unzip the data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/',
    dag=dag,
)

# 2. Task to extract data from CSV
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1,2,3,4 /home/project/airflow/dags/vehicle-data.csv > /home/project/airflow/dags/csv_data.csv',
    dag=dag,
)

# 3. Task to extract data from TSV
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -d"\t" -f1,2,3 /home/project/airflow/dags/tollplaza-data.tsv > /home/project/airflow/dags/tsv_data.csv',
    dag=dag,
)

# 4. Task to extract data from Fixed Width
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c1-10,11-20 /home/project/airflow/dags/payment-data.txt > /home/project/airflow/dags/fixed_width_data.csv',
    dag=dag,
)

# 5. Task to consolidate the extracted data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d"," /home/project/airflow/dags/csv_data.csv /home/project/airflow/dags/tsv_data.csv /home/project/airflow/dags/fixed_width_data.csv > /home/project/airflow/dags/extracted_data.csv',
    dag=dag,
)

# 6. Task to transform the data (convert vehicle type to uppercase)
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='awk -F"," \'{ print $1","$2","$3","toupper($4)","$5","$6","$7","$8","$9 }\' /home/project/airflow/dags/extracted_data.csv > /home/project/airflow/dags/staging_data.csv',
    dag=dag,
)

# Task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data