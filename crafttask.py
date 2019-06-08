
#Import all the libraries to be used
from airflow import DAG
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators import MySqlOperator
import datetime as dt
from datetime import datetime, timedelta
from psycopg2.extras import execute_values


default_args = {
    'owner': 'kemboi',
    'start_date': dt.datetime(2018, 9, 24, 10, 00, 00),
    'retries': 5
}

#Query to fetch all records from Mysql
sql = """ SELECT * FROM marks ;"""


#once you have cloned the project,change the path of your greet.txt
def greet():
    print('Writing in file')
    with open('/home/kemboi/Desktop/greet.txt', 'a+', encoding='utf8') as f:
        now = dt.datetime.now()
        t = now.strftime("Hi the time now is %Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return 'Greeted'


#function to test things work as expected
def respond():
    print("Hello just saying Hi")



def postgres(ds, **kwargs):

    #this should be a query to insert the data to the postgress
    query = """ SELECT *FROM marks """

    conn =  PostgresHook(postgres_conn_id='source', schema='marks').get_conn()

    # that's going to force the library to create a server cursor
    cursor = conn.cursor("serverCursor")
    cursor.execute(query)

    # now we need to close our connection
    cursor.close()

    return "Saved to the database"


#these are the tasks to be scheduled 
with DAG('craft_tasks', default_args=default_args, schedule_interval='*/1 * * * *') as dag:
    opr_hello = BashOperator(task_id='say_Hi',bash_command='echo "Hi!!"')
    opr_greet = PythonOperator(task_id='greet',python_callable=greet)
    opr_sleep = BashOperator(task_id='sleep_me', bash_command='sleep 5')
    opr_respond = PythonOperator(task_id='respond',python_callable=respond)
    mysql_op = MySqlOperator(task_id='running_query',mysql_dbid='testing', sql=sql, owner='kemboi')
    #We are suppose to add the task to add the data dumped from the sql database



opr_hello >> opr_greet >> opr_sleep >> opr_respond  >> mysql_op   #task responsible for adding records to the postgress
