# Airflow
A project  to move data from Mysql to Postgress for Archival and Analytics.

Workflow  to scan any changes to mysql and sync them to Postgress using Airflow appache and 
It uses the following technologies:

[Appache airflow](https://airflow.apache.org/index.html).<br>
[Postgress](https://www.postgresql.org/).<br>
[Mysql](https://www.postgresql.org/).<br>
[Python3](https://www.python.org/).

# Steps on how to get Started

## Create a folder and cd into the folder
`mkdir craft && cd craft`

## Create a virtualenv and activate it [More about virtualenv](https://virtualenv.pypa.io/en/latest/)
`virtualenv venv` <br>
`source venv/bin/activate`

## Clone/Download the project  
Download via this link [clone](https://github.com/felexkemboi/Airflow.git).

## Open a new tab in terminal,activate the virtualenv
In one terminal run `airflow webserver` <br>
On the other run `airflow scheduler`

Runs the airflow  in the browser .<br>
Open [http://0.0.0.0:8080/admin](http://0.0.0.0:8080/admin) to view it in the browser. 

Guess what,this is my welcome page when i visit one my scheduled tasks
### DAG [craft_tasks] is now fresh as a daisy .<br>

