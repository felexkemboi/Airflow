
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


import datetime as dt
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators import MySqlOperator
from datetime import datetime, timedelta
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from psycopg2.extras import execute_values


default_args = {
    'owner': 'kemboi',
    'start_date': dt.datetime(2018, 9, 24, 10, 00, 00),
    'retries': 5
}

sql = """ SELECT * FROM marks ;"""

def greet():
    print('Writing in file')
    with open('/home/kemboi/Desktop/greet.txt', 'a+', encoding='utf8') as f:
        now = dt.datetime.now()
        t = now.strftime("Hi the time now is %Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return 'Greeted'


def respond():
    print("Hello just saying Hi")



def postgres(ds, **kwargs):


    #this should be a query to insert the data to the postgress
    query = """ SELECT *FROM marks """

    conn =  PostgresHook(postgres_conn_id='source', schema='marks').get_conn()
    #dest_conn = PostgresHook(postgres_conn_id='dest',   schema='mak').get_conn()

    # notice this time we are naming the cursor for the origin table
    # that's going to force the library to create a server cursor
    cursor = conn.cursor("serverCursor")
    cursor.execute(query)

    # now we need to close our connection
    cursor.close()

with DAG('craft_tasks', default_args=default_args, schedule_interval='*/1 * * * *') as dag:
    opr_hello = BashOperator(task_id='say_Hi',bash_command='echo "Hi!!"')
    opr_greet = PythonOperator(task_id='greet',python_callable=greet)
    opr_sleep = BashOperator(task_id='sleep_me', bash_command='sleep 5')
    opr_respond = PythonOperator(task_id='respond',python_callable=respond)
    mysql_op = MySqlOperator(task_id='running_query',mysql_dbid='testing', sql=sql, owner='kemboi')
    #We are suppose to add the task to add the data dumped from the sql database



opr_hello >> opr_greet >> opr_sleep >> opr_respond  >> mysql_op   #task responsible for adding records to the postgress
