"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import pandas as pd
import numpy as np
import os

import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import balanced_accuracy_score

from zenml.pipelines import pipeline
from zenml.steps import step
from zenml.steps.step_output import Output
from zenml.steps.base_step_config import BaseStepConfig

class pipeline_config(BaseStepConfig):
    """
    Params used in the pipeline
    """
    label: str = 'species'

@step
def split_data(config: pipeline_config) -> Output(
    X=pd.DataFrame, y=pd.DataFrame
):
    path_to_csv = os.path.join('~/airflow/data', 'leaf.csv')
    df = pd.read_csv(path_to_csv)
    label = config.label

    y = df[[label]]
    X = df.drop(label, axis=1)

    return X, y


@step
def train_evaltor(
        config: pipeline_config,
        X: pd.DataFrame,
        y: pd.DataFrame
) -> float:
    y = y[config.label]

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

    return avg_performance


@pipeline
def super_mini_pipeline(
    data_spliter,
    train_evaltor
):
    X, y = data_spliter()
    train_evaltor(X=X, y=y)


# run the pipeline
pipeline = super_mini_pipeline(data_spliter=split_data(),
                                train_evaltor=train_evaltor())
DAG = pipeline.run()
