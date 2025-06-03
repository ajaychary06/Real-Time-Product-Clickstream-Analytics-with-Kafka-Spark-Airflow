from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'kafka_spark_streaming_pipeline',
    default_args=default_args,
    description='Run Spark Structured Streaming Consumer',
    schedule_interval=None,
    catchup=False
)

start_spark_streaming = BashOperator(
    task_id='start_spark_streaming',
    bash_command="""
        export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 &&
        export PATH=$JAVA_HOME/bin:$PATH &&
        export PYSPARK_PYTHON=python3 &&
        cd "/mnt/c/Users/ajayc/OneDrive/Desktop/real time product pipeline/spark" &&
        python3 spark_streaming_consumer.py
    """,
    dag=dag,
)
