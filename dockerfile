FROM apache/airflow:2.4.3

USER root
USER airflow

RUN pip install --no-cache-dir \
    pdfplumber \
    pandas \
    matplotlib==3.5.3 \
    seaborn==0.12.2 \
    psycopg2-binary \
    beautifulsoup4
