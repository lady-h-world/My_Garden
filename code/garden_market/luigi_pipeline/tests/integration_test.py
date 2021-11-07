"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import pytest
import pandas as pd
import os
import luigi
import yaml
import json
from pathlib import Path
import shutil

from ..data_collection import CollectDataTask
from ..data_preprocessing import PreprocessingDataTask
from ..feature_engineering import FeatureEngineeringTask
from ..model_selection import ModelSelectionTask
from ..model_evaluation import ModelEvaluationTask
from ..data_drift_monitoring import DataDriftMonitoring

stream = open("../config.yaml", 'r')
config = yaml.load(stream, Loader=yaml.SafeLoader)


def test_data_collection():
    config['raw_data_dir'] = 'testing_input/'
    config['output_dir'] = 'testing_output/'

    output_file_path = config['output_dir'] + config['collected_data_file']
    os.remove(output_file_path) if os.path.exists(output_file_path) else None

    task = CollectDataTask(config)
    luigi.build([task], workers=1, local_scheduler=True)

    output_file = pd.read_pickle(output_file_path)
    assert output_file.shape == (693861, 18)


def test_feature_engineering():
    config['output_dir'] = 'testing_output/'

    output_file_path = config['output_dir'] + config['feature_engineered_data_file']
    os.remove(output_file_path) if os.path.exists(output_file_path) else None

    task = FeatureEngineeringTask(config)
    luigi.build([task], workers=1, local_scheduler=True)

    output_file = pd.read_pickle(output_file_path)
    assert output_file.shape == (693861, 18 + config['added_columns'])


def test_data_preprocessing():
    config['output_dir'] = 'testing_output/'
    cat_cols = config['le_cols'] + config['int_cat_cols']

    output_file_path = config['output_dir'] + config['preprocessed_data_file']
    os.remove(output_file_path) if os.path.exists(output_file_path) else None

    task = PreprocessingDataTask(config)
    luigi.build([task], workers=1, local_scheduler=True)

    output_file = pd.read_pickle(output_file_path)
    assert output_file.shape == (693861, 18 + config['added_columns'])
    assert list(set(output_file[cat_cols].dtypes))[0] == 'category'


def test_model_selection():
    config['output_dir'] = 'testing_output/'
    config['total_time_limit'] = 300
    config['validation_strategy']['k_folds'] = 3

    output_path = config['output_dir'] + config['results_path']
    output_dir = Path(output_path)
    if output_dir.exists() and output_dir.is_dir():
        shutil.rmtree(output_dir)

    task = ModelSelectionTask(config)
    luigi.build([task], workers=1, local_scheduler=True)

    leaderboard_df = pd.read_csv(output_path + '/leaderboard.csv')
    assert len(leaderboard_df) > 0


def test_model_evaluation():
    config['output_dir'] = 'testing_output/'

    output_file_path = config['output_dir'] + config['model_evaluation_output']
    os.remove(output_file_path) if os.path.exists(output_file_path) else None

    task = ModelEvaluationTask(config)
    luigi.build([task], workers=1, local_scheduler=True)

    with open(output_file_path) as f:
        model_eval_dict = json.load(f)

        assert model_eval_dict['R2'] > 0 and model_eval_dict['R2 Confidence Interval'] is not None


def test_data_drift_monitoring():
    config['output_dir'] = 'testing_output/'
    config['drift_file_path'] = 'testing_input/drifted_sales.pkl'

    output_path = config['output_dir'] + config['drift_monitor_dir']
    output_dir = Path(output_path)
    if output_dir.exists() and output_dir.is_dir():
        shutil.rmtree(output_dir)

    task = DataDriftMonitoring(config)
    luigi.build([task], workers=1, local_scheduler=True)

    report = output_path + config['report_file']
    with open(report) as f:
        data_drift_dict = json.load(f)

        assert data_drift_dict['Concept Drift PSI'] == 4.309167821031043 \
               and data_drift_dict['Covariate Drift Forecast'] > 0.9

