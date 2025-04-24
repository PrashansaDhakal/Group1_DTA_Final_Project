# Group1_DTA_Final_Project

# DataTech Admin Final Capstone

# Contributors

Fakhruddin Shaik,

Prashansa Dhakal


# Project Description

This project aims to deploy a fully operational data pipeline with Airflow, Superset, MinIO, Docker, and Postgres.


## Purpose

This repository serves as the foundation for learning and managing data lifecycle processes.


## Final Project Presentation
[IT4065C Final Project](https://www.canva.com/design/DAGlgKtYNKM/JsJlHjY1AlXKBGInLaCMFQ/view?utm_content=DAGlgKtYNKM&utm_campaign=designshare&utm_medium=embeds&utm_source=link)


## Directory Structure

- `.devcontainer/`: Placeholder for Codespaces configuration.
  - `devcontainer.json`: Configuration for Codespaces (optional for Phase 1)

- `data/`: Sample datasets.
  - `sample_data.csv`: Example dataset 

- `notebooks/`: Jupyter notebooks for tutorials.
  - `example_notebook.ipynb`: Example notebook 

- `dags/`: Apache Airflow workflows.
  - `elt_pipeline.py`: Example ELT pipeline script 

- `dbt/`: DBT project files.
  - `models/`: Models for DBT transformations
  - `dbt_project.yml`: DBT project configuration

- `superset/`: Superset configuration
  - `superset_config.py`: Example configuration file

- minio-config/`: Configuration for MinIO
  - `config.json`: MinIO example configuration

- `iceberg-tables/`: Definitions for Iceberg tables.
  - `create_tables.sql`: SQL scripts for creating tables

- `scripts/`: Helper scripts for data processing.
  - `ingest_data.py`:Example data ingestion script

- `docker.compose.yml`: Docker Compose to manage services 

## To-Do
1. Edit yelp_tips_etl_dag.py file
2. Load 

## In Progress
1.

## Testing

## Completed
1. Updated devcontainer.json file
2. Created compiled_dag.py file, added pgadmin, and edited credentials
3. Updated the docker-compose.yml file
4. Uploaded the large json file using Git LFS.