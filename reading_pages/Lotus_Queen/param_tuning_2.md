### Design Overview - FLAML

The overall design of FLAML is shown in Figure 1.2:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/FLAML_design.png" width="732" height="414" />
</p>

It has 2 major components:
* <b>ML Layer</b> contains the candidate learners, such as XGBoost, LightGBM, etc.
* <b>AutoML Layer</b> includes a Resampling Strategy Proposer, a Learner Proposer, a Hyperparam & Sample Size Proposer and a Controller. This layer controls the core logic of the search strategy, with the goal of minimizing the total cost before finding a model with the optimal test error.
  * "Total Cost" means the total CPU time of training and validation using cross validation or holdout. This cost is also expected to increase as the test error decreases.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/search_strategy.png" width="866" height="89" />
</p>

Now let's look into each step:

<b>Step 1 - Resampling Strategy</b>: It's a simple thresholding rule to choose between cross validation or holdout. According to FLAML researchers, cross validation is preferred over holdout for small sample size or large time budget.
* "Time Budget" means the total amount of time the user allows FLAML to run HPO.

<b>Step 2 - Learner Proposer</b>: A learner gets a higher priority if it makes improvement with less estimated cost. Meanwhile, every learner has a chance to be searched again since the estimation can be impresise.

<b>Step 3 - Hyperparam & Sample Size Proposer</b>: In this step, each learner chooses between increasing the sample size or trying out a new parameter set in order to make the improvement. By default, each new parameter set is searched by a randomized direct search strategy, CFO. You will see details soon.

<b>Step 4 - Controller</b>: The controller will invoke the parameter tuning trials using the selected learner and observe both validation error as well as CPU time cost of each trial.

Step 2 ~ 4 are repeated by iterations until running out of the time budget.

🌻 [Learn more from FLAML paper >>][1]


### Design Overview - Optuna

The overall design of Optuna is shown as Figure 1.3:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/optuna_design.png" width="678" height="424" />
</p>

Optuna introduced define-by-run framework into HPO in 2019. The main idea behind define-by-run is, a user can rely on Optuna to decide the hyperparamster values in each trial dynamically (when the program is running), without explicitly define everything in advance. There are different ways to dynamically construct the parameter search space, Optuna's is based on historical evaluated trials' results. Meanwhile, Optuna provides highly modularized programming that a user-defined objective function receives a living trial as input and evaluates the trial result, which also enables the parallel computation of multiple trials.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/trial_and_study.png" width="766" height="79" />
</p>

Optuna's sampling algorithm works as its search strategy, supporting both independent sampling (such as TPE) and relational sampling (such as CMA-ES). Independent sampling samples hyperparameters independently while relational sampling exploits the correlations between hyperparaemters. To achieve cost-effectiveness, Optuna also provides pruning algorithm to terminate unpromising trials based on periodically monitored intermediate objective values.

As we can see in Figure 1.3, each Optuna worker executes an instance of the objective function as well as sampling algorithm and pruning algorithm of a study. This type of design is suitable for distributed environment where workers are running in parallel. Furthermore, workers are sharing the progress of current study via the storage. An objective function can access the storage to get the information of past studies.

🌻 [Learn more from Optuna paper >>][4]

Hyperopt is another popular tool for hyperparameter tuning, but Lady H. prefers to use Optuna and didn't include it in the experiments.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/why_not_hyperopt.png" width="766" height="79" />
</p>


### Design Overview - Summary

Table 1.2 has compared and summarized the design of FLAML and Optuna:

While sharing several common strengths, FLAML is designed to be more automated in optimization. The main differences in their core algorithms are, FLAML makes decisions based on the estimated evaluation while Optuna is based on the historical evaluation, and FLAML's time complexity seems more efficient.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/flaml_vs_optuna_design_diff.png" width="901" height="663" />
</p>

Now time to show you Lady H.'s experiments with FLAML and Optuna!

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][2]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]
 



[1]:https://www.microsoft.com/en-us/research/publication/flaml-a-fast-and-lightweight-automl-library/
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_3.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_1.md
[4]:https://arxiv.org/abs/1907.10902
