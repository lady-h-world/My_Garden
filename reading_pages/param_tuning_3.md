### Experiment 1 - Optimization with Default Settings

Since FLAML provides some automated decision making mechanism, Lady H. wanted to see how powerful FLAML and Optuna are in default settings.

#### LGBM for Leaves30

She started with a simple case, using LGBM with default settings to classify the 30-class leaves. 

In FLAML, to use defulat settings only need to create an `AutoML` instance with a few mandatory settings such as time budget, metric, estimator(s) and log location. By settings `n_splits` and `split_type`, in this case it's telling FLAML to run 5-fold cross validation with stratified split. As mentioned before, FLAML provides automated decision making in between cross validation and holdout, but once the user has made the decision in this AutoML instance, FLAML will obey user's settings.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_flaml_default_df30.png" width="1067" height="290" />
</p>

the log file records information in each trial, therefore at the end of FLAML optimization, we can plot its learning curve as below. As we can see, it takes less time to make an improvement in the early stage but in the later stage, it takes longer time to make further performance increase.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/learning_curve_default_leaves30.png" width="390" height="273" />
</p>

To use Optuna default settings with cross validation, users need to use its integrated CV functions, such as `LightGBMTunerCV()` function. However, not every supported model has integrated CV methods.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_optuna_default_df100.png" width="1067" height="407" />
</p>

Given the same 300 seconds time budget, Optuna got a little bit better testing performance, but none of their results is ideal.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/default_leaves30.png" width="658" height="223" />
</p>

* 🌻 [To look into FLAML experiment details >>][1]
* 🌻 [To look into Optuna experiment details >>][2]

#### LGBM for Leaves100

Before making further improvement on Leaves30 classification, Lady H. decided to experiment on a larger dataset and try out different search strategies first. Her motivation was mainly to gain a more complete observation. The dataset, Leaves100 has 100 classes of leaves, each class has 16 records and each record has 192 features. So this is a high dimensional multi-class dataset.

FLAML has 2 main suggested search strategies, CFO and Blend Search.

* [CFO][3] is a search algorithm designed to address the large training cost variation caused by the hyperparameters. It starts from a low-cost initial point and gradually moves towards low-cost region with self-adjustable step size. At the same time, it attempts to avoid high-cost and high-loss hyperparameters. It also reduces the chance of getting trapped in a local optimum with the randomized restarting logic.

* [Blend Search][4] is a better option for a large search space. Combining the benefits of local and global search, it has an economical way to decide the exploration path. Same as CFO, Blend Search starts with a low-cost initial point, but different from CFO, it will try new starting points without waiting for the local search to be fully converged.

CFO is the default search strategy in FLAML, according to FLAML researchers, it works better than Blend Search most of the time in practice.


TPE (Tree-structured Parzen Estimator) applies bayesian theorem, that `P(y|x) = P(x|y) * P(y) / P(x)`.

* `P(x|y)` means, given the objective function's score, what's the probability of the hyperparameters. When there are multiple hyperparameters, this formula assumes they are independent from each other, and this is also why TPE is an independent sampler in Optuna.
* `P(h|o) = l(x) is there is an improvement in objective function, otherwise P(h|o) = g(x)`
  * On each trial, for each parameter, TPE fits one Gaussian Mixture Model (GMM) `l(x)` to the set of parameter values associated with the best objective values, and another GMM `g(x)` to the remaining parameter values. It chooses the parameter value `x` that maximizes the ratio `l(x)/g(x)`.
* 🌻 [To check more about TPE >>][5]


<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/default_leaves100.png" width="790" height="349" />
</p>


* 🌻 [To look into FLAML experiment details >>][1]
* 🌻 [To look into Optuna experiment details >>][2]



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/flaml_experiments/flaml_default.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_default.ipynb
[3]:https://github.com/microsoft/FLAML/tree/main/flaml/tune#cfo-frugal-optimization-for-cost-related-hyperparameters
[4]:https://github.com/microsoft/FLAML/tree/main/flaml/tune#blendsearch-economical-hyperparameter-optimization-with-blended-search-strategy
[5]:https://towardsdatascience.com/a-conceptual-explanation-of-bayesian-model-based-hyperparameter-optimization-for-machine-learning-b8172278050f
