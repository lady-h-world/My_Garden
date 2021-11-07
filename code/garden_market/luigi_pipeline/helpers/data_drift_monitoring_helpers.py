"""
Licensed under the MIT License.
Copyright (c) 2021-2031. All rights reserved.

The helpers are used for data drift monitoring.
"""
import numpy as np
from tqdm import tqdm
from matplotlib import pylab as plt

import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import balanced_accuracy_score

from .psi import calculate_psi
import seaborn as sns
sns.set(color_codes=True)


def check_concept_drift(s1, s2, title, legend1, legend2, xlabel, saved_file):
    fig = plt.figure(figsize=(15, 5))
    sns.kdeplot(s1, label=f'{legend1} distribution', color='green')
    sns.kdeplot(s2, label=f'{legend2} distribution', color='purple')
    plt.legend()
    plt.xlabel(f'{xlabel}')
    plt.ylabel('Density')

    psi = calculate_psi(s1, s2, buckettype='quantiles', buckets=100, axis=1)
    plt.title(f'{title} (PSI: {psi})', fontsize=18)

    plt.savefig(saved_file)

    return psi


def check_covariate_drift(X, y, fig_path, n_splits=10):
    # baseline performance through cross validation
    folds = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=10)
    lgbm = lgb.LGBMClassifier(objective='binary', random_state=10)
    metrics_lst = []

    for train_idx, val_idx in tqdm(folds.split(X, y), total=folds.get_n_splits()):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]

        lgbm.fit(X_train, y_train)
        y_pred = lgbm.predict(X_val)

        cv_balanced_accuracy = balanced_accuracy_score(y_val, y_pred)
        metrics_lst.append(cv_balanced_accuracy)

    avg_performance = round(np.mean(metrics_lst), 4)

    if avg_performance >= 0.6:
        fig = lgb.plot_importance(lgbm)
        fig.figure.savefig(fig_path)

    return avg_performance
