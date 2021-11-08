# Machine Learning Pipeline

In recent years, industries and research groups are developing machine learning pipelines that can handle most for the work automatically, from data collection to model evaluation. This end-to-end pipeline is often called as "AutoML".

<p align="center">🌱 <b>Sprouts Collection Time!</b> 🌱</p>

Similar to the 2 types of perfume pipelines in the garden market, the sprouts also has the power of producing 2 types of machine learning pipeline:
* Mini Pipeline - It takes a specific data input each time, and mainly hadles model selection, which is to select the best model for the data. Some of such pipelines also inlcude data preprocessing, feature engineering and hyperparameter optimization.
  * The sprouts will show you how to use <b>TPOT, AutoKeras and MLJar</b>.
* Customized Pipeline - This type of pipeline can be constructed to handle more clients' data and add more complex functionalities.
  * The sprouts will show you how to build a <b>luigi pipeline</b> that includes data collection, data preprocessing, feature engineering, model selection, model evaluation and data drifting monitoing. You will also see a super mini pipeline of how to use <b>airflow</b>.

## Mini Pipelines
* [TPOT][1] is an AutoML pipeline that uses genetic aalgorithm to select the best pipeline for the data.
* [AutoKeras][2] selects the best neural network model for the data input, it does parameter tuning and model selection using Keras Tuner.
* [MLJar][3] selects the best model from classical machine learning models and neural network, it also generates detailed report and visualization for each model.

Figure 4.1 shows a brief comparison when applied them to regression data and classification data.



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
