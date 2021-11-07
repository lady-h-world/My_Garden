"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import luigi
import pandas as pd
import pprint
import sys
pprint.pprint(sys.path)
sys.path.append(sys.path[0]+'\\luigi_pipeline')

from data_collection import CollectDataTask
from helpers.feature_engineering_helpers import add_date_features, add_threshold_grouping_features


class FeatureEngineeringTask(luigi.Task):
    """
    Feature engineering:

    * Add user required (config) features
    * Re-order columns
    """
    config = luigi.DictParameter()

    def requires(self):
        return CollectDataTask(self.config)

    def output(self):
        return luigi.LocalTarget(self.config['output_dir'] + self.config['feature_engineered_data_file'])

    def run(self):
        fe_fun_map = {
            'add_date_features': add_date_features,
            'add_threshold_grouping_features': add_threshold_grouping_features
        }

        feature_engineered_df = pd.read_pickle(self.config['output_dir'] + self.config['collected_data_file'])

        # Add features
        feature_adding_dct = self.config['feature_adding_dct']

        added_features = []
        for feature_adding_fun, params in feature_adding_dct.items():
            feature_engineered_df, feature_lst = fe_fun_map[feature_adding_fun](feature_engineered_df, **params)
            added_features.extend(feature_lst)

        # Reorder the columns
        reordered_cols = ['Store', 'Date'] + added_features + ['StoreType', 'Assortment', 'CompetitionDistance',
                                                               'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear',
                                                               'Promo2', 'Promo2SinceWeek', 'Promo2SinceYear',
                                                               'PromoInterval', 'DayOfWeek',
                                                               'Sales', 'Customers', 'Open', 'Promo',
                                                               'StateHoliday', 'SchoolHoliday']
        feature_engineered_df = feature_engineered_df[reordered_cols]

        print(f'feature Engineered Data Shape: {feature_engineered_df.shape}')
        feature_engineered_df.to_pickle(self.config['output_dir'] + self.config['feature_engineered_data_file'])
