# 💝 Gift for You 💝

We think a summarized note will give you a better visiting experience :)

### Optuna

#### Pros
* Flexible modularized design
* Supports both classicial machine learning and deep learning, easy to learn
* Design-by-run strategy saves users' efforts to specify all the hyperparameter values
* Self-adjustment based on historical trials
* Support [multi-objective optimization][1]
* Visualization plots optimization insights

#### Cons
* Comparing with FLAML, Keras Tuner, it appears to be less efficient
* Pruner seems doesn't work well with cross validation
* Not all the estimators are well integrated, such as XGBoost
* Errors hard to debug.
  * For example, it can be risky to set `log=True` in `trial.suggest_int()` for parameters like `num_leaves`, `max_depth`, `max_bin`, you may get confusing errors
  
### FLAML

#### Pros
* Automation and design-by-run strategy saves lots of user efforts while being promising in getting descent results


#### Cons


### Keras Tuner

#### Pros

#### Cons



[1]:https://optuna.readthedocs.io/en/v2.7.0/tutorial/20_recipes/002_multi_objective.html
