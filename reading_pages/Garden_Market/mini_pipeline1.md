# Machine Learning Pipeline

In recent years, industries and research groups are developing machine learning pipelines that can automatically handle most of the work, from data collection to model evaluation. This end-to-end pipeline is commonly referred to as "AutoML".

Machine learning pipelines can be categorized in two ways, much like our perfume lines:
* <b>Prebuilt Pipeline</b> - It requires specific data inputs for each run and primarily focuses on model selection, aiming to choose the best model for the given data. Some of these pipelines also incorporate data preprocessing, feature engineering, and hyperparameter optimization. You will find experiments involving <b>TPOT, AutoKeras and MLJar</b>.
* <b>Customized Pipeline</b> - This type of pipeline can be constructed to handle more clients' data and add more complex functionalities.
  * <b>Luigi</b> enables the construction of pipelines that can include data collection, preprocessing, feature engineering, model selection, evaluation, and data drift monitoring, or any other step in your machine learning development process.
  * You will also see simple pipelines built using <b>Airflow</b> and <b>ZenML</b>.


## Prebuilt Pipelines

Let's look at prebuilt pipelines first!

* [TPOT][1] is an AutoML pipeline that uses genetic algorithm to select the best pipeline for the data.
* [AutoKeras][2] builds the optimal neural network model for the data, it does parameter tuning and model selection using Keras Tuner.
* [MLJar][3] selects the best model from classical machine learning models and neural network models. Besides, it also generates detailed reports and visualization for each model.

The experiments utilized the same datasets as those in the [hyperparameter optimization (HPO) experiments][6]. The evaluation results, summarized in Table 4.1, compare the performance of TPOT, AutoKeras, and MLJar, as well as their results against the best HPO performance.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/hpo_comparison.png" width="766" height="79" />
</p>

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tb4.1.png" width="929" height="403" />
</p>

* 🌻 [To get Leaves30 data >>][7]
* 🌻 [To get Sales data >>][8]

When using these prebuilt pipelines, the execution time is expected to be longer than that of HPO, as more models and parameters need to be selected. For a deeper exploration, let's follow the Chansey Butterflies!

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
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_1.md#flaml-vs-optuna---hpo-for-classical-machine-learning
[7]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_leaf.ipynb
[8]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_sales.ipynb
