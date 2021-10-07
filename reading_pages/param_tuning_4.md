### Experiment 2 - Optimization with Specified Search Space

After experimenting on the defualt settings, time to make the improvement, and a straightforward way is to specify a better search space, meaning, to suggest a better value range for hyperparameters. In this experiment, Lady H. was focusing on Leaves30 dataset.

#### FLAML Specified Search Space

To specify the search space in FLAML, no matter whether the model is in FLAML's default estimator list, users need to create a new class with specified hyperparameters. For example, Lady H. wanted to adjust the hyperparameters of LGBM, and she had to create a new learner class like this:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_flaml_search_space.png" width="1068" height="477" />
</p>

To specify a good search space, different estimators have different tips. Hyperparameters can be adjusted for better accuracy, or for faster speed, or for reducing overfitting, etc. 

🌻 [Check LGBM tips for search space specification >>][1]

After creating the new learner class, users just need to add it in the `estimator_list` and in the AutoML instance:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_flaml_add_learner.png" width="700" height="286" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/estimator_learner_model.png" width="766" height="79" />
</p>

🌻 [Look into FLAML experiment details >>][2]

In the code, you will also see, Lady H. had tried CFO and Blend Search again with larger search space, but neither work well. Lessons learned, `larger search space != better search sapce`


#### Optuna Specified Search Space

In Optuna, Lady H. made the same search space specification in a new objective function. Meanwhile, in order to apply cross validation as FLAML experiment, `LightGBMTunerCV()` was used here:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_optuna_search_space_no_pruner.png" width="824" height="685" />
</p>

The experiment above took much longer running time than FLAML, therefore, Lady H. was wondering whether she should add pruning to skip those unpromising trials in order to save time. Also because the testing performance from above Optuna experiment didn't look well, Lady H. added more trials to see whether there can be some performance improvement. TPE is still used as the search strategy in these Optuna experiments, and [hyperband is a suggested pruner to be used together with TPE][3], in order to achieve a better performance result.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_optuna_search_sapce_has_prunder.png" width="824" height="685" />
</p>

🌻 [Look into Optuna experiments details >>][4]

In these experiments, FLAML and Optuna share the same specified search space. However, comparing with their default settings, FLAML made 11.87% improvement in testing performance without increasing time cost, while Optuna made 8% decrease in the testing performance and had its time cost increased 3 times.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/flaml_optuna_search_space.png" width="655" height="306" />
</p>

Looking into Optuna's experiment code, you may have noticed that the time cost increased 9 times when the number of trials increased 9 times. However, this won't happen in FLAML, because FLAML's time complexity is affected by the number of hyperparameters rather than the number of trials.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/flaml_time_complexity.png" width="766" height="79" />
</p>

The output of Optuna experiments didn't show prunning had happened at all. This made Lady H. wonder, this was because Optuna's pruner doesn't work well with cross validation? And how to make optuna's pruner work? She decided to test more in the next experiment.



[1]:https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/flaml_experiments/flaml_specified_search_space.ipynb
[3]:https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html#which-sampler-and-pruner-should-be-used
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_specified_search_space_integratedCV.ipynb
