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
```html
<div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAGlgKtYNKM/JsJlHjY1AlXKBGInLaCMFQ/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGlgKtYNKM&#x2F;JsJlHjY1AlXKBGInLaCMFQ&#x2F;view?utm_content=DAGlgKtYNKM&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">IT4065C Final Project</a> by Fakhruddin Shaik
 ```

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