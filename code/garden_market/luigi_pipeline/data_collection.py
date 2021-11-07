"""
Licensed under the MIT License.

Copyright (c) 2021-2031. All rights reserved.
"""
import luigi
import pandas as pd


class CollectDataTask(luigi.Task):
    """
    Collect data from the raw data sources.
    """
    config = luigi.DictParameter()

    def output(self):
        return luigi.LocalTarget(self.config['output_dir'] + self.config['collected_data_file'])

    def run(self):
        store_df = pd.read_csv(self.config['raw_data_dir'] + self.config['raw_store_file'],
                               dtype={k: v for k, v in self.config['store_dtype'].items()})

        sales_df = pd.read_csv(self.config['raw_data_dir'] + self.config['raw_sales_file'],
                               dtype={k: v for k, v in self.config['sales_dtype'].items()},
                               parse_dates=[self.config['date_col']])
        store_df[list(self.config['impute_cols'])] = store_df[list(self.config['impute_cols'])].fillna('-1')
        store_df = store_df.dropna(how='any')

        store_sales_df = store_df.merge(sales_df, on=self.config['merge_key'])

        print(f'Collected data shape: {store_sales_df.shape}')
        store_sales_df.to_pickle(self.config['output_dir'] + self.config['collected_data_file'])
