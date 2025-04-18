"""
Sample ETL Pipeline DAG for Capstone Project Phase 2 – IT4065C: Data Technologies Administration

This example DAG demonstrates how to:
- Extract data from multiple file formats: CSV (retail), JSON (business data), and PDF (financial report)
- Perform basic transformation and validation
- Load clean data into PostgreSQL tables using Airflow and PythonOperator

Instructions:
- Customize file paths to match your Docker volume or Airflow environment.
- Ensure your PostgreSQL tables match the expected schema.
- Use this DAG as a reference. Do not copy it without adapting to your specific project data and structure.

Author: Isaac Kofi Nti
Date: April 2025
"""

# Import necessary libraries
from __future__ import annotations
import pendulum
import os
import pandas as pd
import json
import pdfplumber
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Set default paprameters, who own this Dag file, start data and number of retries
default_args = {
    "owner": "airflow",
    "start_date": pendulum.datetime(2025, 2, 2, tz="UTC"),
    "retries": 1,
}
#Define DAG 
dag = DAG(
    dag_id="Final_Project_Data_processing",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="DAG to extract, transform, and load Final Project data into PostgreSQL",
    tags=['ETL', 'PostgreSQL']
)
# Make sure you customize file paths to match your Docker volume or Airflow environment
CSV_FILE = "/opt/airflow/data/Online Retail.csv"
JSON_FILE = "/opt/airflow/data/yelp_academic_dataset_business.json"
PDF_FILE = "/opt/airflow/data/BBKBLK Limited Financial Report.pdf"

# Define a function to load and extract CSV File
def extract_csv():
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError(f"CSV file not found: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE,encoding='ISO-8859-1')
    return df.to_dict(orient="records")

# Define a function to load and extract JSON File
def extract_json():
    records = []
    if not os.path.exists(JSON_FILE):
        raise FileNotFoundError(f"JSON file not found: {JSON_FILE}")
    with open(JSON_FILE, "r", encoding='utf-8') as f:
        for line in f:
            records.append(json.loads(line))
    return records
# Define a function to load and extract PDF File
def extract_pdf():
    if not os.path.exists(PDF_FILE):
        raise FileNotFoundError(f"PDF file not found: {PDF_FILE}")
    with pdfplumber.open(PDF_FILE) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return {"annual_report_text": text}

# Define a function to load and save extracted files into postgres
def load_to_postgres(**kwargs):
    pg_hook = PostgresHook(postgres_conn_id="postgres_default") #This connection ID must be the same in your airflow
    conn = pg_hook.get_conn()
    cursor = conn.cursor()

    retail_data = kwargs["ti"].xcom_pull(task_ids="extract_csv") or []
    yelp_data = kwargs["ti"].xcom_pull(task_ids="extract_json") or []
    report_data = kwargs["ti"].xcom_pull(task_ids="extract_pdf") or {"annual_report_text": ""}

    try:
        for row in retail_data:
            cursor.execute("""
                INSERT INTO online_retail (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (InvoiceNo) DO NOTHING
            """, (
                row["InvoiceNo"], row["StockCode"], row["Description"], row["Quantity"],
                row["InvoiceDate"], row["UnitPrice"], row["CustomerID"], row["Country"]
            ))

        for business in yelp_data:
            cursor.execute("SELECT 1 FROM yelp_business WHERE business_id = %s", (business["business_id"],))
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO yelp_business (
                        business_id, name, address, city, state, postal_code, latitude, longitude, 
                        stars, review_count, is_open, categories
                    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (business_id) DO NOTHING
                """, (
                    business["business_id"], business["name"], business["address"], business["city"],
                    business["state"], business["postal_code"], business["latitude"], business["longitude"],
                    business["stars"], business["review_count"], business["is_open"], business["categories"]
                ))

        cursor.execute("""
            INSERT INTO annual_reports (report_text)
            VALUES (%s)
        """, (report_data["annual_report_text"],))

        conn.commit()
        logger.info("Data loaded successfully!")

    except Exception as e:
        conn.rollback()
        logger.error("Error loading data: %s", e)
        raise
    finally:
        cursor.close()
        conn.close()

with dag:
    extract_csv_task = PythonOperator(
        task_id='extract_csv',
        python_callable=extract_csv
    )

    extract_json_task = PythonOperator(
        task_id='extract_json',
        python_callable=extract_json
    )

    extract_pdf_task = PythonOperator(
        task_id='extract_pdf',
        python_callable=extract_pdf
    )

    load_to_postgres_task = PythonOperator(
        task_id='load_to_postgres',
        python_callable=load_to_postgres,
        provide_context=True
    )
 # Set task dependencies
    #extract_csv_task >> extract_json_task >> extract_pdf_task >> load_to_postgres_task
    # Parallel execution of extraction tasks
    [extract_csv_task, extract_json_task, extract_pdf_task] >> load_to_postgres_task