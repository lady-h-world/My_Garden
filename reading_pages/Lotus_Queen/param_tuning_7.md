# 💝 A Gift for You 💝

The experiments here represent just the tip of the iceberg, as different hyperparameter optimization (HPO) tools can perform differently across various datasets. Let's summarize the pros & cons of these tools.


### Optuna

#### Pros
* Has flexible modularized design
* Supports both classicial machine learning and deep learning, easy to learn
* Supports [multi-objective optimization][1]
* Provides optimization insights in visuals

#### Cons
* Comparing with FLAML, Keras Tuner, it appears to be less efficient
* Incomplete integration, such as XGBoost integration, pruning in cross validation, etc.
* Confusing errors, such as setting `log=True` in use `trial.suggest_int()` for parameters like `num_leaves`, `max_depth`, `max_bin` may get confusing errors
  

### FLAML

#### Pros
* Has automation intelligence, nice choice for fast prototyping
* Has simple but intelligent search strategy
* Has efficient time complexity, not affected by the number of trials
* [FLAML research team responses to users' questions fast][2] 💯

#### Cons
* Hard to use for deep learning HPO
* Incomplete documentation, such as available parameter values, deep learning HPO, etc.
* Challenging to customize the Objective function


### Keras Tuner

#### Pros
* Has great documentation, also supports keywords search
* Has efficient search strategy
* Has flexible modularized design
* Easy to learn and use

#### Cons

<i>Haven't found yet, if you know any weakness, feel free to [share it here][5]!</i>

<p>&nbsp</p>


### A Surprise!

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/surprise.png" width="265" height="248" /></p>

Lady H. was very happy to get a notice when FLAML published their latest release, they listed her as one of the contributors just because she was asking questions which pushed the team to make further improvements :)

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/flaml_my_name.png" width="578" height="848" />
</p>


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Garden Map >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<< Looking back][3]
 


[1]:https://optuna.readthedocs.io/en/v2.7.0/tutorial/20_recipes/002_multi_objective.html
[2]:https://github.com/microsoft/FLAML/discussions
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_6.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/tour_guide.md#garden-map
[5]:https://github.com/lady-h-world/My_Garden/discussions/categories/open-end-discussions