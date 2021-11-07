"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import luigi
import pandas as pd
import json
from pathlib import Path
from helpers.data_drift_monitoring_helpers import check_concept_drift, check_covariate_drift


class DataDriftMonitoring(luigi.Task):
    """
    Monitor:
    * Concept drift from the target
    * Covariate drift from the features
    """
    config = luigi.DictParameter()

    def output(self):
        return luigi.LocalTarget(
            self.config['output_dir'] + self.config['drift_monitor_dir'] + self.config['report_file'])

    def run(self):
        drifted_df = pd.read_pickle(self.config['drift_file_path'])

        # train, test split for df
        train_df = drifted_df.loc[drifted_df['Year'].astype(str) < '2015']
        drifted_test_df = drifted_df.loc[drifted_df['Year'].astype(str) == '2015']

        y_train, drifted_y_test = train_df['Sales'], drifted_test_df['Sales']
        X_train, drifted_X_test = train_df.drop(['Sales', 'Date', 'Year'], axis=1), \
                                  drifted_test_df.drop(['Sales', 'Date', 'Year'], axis=1)

        X_train.reset_index(inplace=True, drop=True)
        drifted_X_test.reset_index(inplace=True, drop=True)
        y_train.reset_index(inplace=True, drop=True)
        drifted_y_test.reset_index(inplace=True, drop=True)

        # create the output folder if not exists
        output_folder = self.config['output_dir'] + self.config['drift_monitor_dir']
        path = Path(output_folder)
        path.mkdir(parents=True, exist_ok=True)

        # check concept drift
        psi = check_concept_drift(y_train, drifted_y_test, title='Distributions of y_train vs drifted_y_test',
                                  legend1='y_train', legend2='drifted_y_test', xlabel='Sales',
                                  saved_file=output_folder + 'target_dist_comparision.png')

        # check covariate drift
        new_X_train = X_train.copy()
        new_X_test = drifted_X_test.copy()
        new_X_train['label'] = 0
        new_X_test['label'] = 1

        combo_df = new_X_train.append(new_X_test)
        combo_df = combo_df.sample(frac=1).reset_index(drop=True)  # shuffle the dataframe
        y = combo_df['label']
        X = combo_df.drop('label', axis=1)
        avg_performance = check_covariate_drift(X, y,
                                                fig_path=output_folder + 'drift_features.png', n_splits=10)

        report = {'Concept Drift PSI': psi, 'Covariate Drift Forecast': avg_performance}

        with open(output_folder + self.config['report_file'], 'w') as f:
            json.dump(report, f)
