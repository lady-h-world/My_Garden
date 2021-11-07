"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import luigi
import pandas as pd
import json
from supervised.automl import AutoML
from sklearn.metrics import r2_score
import pprint
import sys
pprint.pprint(sys.path)
sys.path.append(sys.path[0]+'\\luigi_pipeline')

from data_preprocessing import PreprocessingDataTask
from model_selection import ModelSelectionTask
from helpers.model_evaluation_helpers import get_model_performance_ci


class ModelEvaluationTask(luigi.Task):
    """
    Model evaluation:

    * Load selected model and evaluate the testing data prediction
    * Calculate the confidence interval of model performance
    """
    config = luigi.DictParameter()

    def requires(self):
        return [PreprocessingDataTask(self.config), ModelSelectionTask(self.config)]

    def output(self):
        return luigi.LocalTarget(self.config['output_dir'] + self.config['model_evaluation_output'])

    def run(self):
        features_df = pd.read_pickle(self.config['output_dir'] + self.config['preprocessed_data_file'])

        cat_cols = [col for col in features_df.select_dtypes(include='category').columns if col != 'Year']
        features_df.drop(cat_cols, axis=1, inplace=True)

        test_df = features_df.loc[features_df['Year'].astype(str) == '2015']

        y_test = test_df['Sales']
        X_test = test_df.drop(['Sales', 'Date', 'Year'], axis=1)

        X_test.reset_index(inplace=True, drop=True)
        y_test.reset_index(inplace=True, drop=True)

        print(f"X_test Shape: {X_test.shape}, y_test Shape: {y_test.shape}")

        loaded_automl = AutoML(results_path=self.config['output_dir'] + self.config['results_path'])
        y_pred = loaded_automl.predict(X_test)

        model_performance = r2_score(y_test, y_pred)
        ci_lower_bound, ci_upper_bound = get_model_performance_ci(X_test, y_test, eval_metric='r2',
                                                                  model_results_path=self.config['output_dir'] +
                                                                                     self.config['results_path'],
                                                                  confidence_level=0.95, bootstrap_iters=10,
                                                                  sample_size_perct=0.5)

        out_dct = {'R2': model_performance,
                   'R2 Confidence Interval': f'[{ci_lower_bound}, {ci_upper_bound}]'}

        with open(self.config['output_dir'] + self.config['model_evaluation_output'], 'w') as f:
            json.dump(out_dct, f)
