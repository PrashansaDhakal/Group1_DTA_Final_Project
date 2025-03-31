from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import os

# -------------------------------
# Instruction for Students
# -------------------------------
# This is a SAMPLE DAG to demonstrate how to:
# 1. Parse online retail data
# 2. Extract data fields
# 3. Load the data into a PostgreSQL database
#
# You are expected to modify:
# - The excel path
# - The database credentials
# - The target table and schema
#
# Think of this as a starting point, not a complete solution.
# -------------------------------

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='etl_online_retail_to_postgres',
    default_args=default_args,
    description='ETL pipeline to load Online Retail Excel data into PostgreSQL',
    schedule_interval=None,
    catchup=False,
    tags=['example', 'ETL'],
) as dag:

    def load_online_retail():
        file_path = '/workspaces/Group1_DTA_Final_Project/data/Online Retail.xlsx'

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        df = pd.read_excel(file_path)

        # Set your PostgreSQL connection details
        db_user = 'your_postgres_user'
        db_password = 'your_postgres_password'
        db_host = 'your_postgres_host'
        db_port = '5432'
        db_name = 'final_project'

        db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        engine = create_engine(db_url)

        df.to_sql('Online_Retail', engine, if_exists='append', index=False)
        print("Data loaded into Online_Retail table.")

    load_task = PythonOperator(
        task_id='load_online_retail_to_postgres',
        python_callable=load_online_retail
    )

    load_task