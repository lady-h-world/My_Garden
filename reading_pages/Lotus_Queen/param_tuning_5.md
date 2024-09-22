### Experiment 3 - Customized Optimization for A Regression Problem

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/perfume.png" width="355" height="307" /></p>

It was a Sunday in early autumn, and the air was filled with a delightful mix of fragrant scents. Lady H. was enjoying afternoon tea on her balcony as her assistants arrived one by one to discuss garden matters, each bringing a fresh aroma. Everything seemed ordinary until Diana walked in.

"Diana! You’re wearing perfume today!? I thought you’d never do that!" Lady H. exclaimed, surprised, as Diana was known for her sensitive nose and rarely wore perfume. With a broad smile and eyes sparkling, Diana replied, "The Garden Market gave us a 99% discount on the latest summer fragrance. I’ve never seen prices that low, so I decided to try it—and it brings me so much joy!"

"Oh, I’m glad to hear that! ... Wait a minute, why is the Garden Market giving away perfume?" Lady H. asked, puzzled. Diana explained, "Remember how we harvested three times more summer flowers this year? The Garden Market produced far more perfume than they could sell, so they had to have a clearance sale." Lady H. thought for a moment, then said, "I see. Hmm... we should do some sales forecasting before manufacturing next time."

To forecast Garden Market's sales is a regression problem 😉.


#### Baseline Forecast

To start, Lady H. used the default LGBM to perform a baseline forecast, achieving an R2 score of 0.884 in 34.3 seconds. This is a solid result, as previously noted—the closer the R2 score is to 1 on the test data, the better.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/r2_note.png" width="766" height="79" />
</p>

🌻 [Look into Sales Baseline details >>][2]


#### FLAML Customized

In this experiment, lady H. wanted to test with not only customized learner but also customized objective function. The learner is still LGBM.

Below displays the distributions of the target (Sales) in both training and testing data. 

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/sales_distribution.png" width="911" height="324" />
</p>

The two datasets have nearly identical distributions, and the shape resembles a combination of two normal distributions, which suggests it could be modeled as a mixture of Gaussians or a Gaussian Mixture Model (GMM). Interestingly, however, Lady H. achieved better performance by using "poisson" as the objective, which assumes the target follows a [Poisson Distribution][3].

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/code_flaml_customized_poisson_loss.png" width="1064" height="809" />
</p>

Then she got 0.982 R2 testing score in 300 seconds with above settings, so there is an improvement in comparison with the baseline result.

After that, she wanted to try out her self-written objective function. But the challenge is, FLAML is using estimators' built-in config, and LGBM's customized objective function needs users to specify `grad` and `hess` 🤔

* `grad` is the value of the first order derivative (gradient) of the loss with respect to the elements of `y_pred` for each sample point.
* `hess` is the value of the second order derivative (gradient) of the loss with respect to the elements of `y_pred` for each sample point.

If you have any tip on how to calculate grad and hess well, welcome to [share it here][4], Lady H. will be more than happy to learn. But anyway, she found the formulas for some loss functions, such as "fair loss" as the code shown below.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/flaml_custimized_fair_loss.png" width="900" height="700" />
</p>

The customized objective function achieved 0.964 R2 testing score in 300 seconds, a bit lower than "poisson" objective function.

🌻 [Look into FLAML experiment details >>][5]


#### Optuna Customized

The objective function for Optuna is similar to the [previous Optuna experiment][9]. Lady H. aims to answer the question left unresolved in the earlier experiment: whether the Optuna pruner performs better without using cross-validation. As shown in the code below, users need to call `LightGBMPruningCallback()` to create the pruning callback used in LGBM:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/optuna_customized_code.png" width="765" height="634" />
</p>

🌻 [Look into Optuna experiment details >>][6]

Without applying cross validation, the overall time cost is definitely reduced, and the output is showing prunning was taking effect!

Table 1.6 summarized the performance in this experiment:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/Table1.6.png" width="654" height="303" />
</p>

Looking at all these experiments, FLAML appears to be better overall. However, it doesn't mean Optuna is worse in every aspect.

In the code, you may have noticed that Lady H. generated some visualization, which provides more insights of Optuna's hyperparameter tuning. For example,

* Parameter importance plot shows an overall view of the parameters' impact on model's validation performance:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/param_importance_optuna.png" width="1651" height="379" />
</p>

* Slice plot shows the relationship between each hyperparameter, objective value and the number of trials:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/slice_plot_optuna.png" width="1702" height="377" />
</p>

* Contour plot looks into each hyperparameter pairs:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/contour_optuna.png" width="1727" height="369" />
</p>

* Intermediate plot can interactively show you the intermediate value of each trial:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/intermediate_optuna.png" width="1664" height="368" />
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
[4]:https://github.com/lady-h-world/My_Garden/discussions/categories/open-end-discussions
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/flaml_experiments/flaml_customized_learner.ipynb
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_customized.ipynb
[7]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_6.md
[8]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_4.md
[9]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_4.md#optuna-specified-search-space
