The performance of FLAML and Optuna in Table 1.1 came from their best experiment results. In order to give you a better view of the power of our seeds, we'd like to take you around to see the internal mechanism, as well as each experiment's details.

### Design Overview - FLAML

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

<b>Step 0 - Resampling Strategy</b>: It's a simple thresholding rule to choose between cross validation or holdout. According to FLAML researchers, cross validation is preferred over holdout for small sample size or large time budget.
* "Time Budget" means the total amount of time the user allows FLAML to run HPO.

<b>Step 1 - Learner Proposer</b>: A learner gets a higher priority if it makes improvement with less estimated cost. Meanwhile, every learner has a chance to be searched again since the estimation can be impresise.

<b>Step 2 - Hyperparam & Sample Size Proposer</b>: In this step, each learner chooses between increasing the sample size or trying out a new parameter set in order to make the improvement. By default, each new parameter set is searched by a randomized direct search strategy, CFO. We will show you more about it soon.

<b>Step 3 - Controller</b>: The controller will invoke the trial using the selected learner and observe both validation error as well as GPU time cost of the trial.

Step 1 ~ 3 are repeated by iterations until running out of the time budget.

🌻 [Learn more about FLAML >>][1]


### Design Overview - Optuna

The overall design of Optuna is shown in Figure 1.3:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/optuna_design.png" width="678" height="424" />
</p>



[1]:https://www.microsoft.com/en-us/research/publication/flaml-a-fast-and-lightweight-automl-library/
