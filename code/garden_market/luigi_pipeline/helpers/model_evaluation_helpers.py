"""
Licensed under the MIT License.
Copyright (c) 2021-2031. All rights reserved.

The helpers are used for model evaluation.
"""
from supervised.automl import AutoML
import numpy as np
from tqdm import tqdm
from sklearn.metrics import r2_score, balanced_accuracy_score
from sklearn.utils import resample
import warnings
warnings.filterwarnings('ignore')


EVAL_FUN_MAPPING = {
    'r2': r2_score,
    'balanced_accuracy': balanced_accuracy_score
}


def get_model_performance_ci(X_test, y_test, eval_metric, model_results_path,
                             confidence_level=0.95, bootstrap_iters=1000, sample_size_perct=0.5):
    sample_performance_lst = []
    eval_fun = EVAL_FUN_MAPPING[eval_metric]
    loaded_automl = AutoML(results_path=model_results_path)

    with tqdm(total=bootstrap_iters) as progress_bar:
        for i in range(bootstrap_iters):
            X_test_sample = resample(X_test, n_samples=int(len(X_test) * sample_size_perct))
            y_test_sample = y_test.iloc[X_test_sample.index]

            y_pred_sample = loaded_automl.predict(X_test_sample)

            performance_score = eval_fun(y_test_sample, y_pred_sample)
            sample_performance_lst.append(performance_score)

            progress_bar.update(1)

    alpha = 1 - confidence_level
    lower_p = alpha * 100 / 2.0
    lower_bound = max(0.0, np.percentile(sample_performance_lst, lower_p))
    upper_p = (confidence_level + alpha / 2.0) * 100
    upper_bound = min(1.0, np.percentile(sample_performance_lst, upper_p))

    print(
        f"There's {confidence_level * 100}% likelihood that R2 score between "
        f"[{lower_bound}, {upper_bound}] covers the true model performance")

    return lower_bound, upper_bound
