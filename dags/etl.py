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
    @task
    def create_table():
        # Initialize postgres hook to create table
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")

        # SQL query to create a table
        create_table_query = """

        CREATE TABLE IF NOT EXISTS apod_data (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );

        """

        # Execute the table creation query
        postgres_hook.run(create_table_query)

    # Step2: Extract data from NASA data (Extract Data Pipeline)

    # Step3: Pick information which we want (Transform Data Pipeline)

    # Step4: Put data in postgres (Load Data Pipeline)

    # Step5: Verify Data

    # Step6: Define the task dependencies