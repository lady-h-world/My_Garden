### Experiment 3 - Customized Optimization for A Regression Problem

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/miss_mooncake.png" width="255" height="320" /></p>

Hey, it's Miss Mooncake's story time!

That was a Sunday in an early Autumn, the air was filled with mixed fragant scents. Lady H. had been sitting in her lab more than 1 week in order to find all the missing labels for 30-ish types of leaves... Her assistants came one after another to report garden business, and each one brought in an aromatic air to the room. Lady H. didn't notice anything unusual until the 5th girl Diana came in. "Diana! You're wearing perfume today!? I thought your nose was too sensitive to the scent!?". "I thought so too!", Diana replied with a big smile and shinning eyes, "But Garden Market gave us 99% discounts to buy the latest summer design, I have never seen such low price, so decided to give it a try and I love it!". "Oh, I'm glad to hear that! ... Wait a min, Garden Market is giving out perfume almost for free!? Why?". "Remeber we had harvested 3 times more summer flowers this year? Garden Market made much more perfume than they can sell and had to do a clearance sale". "I see. Hmm... we should do some sales forecasting before manufacturing".

With HPO tools at hand, this is how Lady H. decided to add this regression problem into her experiments, to forecast Garden Market's sales.

#### Baseline Forecast

Remember the Sales baseline model output shown before?

Before using the HPO power, Lady H. used default LGBM to do a baseline forecast and got 0.975 R2 score within 40.2 seconds. That's a nice result, as mentioned before, the closer R2 gets towards 1 in testing data, the better.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/r2_note.png" width="766" height="79" />
</p>

🌻 [Look into Sales Baseline details >>][2]

#### FLAML Customized

In this experiment, lady H. wanted to test with not only customized learner but also customized objective function. The learner is still LGBM.

She did some basic data exploration, such as checking the distributions of the forecast target (Sales) in both training and testing data. 

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/sales_distribution.png" width="911" height="324" />
</p>

The 2 datasets have almost the same distributions, and the shape looks like the combination of 2 [poisson distributions][3]. In LGBM's built-in objective funtions, there is a "poisson loss" which assumes the forecast target follows poisson distribution, when the likelihood of the assumption is larger, the forecast performance can be better.

Therefore, Lady H. started with LGBM's built-in poisson loss. Because the customized learner inherited from `LGBMEstimator`, users can simply specify the `objective` as "poisson":

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_flaml_customized_poisson_loss.png" width="1064" height="809" />
</p>

Lady H. got 0.982 R2 testing score in 300 seconds with these settings, so there is an improvement in comparison with the baseline result.

After that, she wanted to try out her self-written objective function. But the challenge is, LGBM's customized objective function needs users to specify `grad` and `hess` 🤔

* `grad` is the value of the first order derivative (gradient) of the loss with respect to the elements of `y_pred` for each sample point.
* `hess` is the value of the first order derivative (gradient) of the loss with respect to the elements of `y_pred` for each sample point.

Lady H. had graduated from high school for a while and forgot how to do the calculation. If you have any good suggestion, welcome to leave comments in [the discussion forum][4], Lady H. will be more than happy to know that. But anyway, she found the formulas for some loss functions, such as "fair loss" as the code shown below. LGBM does have its built-in fair loss too, but here Lady H. changed the constant value used in the formula.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/flaml_custimized_fair_loss.png" width="900" height="700" />
</p>

Not to her surprise, the final performance in testing data wasn't better than using poisson loss. 0.964 R2 testing score in 300 seconds, even worse than the baseline output.

🌻 [Look into FLAML experiment details >>][5]

#### Optuna Customized

Because the learner is LGBM too and the way to customize the objective function will be the same, Lady H. didn't plan to add customized objective function in this experiment. Instead, she wanted to address the question left from the previous Optuna experiment, about whether Optuna pruner works better without using cross validation. As the code shown below, users need to call `LightGBMPruningCallback()` to create the pruning callback used in LGBM:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/optuna_customized.png" width="1066" height="635" />
</p>

🌻 [Look into Optuna experiment details >>][6]

Without applying cross validation, the overall time cost is definitely reduced, and the output is showing prunning was taking effect, but the testing performance is still worse than the baseline result.

Table 1.6 summarized the performance in this experiment:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/flaml_vs_optuna_customized.png" width="654" height="304" />
</p>

Looking at all these experiments, FLAML appears to be better overall. However, it doesn't mean Optuna is worse in every aspect.

In the code of Optuna experiment, you may have noticed that Lady H. generated some visualization, which provides more insights of Optuna's hyperparameter tuning. For example,

* Parameter importance plot shows an overall view of the parameters' impact on model's validation performance.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/optuna_param_importance.PNG" width="900" height="435" />
</p>

* Slice plot shows the relationship between each hyperparameter, objective value and the number of trials.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/optuna_slice.PNG" width="1484" height="382" />
</p>

* Contour plot looks into each hyperparameter pairs.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/optuna_contour.PNG" width="1476" height="378" />
</p>

* Intermediate plot can interactively show you the intermediate value of each trial.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/optuna_intermediate.PNG" width="1478" height="373" />
</p>

Comparing with FLAML, Optuna has a better user experience in deep learning, and in the next experiment, we will bring you to the experiment of deep learning HPO!

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][7]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<< Looking back][8]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_1.md#the-baseline-model
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/lgbm_regression_baseline.ipynb
[3]:https://en.wikipedia.org/wiki/Poisson_distribution
[4]:https://github.com/lady-h-world/My_Garden/discussions
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/flaml_experiments/flaml_customized_learner.ipynb
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_customized.ipynb
[7]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_6.md
[8]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_4.md
