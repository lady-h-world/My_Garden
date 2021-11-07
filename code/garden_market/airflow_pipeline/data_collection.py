from datetime import datetime
import pandas as pd
import os

from airflow.decorators import dag, task
from airflow.operators.python_operator import PythonOperator


@dag(dag_id='hanhan_data_collection', schedule_interval=None, 
     start_date=datetime(2021, 1, 1), catchup=False, tags=['example'])
def data_collection():

    def load_data():
        path_to_csv = os.path.join('~/airflow/data','leaf.csv') 
        df = pd.read_csv(path_to_csv)
        print(df.shape)



    data_load_task = PythonOperator(task_id='load_data_task', python_callable=load_data)
    data_load_task


# dag invocation
data_collection_dag = data_collection()
