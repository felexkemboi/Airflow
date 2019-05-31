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

dag = DAG("update_sale_statuses", default_args=default_args, schedule_interval='@daily', catchup=False)
#copy the data to postgresss

def fetch(ds, **kwargs):
    conn = pg.connect("host=localhost dbname=airflow user=airflow password=airflow")
    cur = conn.cursor()
    #cur.copy_from(f, 'sale_statuses', sep=',')
    conn.commit()
    f.close()