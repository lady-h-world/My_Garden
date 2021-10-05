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

To use Optuna default settings with cross validation, users need to use its integrated CV functions, such as `LightGBMTunerCV()` function. However, not every supported model has integrated CV methods. Using `LightGBMTunerCV()` here, the mandatory settings are almost the same as FLAML's settings above, the time budget is 300 seconds too.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_optuna_default_df100.png" width="1067" height="407" />
</p>

Given the same time budget, Optuna got a little bit better testing performance, but none of their results is ideal.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/default_leaves30.png" width="658" height="223" />
</p>

* 🌻 [To look into FLAML experiment details >>][1]
* 🌻 [To look into Optuna experiment details >>][2]

#### LGBM for Leaves100

Before making further improvement on Leaves30 classification, Lady H. decided to experiment on a larger dataset and try out different search strategies first. Her motivation was mainly to gain a more complete observation. The dataset, Leaves100 has 100 classes of leaves, each class has 16 records and each record has 192 features. So this is a high dimensional multi-class dataset.



<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/default_leaves100.png" width="790" height="349" />
</p>


* 🌻 [To look into FLAML experiment details >>][1]
* 🌻 [To look into Optuna experiment details >>][2]



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/flaml_experiments/flaml_default.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_default.ipynb
