### Experiment 3 - Customized Optimization for A Regression Problem

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/perfume.png" width="355" height="307" /></p>

It was a Sunday in early autumn, and the air was infused with a blend of fragrant scents. Lady H. was enjoying afternoon tea on her balcony. Her assistants arrived one by one to report on garden business, each bringing with them a delightful aroma. Lady H. didn't notice anything unusual until Diana walked in.

"Diana! You're wearing perfume today!? I thought you would never do that!" Diana, known for her sensitive nose and rare use of perfume, replied with a big smile and shining eyes, "The Garden Market offered us a 99% discount on the latest summer design. I've never seen such a low price, so I decided to give it a try, and I love it!"

"Oh, I'm glad to hear that! ... Wait a minute, Garden Market is giving away perfume? Why?" Diana explained, "Remember, we harvested three times more summer flowers this year? Garden Market produced much more perfume than they could sell and had to have a clearance sale." Lady H. pondered, "I see. Hmm... we should conduct some sales forecasting before manufacturing."

To forecast Garden Market's sales is a regression problem.


#### Baseline Forecast

Before using the HPO power, Lady H. used default LGBM to do a baseline forecast and got 0.884 R2 score in 34.3 seconds. That's a decent result, as mentioned before, the closer R2 gets towards 1 in testing data, the better.

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

After that, she wanted to try out her self-written objective function. But the challenge is, FLAML is using estimators' built-in config, and LGBM's customized objective function needs users to specify `grad` and `hess` 🤔

* `grad` is the value of the first order derivative (gradient) of the loss with respect to the elements of `y_pred` for each sample point.
* `hess` is the value of the second order derivative (gradient) of the loss with respect to the elements of `y_pred` for each sample point.

If you have any tips on how to calculate grad and hess well, welcome to [show and tell us][4], Lady H. will be more than happy to know that. But anyway, she found the formulas for some loss functions, such as "fair loss" as the code shown below. LGBM does have its built-in fair loss too, but here Lady H. changed the constant value used in the formula.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/flaml_custimized_fair_loss.png" width="900" height="700" />
</p>

Not to her surprise, the final performance in testing data wasn't better than using poisson loss. 0.964 R2 testing score in 300 seconds, even worse than the baseline output.

🌻 [Look into FLAML experiment details >>][5]

#### Optuna Customized

Same as FLAML, here we use LGBM as the learner, therefore the way to customize the objective function will be the same, Lady H. didn't plan to add customized objective function in this experiment. Instead, she wanted to address the question left from the previous Optuna experiment, about whether Optuna pruner works better without using cross validation. As the code shown below, users need to call `LightGBMPruningCallback()` to create the pruning callback used in LGBM:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/optuna_customized_code.png" width="765" height="634" />
</p>

🌻 [Look into Optuna experiment details >>][6]

Without applying cross validation, the overall time cost is definitely reduced, and the output is showing prunning was taking effect, but the testing performance is still worse than the baseline result.

Table 1.6 summarized the performance in this experiment:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/Table1.6.png" width="654" height="303" />
</p>

Looking at all these experiments, FLAML appears to be better overall. However, it doesn't mean Optuna is worse in every aspect.

In the code, you may have noticed that Lady H. generated some visualization, which provides more insights of Optuna's hyperparameter tuning. For example,

* Parameter importance plot shows an overall view of the parameters' impact on model's validation performance.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/param_importance_optuna.png" width="1651" height="379" />
</p>

* Slice plot shows the relationship between each hyperparameter, objective value and the number of trials.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/slice_plot_optuna.png" width="1702" height="377" />
</p>

* Contour plot looks into each hyperparameter pairs.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/contour_optuna.png" width="1727" height="369" />
</p>

* Intermediate plot can interactively show you the intermediate value of each trial.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/intermediate_optuna.png" width="1664" height="368" />
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
[4]:https://github.com/lady-h-world/My_Garden/discussions/categories/show-and-tell
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/flaml_experiments/flaml_customized_learner.ipynb
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_customized.ipynb
[7]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/The%20Queen/param_tuning_6.md
[8]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/The%20Queen/param_tuning_4.md
