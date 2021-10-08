### Experiment 3 - Customized Optimization for A Regression Problem

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/miss_mooncake.png" width="255" height="320" /></p>

Hey, it's Miss Mooncake's story time!

That was a Sunday in an early Autumn, the air was filled with mixed fragant scents. Lady H. had been sitting in her office more than 1 week in order to find all the missing labels for more than 30 types of leaves... Her assistants came one after another to report garden business, and each one brought in an aromatic air to the office. Lady H. didn't notice anything unusual until the 5th girl Diana came in. "Diana! You applied perfume today!? I thought your nose was too sensitive to the scent!?". "I thought so too!", Diana replied with a big smile and shinning eyes, "But Garden Market gave us 99% discounts to buy the latest summer design, I have never seen such low price, so decided to give it a try and I love it!". "Oh, I'm glad to hear that! ... Wait a min, Garden Market is giving out perfume almost for free!? Why?". "Remeber we had harvested 3 times more summer flowers this year? Garden Market made much more perfume than they can sell and had to do a clearance sale". "I see. Hmm... we should do some sales forecasting before manufacturing".

With HPO tools at hand, this is how Lady H. decided to add this regression problem into her experiments, to forecast Garden Market's sales.

#### Baseline Forecast

Remember the Sales baseline model output [shown before][1]?

Before using the HPO power, Lady H. used default LGBM to do a baseline forecast and got 0.975 R2 score within 40.2 seconds. That's a nice result, as [mentioned before][3], the closer R2 gets towards 1 in testing data, the better.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/r2_note.png" width="766" height="79" />
</p>

🌻 [Look into Sales Baseline details >>][2]

#### FLAML Customized





[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_1.md#the-baseline-model
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/lgbm_regression_baseline.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_1.md#flaml-vs-optuna---hpo-for-classical-machine-learning

