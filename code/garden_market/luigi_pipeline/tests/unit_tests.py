"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import pytest
import pandas as pd
import numpy as np

from ..helpers.feature_engineering_helpers import add_date_features, add_threshold_grouping_features
from ..helpers.model_evaluation_helpers import get_model_performance_ci

INPUT_DIR = 'testing_input/'
COLLECTED_DATA_FILE = f'{INPUT_DIR}collected_data.pkl'
PREPROCESSED_DATA_FILE = f'{INPUT_DIR}preprocessed_data.pkl'
MODEL_RESULTS_FOLDER = f'{INPUT_DIR}mljar_regression_sales'


def test_add_date_features():
    input_df = pd.read_pickle(COLLECTED_DATA_FILE)
    output_df, feature_lst = add_date_features(input_df, date_col='Date')

    input_shape = input_df.shape
    assert output_df.shape == (input_shape[0], input_shape[1] + len(feature_lst))


def test_add_threshold_grouping_features():
    input_df = pd.read_pickle(COLLECTED_DATA_FILE)
    original_feature = 'Customers'
    threshold = 3000
    new_feature = f'{original_feature}_larger_than_{threshold}'
    output_df, feature_lst = add_threshold_grouping_features(input_df,
                                                             original_feature=original_feature,
                                                             threshold=threshold)
    input_shape = input_df.shape
    assert output_df.shape == (input_shape[0], input_shape[1] + len(feature_lst))
    assert np.array_equal(output_df[new_feature].value_counts().values, [691667, 2194])


def test_get_model_performance_ci():
    features_df = pd.read_pickle(PREPROCESSED_DATA_FILE)

    cat_cols = [col for col in features_df.select_dtypes(include='category').columns if col != 'Year']
    features_df.drop(cat_cols, axis=1, inplace=True)

    test_df = features_df.loc[features_df['Year'].astype(str) == '2015']

    y_test = test_df['Sales']
    X_test = test_df.drop(['Sales', 'Date', 'Year'], axis=1)

    X_test.reset_index(inplace=True, drop=True)
    y_test.reset_index(inplace=True, drop=True)

    print(f"X_test Shape: {X_test.shape}, y_test Shape: {y_test.shape}")

    ci_lower_bound, ci_upper_bound = get_model_performance_ci(X_test, y_test, eval_metric='r2',
                                                              model_results_path=MODEL_RESULTS_FOLDER,
                                                              confidence_level=0.95, bootstrap_iters=3,
                                                              sample_size_perct=0.5)

    assert ci_lower_bound > 0 and ci_upper_bound > 0 and ci_lower_bound <= ci_upper_bound
