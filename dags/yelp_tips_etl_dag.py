from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import json
from sqlalchemy import create_engine
import os

# -------------------------------
# Instruction for Students
# -------------------------------
# This is a SAMPLE DAG to demonstrate how to:
# 1. Parse Yelp Business JSON data
# 2. Extract business fields
# 3. Load the data into a PostgreSQL database
#
#  You are expected to modify:
# - The JSON path
# - The database credentials
# - The target table and schema
# - Or even extend this script as needed
#
# Think of this as a starting point, not a complete solution.
# -------------------------------

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='etl_yelp_tips_to_postgres',
    default_args=default_args,
    description='Load Yelp tips data into PostgreSQL',
    schedule_interval=None,
    catchup=False,
    tags=['example', 'ETL'],
) as dag:

    def extract_and_load():
        # Modify this if needed
        json_file_path = '/opt/airflow/data/yelp_tips.json'

        if not os.path.exists(json_file_path):
            raise FileNotFoundError(f"File not found: {json_file_path}")

        tips = []
        with open(json_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                tips.append({
                    'user_id': data['user_id'],
                    'business_id': data['business_id'],
                    'text': data['text'],
                    'date': data['date'],
                    'compliment_count': data['compliment_count']
                })

        df = pd.DataFrame(tips)

        # Set your PostgreSQL connection details here
        db_user = 'your_postgres_user'
        db_password = 'your_postgres_password'
        db_host = 'your_postgres_host'
        db_port = '5432'
        db_name = 'final_project'

        db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        engine = create_engine(db_url)

        df.to_sql('Yelp_Tips', engine, if_exists='append', index=False)
        print("Yelp_Tips loaded into PostgreSQL.")

    load_task = PythonOperator(
        task_id='load_yelp_tips_to_postgres',
        python_callable=extract_and_load
    )

    load_task