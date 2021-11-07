"""
Licensed under the MIT License.
Copyright (c) 2021-2031. All rights reserved.

This helper file provides feature engineering functions.
"""


def add_date_features(df, date_col):
    """
    Add date related features generated into the feature set.

    :param df: Input feature dataframe
    :param date_col: the column name of date column
    :return: 1) A dataframe with added date features 2) Added feature list
    """
    output_df = df.copy()

    output_df['Year'] = df[date_col].dt.year.astype('category')
    output_df['Month'] = df[date_col].dt.month.astype('category')
    output_df['Quarter'] = (df[date_col].dt.month - 1) // 3 + 1
    output_df['Quarter'] = df[date_col].astype('category')

    feature_lst = ['Year', 'Month', 'Quarter']

    return output_df, feature_lst


def add_threshold_grouping_features(df, original_feature, threshold):
    """
    Add a new feature to tell whether the original feature value is > or <= the threshold.

    :param df: Input feature dataframe
    :param original_feature: The existing feature used to generate the new feature
    :param threshold: The threshold to divide the original_feature into 2 groups
    :return: 1) A dataframe added new features 2) Added feature list
    """
    output_df = df.copy()
    new_feature = f'{original_feature}_larger_than_{threshold}'

    output_df.loc[output_df[original_feature] > threshold, new_feature] = 1
    output_df.loc[output_df[original_feature] <= threshold, new_feature] = 0

    return output_df, [new_feature]
