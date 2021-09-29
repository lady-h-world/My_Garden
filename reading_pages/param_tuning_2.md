The performance of FLAML and Optuna in Table 1.1 came from their best experiment results. In order to give you a better view of the power of our seeds, we'd like to take you around to see the internal mechanism, as well as each experiment's details.

### Design Overview

#### FLAML

The overall design of FLAML is shown in Figure 1.2:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/FLAML_design.png" width="732" height="414" />
</p>

It has 2 major components:
* ML Layer contains the candidate learners.
* AutoML Layer includes a Resampling Strategy Proposer, a Learner Proposer, a Hyperparam & Sample Size Proposer and a Controller. This component controls the core logic of search strategy, with the goal of minimizing the total cost before finding a model with the lowest test error.
  * "Total Cost" means the total GPU time of training and validation using cross validation or holdout. This cost is also expected to increase as the test error decreases.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/search_strategy.png" width="866" height="89" />
</p>

Now let's look into each step:

<b>Step 0 - Resampling Strategy</b>: It's a simple thresholding rule to choose between cross validation or holdout. 

If the training data has less than 100K instances and `# instances * # features / time budget` is less than 10M/hour, then use cross validation, otherwise use holdout.
* The reason behind is, cross validation is preferred over holdout for small sample size or large time budget.
* "Time Budget" means the total amount of time the user allows FLAML to run HPO.


### Experiment 1 - Optimization with Default LGBM
