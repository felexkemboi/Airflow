# airflow stuff
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta

# for postgres access
import psycopg2 as pg

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2018, 6, 30),
    "email": ["felokemboi10@mail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}