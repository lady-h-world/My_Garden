# Machine Learning Pipeline

In recent years, industries and research groups are developing machine learning pipelines that can handle most of the work (from data collection to model evaluation) automatically. This end-to-end pipeline is often called as "AutoML".

<p align="center">🌱 <b>Sprouts Collection Time!</b> 🌱</p>

Similar to the 2 types of perfume pipelines in the garden market, the sprouts' super power is to create machine learning pipeline.
* Mini Pipeline - It takes a specific data input each time, and mainly hadles model selection, which is to select the best model for the data. Some of such pipelines also inlcude data preprocessing, feature engineering and hyperparameter optimization.
  * The sprouts will show you how to use <b>TPOT, AutoKeras and MLJar</b>.
* Customized Pipeline - This type of pipeline can be constructed to handle more clients' data and add more complex functionalities.
  * The sprouts will show you how to build a <b>luigi pipeline</b> that includes data collection, data preprocessing, feature engineering, model selection, model evaluation and data drifting monitoing. You will also see a super mini pipeline built using <b>Airflow</b> and <b>ZenML</b>.

## Mini Pipelines
* [TPOT][1] is an AutoML pipeline that uses genetic algorithm to select the best pipeline for the data.
* [AutoKeras][2] builds the optimal neural network model for the data input, it does parameter tuning and model selection using Keras Tuner.
* [MLJar][3] selects the best model from classical machine learning models and neural network models. Besides, it also generates detailed reports and visualization for each model.

Lady H. tested the power of these sprouts with the same data sets used in [hyperparameter optimization (HPO) experiments][6]. The test results are summarized in Table 4.1, as we can see, not only there is a comparison between TPOT, AutoKeras and MLJar, but also a comparison with the best HPO performance.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/hpo_comparison.png" width="766" height="79" />
</p>

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tb4.1.png" width="929" height="403" />
</p>

* 🌻 [To get Leaves30 data >>][7]
* 🌻 [To get Sales data >>][8]

When using these mini pipelines, it is expected to take longer execution time than HPO, since there are more models and parameters to be selected. Then based on the results in Table 4.1, MLJar appears to be a better model selection tool. To dive into more details, let's follow the Chansey Butterflies!

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]
 


[1]:https://github.com/EpistasisLab/tpot
[2]:https://github.com/keras-team/autokeras
[3]:https://github.com/mljar/mljar-supervised
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline2.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/garden_market.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_1.md#flaml-vs-optuna---hpo-for-classical-machine-learning
[7]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_leaf.ipynb
[8]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_sales.ipynb
