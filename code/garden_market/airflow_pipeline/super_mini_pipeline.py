"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
from datetime import datetime
import pandas as pd
import numpy as np
import os

import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import balanced_accuracy_score

from airflow.decorators import dag, task
from airflow.operators.python_operator import PythonOperator


@dag(dag_id='super_mini_pipeline', schedule_interval=None, 
     start_date=datetime(2021, 11, 5), catchup=False, tags=['ml_pipeline'])
def baseline_pipeline():

    def all_in_one(label):
        path_to_csv = os.path.join('~/airflow/data','leaf.csv') 
        df = pd.read_csv(path_to_csv)

        y = df[label]
        X = df.drop(label, axis=1)

        folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=10)
        lgbm = lgb.LGBMClassifier(objective='multiclass', random_state=10)
        metrics_lst = []

        for train_idx, val_idx in folds.split(X, y):
            X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
            X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
            
            lgbm.fit(X_train, y_train)
            y_pred = lgbm.predict(X_val)
            
            cv_balanced_accuracy = balanced_accuracy_score(y_val, y_pred)
            metrics_lst.append(cv_balanced_accuracy)
        
        avg_performance = np.mean(metrics_lst)

        print(f"Avg Performance: {avg_performance}")


    all_in_one_task = PythonOperator(task_id='all_in_one_task', python_callable=all_in_one, op_kwargs={'label':'species'})
    all_in_one_task 


# dag invocation
pipeline_dag = baseline_pipeline()
