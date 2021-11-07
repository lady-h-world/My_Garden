"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import luigi
import pandas as pd
from supervised.automl import AutoML
import pprint
import sys
pprint.pprint(sys.path)
sys.path.append(sys.path[0]+'\\luigi_pipeline')

from data_preprocessing import PreprocessingDataTask

import warnings
warnings.filterwarnings('ignore')


class ModelSelectionTask(luigi.Task):
    """
    Model selection:

    * MLJAR automl package will select the model and tune params to deliver an optimal output
    """
    config = luigi.DictParameter()

    def requires(self):
        return PreprocessingDataTask(self.config)

    def output(self):
        return luigi.LocalTarget(self.config['output_dir'] + self.config['results_path'])

    def run(self):
        features_df = pd.read_pickle(self.config['output_dir'] + self.config['preprocessed_data_file'])

        cat_cols = [col for col in features_df.select_dtypes(include='category').columns if col != 'Year']
        features_df.drop(cat_cols, axis=1, inplace=True)
        train_df = features_df.loc[features_df['Year'].astype(str) < '2015']

        y_train = train_df['Sales']
        X_train = train_df.drop(['Sales', 'Date', 'Year'], axis=1)

        X_train.reset_index(inplace=True, drop=True)
        y_train.reset_index(inplace=True, drop=True)

        print(f"X_train Shape: {X_train.shape}, y_train Shape: {y_train.shape}")

        automl = AutoML(mode=self.config['mode'], eval_metric=self.config['eval_metric'],
                        explain_level=self.config['explain_level'], random_state=self.config['random_state'],
                        results_path=self.config['output_dir'] + self.config['results_path'],
                        total_time_limit=self.config['total_time_limit'],
                        validation_strategy={
                            'validation_type': self.config['validation_strategy']['validation_type'],
                            'k_folds': self.config['validation_strategy']['k_folds'],
                            'shuffle': self.config['validation_strategy']['shuffle'],
                            'stratify': self.config['validation_strategy']['stratify'],
                            'random_seed': self.config['validation_strategy']['random_seed']
                        })

        automl.fit(X_train, y_train)
