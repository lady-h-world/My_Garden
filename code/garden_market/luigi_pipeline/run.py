"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import luigi
import yaml

from model_evaluation import ModelEvaluationTask
from data_drift_monitoring import DataDriftMonitoring


def main():

    stream = open("config.yaml", 'r')
    config = yaml.load(stream, Loader=yaml.SafeLoader)

    if config['run_model_pipeline']:
        task = ModelEvaluationTask(config)
        luigi.build([task], workers=1, local_scheduler=True)
    if config['monitor_data_drift']:
        task = DataDriftMonitoring(config)
        luigi.build([task], workers=1, local_scheduler=True)


if __name__ == '__main__':
    main()
