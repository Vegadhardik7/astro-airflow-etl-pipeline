from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json

# Define the DAG
with DAG(
    dag_id="nasa_apod_postgres",
    start_date=days_ago(1),
    schedule='@daily',
    catchup=False
) as dag:
    
    # Step1: Create table if doesn't exists

    # Step2: Extract data from NASA data (Extract Data Pipeline)

    # Step3: Pick information which we want (Transform Data Pipeline)

    # Step4: Put data in postgres (Load Data Pipeline)

    # Step5: Verify Data

    # Step6: Define the task dependencies