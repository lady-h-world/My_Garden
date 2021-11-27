"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import luigi
import pandas as pd
from sklearn import preprocessing
import pprint
import sys
pprint.pprint(sys.path)
sys.path.append(sys.path[0]+'\\luigi_pipeline')

from feature_engineering import FeatureEngineeringTask


class PreprocessingDataTask(luigi.Task):
    """
    Preprocessing collected data:

    * Categorical features --> "category"
    """
    config = luigi.DictParameter()

    def requires(self):
        return FeatureEngineeringTask(self.config)

    def output(self):
        return luigi.LocalTarget(self.config['output_dir'] + self.config['preprocessed_data_file'])

    def run(self):
        preprocessed_data = pd.read_pickle(self.config['output_dir'] + self.config['feature_engineered_data_file'])

        # Label encoding categorical variables and convert to "category" type
        le = preprocessing.LabelEncoder()
        le_cols = self.config['le_cols']
        int_cat_cols = self.config['int_cat_cols']

        for le_col in le_cols:
            preprocessed_data[le_col] = le.fit_transform(preprocessed_data[le_col])
            preprocessed_data[le_col] = preprocessed_data[le_col].astype('category')

        for int_cat_col in int_cat_cols:
            preprocessed_data[int_cat_col] = preprocessed_data[int_cat_col].astype('category')

        print(f'Preprocessed Data Shape: {preprocessed_data.shape}')
        preprocessed_data.to_pickle(self.config['output_dir'] + self.config['preprocessed_data_file'])
