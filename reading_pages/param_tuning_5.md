### Experiment 3 - Customized Optimization for A Regression Problem

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/miss_mooncake.png" width="255" height="320" /></p>

Hey, it's Miss Mooncake's story time!

That was a Sunday in an early Autumn, the air was filled with mixed fragant scents. Lady H. had been sitting in her lab more than 1 week in order to find all the missing labels for 30-ish types of leaves... Her assistants came one after another to report garden business, and each one brought in an aromatic air to the room. Lady H. didn't notice anything unusual until the 5th girl Diana came in. "Diana! You're wearing perfume today!? I thought your nose was too sensitive to the scent!?". "I thought so too!", Diana replied with a big smile and shinning eyes, "But Garden Market gave us 99% discounts to buy the latest summer design, I have never seen such low price, so decided to give it a try and I love it!". "Oh, I'm glad to hear that! ... Wait a min, Garden Market is giving out perfume almost for free!? Why?". "Remeber we had harvested 3 times more summer flowers this year? Garden Market made much more perfume than they can sell and had to do a clearance sale". "I see. Hmm... we should do some sales forecasting before manufacturing".

With HPO tools at hand, this is how Lady H. decided to add this regression problem into her experiments, to forecast Garden Market's sales.

#### Baseline Forecast

Remember the Sales baseline model output [shown before][1]?

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

The 2 datasets have almost the same distributions, and the distribution looks like the combination of 2 [poisson distributions][3]. In LGBM's built-in objective funtions, there is a "poisson loss" which assumes the forecast target follows poisson distribution, when the likelihood of the assumption is larger, the forecast performance can be better.

Therefore, Lady H. started with LGBM's built-in poisson loss. Because the customized learner inherited from `LGBMEstimator`, users can simply specify the `objective` as "poisson":

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/code_flaml_customized_poisson_loss.png" width="1064" height="809" />
</p>

Lady H. got 0.982 R2 score within 300 seconds with these settings, so there is an improvement from the baseline result.

After that, she wanted to try out her self-written objective function. But the challenge is, LGBM's customized objective function needs users to specify `grad` and `hess` 🤔

* `grad` is the value of the first order derivative (gradient) of the loss with respect to the elements of `y_pred` for each sample point.
* `hess` is the value of the first order derivative (gradient) of the loss with respect to the elements of `y_pred` for each sample point.

Lady H. had graduated from high school for a while and forgot how to do the calculation. If you have any good suggestion, welcome to contact us at ladyheartsworld@gmail.com, Lady H. will be more than glad to know that.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/flaml_custimized_fair_loss.png" width="900" height="700" />
</p>






[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_1.md#the-baseline-model
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/lgbm_regression_baseline.ipynb
[3]:https://en.wikipedia.org/wiki/Poisson_distribution
