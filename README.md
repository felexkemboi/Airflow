# Airflow
A project  to move data from Mysql to Postgress for Archival and Analytics.

Workflow  to scan any changes to mysql and sync them to Postgress using Airflow appache and 
It uses the following technologies:

[Appache airflow](https://airflow.apache.org/index.html).
[Postgress](https://www.postgresql.org/).
[Mysql](https://www.postgresql.org/).
[Python3](https://www.python.org/).

# Steps on how to get Started

## Create a folder and cd into the folder
`mkdir craft && cd craft`

## Create a virtualenv and activate it [More about virtualenv](https://virtualenv.pypa.io/en/latest/)
`virtualenv venv`
`source venv/bin/activate`

## Clone/Download the project  
Download via this link [clone](https://github.com/felexkemboi/Airflow.git).

## Open a new tab in terminal,activate the virtualenv
In one terminal run `airflow webserver`
On the other run `airflow scheduler`

Runs the airflow  in the browser .<br>
Open [http://0.0.0.0:8080/admin](http://0.0.0.0:8080/admin) to view it in the browser. 

The page will reload if you make edits.<br>
You will also see any lint errors in the console.

