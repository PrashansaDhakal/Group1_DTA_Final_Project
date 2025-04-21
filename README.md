# Group1_DTA_Final_Project

# DataTech Admin Final Capstone

# Contributors

Fakhruddin Shaik,

Prashansa Dhakal


# Project Description
This capstone project demonstrates the implementation of a complete data pipeline using Apache Airflow, PostgreSQL, pgAdmin, Jupyter Notebook, and Docker. The goal was to ingest, transform, and analyze multi-format datasets (CSV, JSON, PDF), and generate actionable business insights.

The pipeline automates the ELT (Extract, Load, Transform) process and concludes with visual data exploration using Python (Pandas, Matplotlib).


## Purpose

The purpose of this project is to simulate a real-world data engineering environment by implementing a complete data pipeline using industry-standard tools and understand how to:

- Automate data ingestion, transformation, and storage across multiple formats (CSV, JSON, PDF).
- Orchestrate workflows using Apache Airflow and containerize applications with Docker.
- Manage and query relational databases using PostgreSQL and pgAdmin.
- Perform advanced analytics in Python to extract actionable business insights.
- Collaborate effectively via GitHub using best practices for version control and project tracking.

This capstone integrates data pipelines, analytics, and visualization into a unified project that simulates real-world data engineering and analytics roles.


## Directory Structure

- `.devcontainer/`: Placeholder for Codespaces configuration.
  - `devcontainer.json`: Configuration for Codespaces (optional for Phase 1)

- `config/`: Houses SQL files used
  - `create_tables.sql`: SQL code used for creating the tables

- `dags/`: Apache Airflow workflows.
  - `compiled_dag.py`: Main ETL pipeline DAG

- `data/`: Datasets.
  - `Online Retail.csv`
  - `yelp_academic_dataset_business.json`
  - `BBKBLK Limited Financial Report.pdf`

- `notebooks/`: Jupyter notebooks for analysis & plots
  - `DataTechAdmin.ipynb`

- `docker.compose.yml`: Docker Compose to manage services 
-  `Dockerfile`: Custom Airflow image with extra Python packages


## Technologies Used

Apache Airflow

Docker & Docker Compose

PostgreSQL + pgAdmin

Jupyter Notebook (Pandas, Matplotlib)

Python 3.7

pdfplumber for PDF parsing


## Key Business Questions Answered

**Online Retail Dataset (CSV)**
Which products are top-selling and least-selling based on quantity and revenue? How does this vary monthly?

How many transactions were canceled, and which products/customers are most involved?

**Yelp Business Dataset (JSON)**
What are the most common business categories, and how do their average ratings and review counts compare?

What are the top-rated businesses (stars ≥ 4.5) in a selected city, and what types of businesses are they?


## Analysis Summary
**Analytics Technique Used**
The team used Python and Pandas within Jupyter Notebook to perform all data analytics.

SQL was used for querying PostgreSQL via Airflow DAG scripts.

**How Insights Were Derived**
Data was loaded and transformed using Airflow DAGs and PostgreSQL.

Exploratory Data Analysis (EDA) was performed in Python notebooks using charts and aggregations.

Business questions were directly answered through targeted visualizations and filtering.

**Business Implications**
Retailers can identify high-revenue and low-performing products and adjust inventory or promotions accordingly.

Cancellation analysis highlights operational inefficiencies and frequent refund items.

Local business platforms can use category and rating data to improve listing strategies.

Entrepreneurs benefit from knowing top-rated business types in specific cities.


## To-Do

## In Progress

## Testing


## Completed
1. Updated devcontainer.json file
2. Created compiled_dag.py file, added pgadmin, and edited credentials
3. Updated the docker-compose.yml file
4. Uploaded the large json file using Git LFS.
5. DAG built for extracting CSV, JSON, and PDF data
6. PostgreSQL and pgAdmin setup with working tables
7. ETL tested in Airflow; logs validated
8. Jupyter Notebook connected to PostgreSQL
9. Visualizations created and interpreted
10. README, screenshots, and report submitted