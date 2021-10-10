### Experiment 1 - Optimization with Default Settings

In Lady H.'s past journey, a real world project often starts from building the prototype, and the prototype often starts with a baseline result which will be compared with the future enhanced solutions. To quickly generate the baseline result, an efficient way is to choose 1 or more models and experiment with their default settings.

Therefore, Lady H. wanted to test the power of FLAML and Optuna under default settings.

#### LGBM for Leaves30

She started with a simple case, using LGBM with default settings to classify the 30-class leaves. 

In FLAML, to use defulat settings only need to create an `AutoML` instance with a few mandatory settings such as time budget, validation metric, estimator(s) and log location. By settings `n_splits` and `split_type`, in this case it's telling FLAML to run 5-fold cross validation with stratified split. As mentioned before, FLAML provides automated decision making between cross validation and holdout, but once the user has made the decision in the AutoML instance, FLAML will obey user's settings. In this example, FLAML has to run 5-fold stratified cross validation.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_flaml_default_df30.png" width="1067" height="290" />
</p>

The log file records information in each trial, therefore at the end of the optimization, we can plot its learning curve as below. As we can see, it takes less time to make an improvement in the early stage but in the later stage, it takes longer time to further enhance the performance.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/learning_curve_default_leaves30.png" width="390" height="273" />
</p>

🌻 [Look into FLAML experiment details >>][1]

To use Optuna's default settings with cross validation, users need to use its integrated CV functions, such as `LightGBMTunerCV()` function. However, not every supported model has integrated CV methods.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_optuna_default_df100.png" width="1067" height="407" />
</p>

🌻 [Look into Optuna experiment details >>][2]

Given the same 300 seconds time budget, Optuna got a little bit better testing performance, but none of their results is ideal.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/default_leaves30.png" width="658" height="223" />
</p>

It is a good practice to train the optimized model on the whole training dataset before evaluating on the testing data, in case the optimized model wasn't trained on all the cases in the training data and might show bias on testing data evaluation. Comparing the code, you may notice this step appeared in Optuna but not in FLAML, this is because FLAML will automate this step at the end of its optimization.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/flaml_train_all.png" width="766" height="79" />
</p>


#### Multi-Learners for Leaves100

Before making further improvement on Leaves30 classification, Lady H. decided to experiment on a larger dataset and try out different search strategies first. Her motivation was mainly to gain a more complete observation. The dataset, Leaves100 has 100 classes of leaves, each class has 16 records and each record has 192 features. So this is a high dimensional multi-class dataset.

🌻 [To get Leaves100 data >>][8]

FLAML has 2 main suggested search strategies, CFO and Blend Search.

* [CFO][3] is a search algorithm designed to address the large training cost variation caused by the hyperparameters. It starts from a low-cost initial point and gradually moves towards low-cost region with self-adjustable step size. At the same time, it attempts to avoid high-cost and high-loss hyperparameters. Meanwhile, the randomized restarting logic is trying to reduce the chance of getting trapped in a local optimum.

* [Blend Search][4] is a better option for a large search space. Combining the benefits of local and global search, it has an economical way to decide the exploration path. Same as CFO, Blend Search starts with a low-cost initial point, but different from CFO, it will try new starting points without waiting for the local search to be fully converged.

To use CFO or Blend Search in FLAML, users only need to specify the `hpo_method` in their settings like what you are seeing in Figure 1.4. What's more, in the settings below, it doesn't specify `estimator_list` as the experiment for Leaves30 above, so FLAML will use its default learner list which contains LGBM, XGBoost, Rnadom Foreast, Catboost, etc. This is also why the experiment here is called as "multi-learners".

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_cfo_vs_bs.png" width="900" height="700" />
</p>

🌻 [Look into FLAML experiment details >>][1]

FLAML uses CFO by default. Optuna uses TPE (Tree-structured Parzen Estimator) as its default search strategy.

TPE applies bayesian theorem `P(y|x) = P(x|y) * P(y) / P(x)`.

* `P(x|y)` means, given the objective function's score, what's the probability of the hyperparameters. When there are multiple hyperparameters, bayesian formula assumes they are independent from each other, and this is also why TPE is an independent method in Optuna.
* `P(x|y) = l(x)` if there is an improvement in the objective function, otherwise `P(x|y) = g(x)`
  * On each trial, for each parameter, TPE fits one Gaussian Mixture Model (GMM) `l(x)` to the set of parameter values associated with the best objective values, and another GMM `g(x)` to the remaining parameter values. It chooses the parameter value `x` that maximizes the ratio `l(x)/g(x)`.
* 🌻 [Learn more about TPE >>][5]

Random search is a common search algorithm implemented in many HPO tools, it selects hyperparameter sets randomly in order to find the optimal solution, and has been proved to be efficient. Since TPE and random search are the most recommended methods in Optuna, Lady H. experimented with these 2 methods. In Optuna, the search strategy is called as "sampler".

To use Optuna, even with default model settings, we need to create the objective function first, and for multi-learners scenario, we need to write the code for each learner as shown below. Because in FLAML experiments, Lady H. observed that LGBM and XGBoost appeared to be most outstanding models (set `verbose` > 0), so in Optuna, she only chose LGBM and XGBoost in the learner list.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_optuna_default_objective.png" width="1066" height="732" />
</p>

Then to select TPE or Random Search, we can specify the the sampler as shown in Figure 1.5. TPE is the default sampler, so we don't have to specify for it.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_tpe_vs_rs.png" width="800" height="800" />
</p>

🌻 [Look into Optuna experiment details >>][2]

The performance difference in Leaves100 dataset is more obvious. While achieving similar balanced accuracy in the testing data, the FLAML methods only took 10 minutes while Optuna methods took more than 1 hour, even though FLAML had more learners to try. At the same time, we can see FLAML CFO gets better testing performance than Blend Search, and this is expected since we are using default settings in this experiment, the search space is not very large. According to FLAML researchers, CFO is selected as the default search strategy is also because it works better than Blend Search in many practical cases.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/default_leaves100.png" width="790" height="349" />
</p>

Besides the difference in the overall performance, we can also see FLAML saves much more coding efforts when we just want to experiment with default settings, thanks to the automation design in FLAML. The way Optuna works gives you the flexibility to add multiple learners regardless of their implementation differences, however, FLAML also alows you to add customized learners, and we will show you that in a later experiment.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][6]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<< Looking back][7]
 



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/flaml_experiments/flaml_default.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_default.ipynb
[3]:https://github.com/microsoft/FLAML/tree/main/flaml/tune#cfo-frugal-optimization-for-cost-related-hyperparameters
[4]:https://github.com/microsoft/FLAML/tree/main/flaml/tune#blendsearch-economical-hyperparameter-optimization-with-blended-search-strategy
[5]:https://towardsdatascience.com/a-conceptual-explanation-of-bayesian-model-based-hyperparameter-optimization-for-machine-learning-b8172278050f
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_4.md
[7]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_2.md
[8]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_100leaves.ipynb
