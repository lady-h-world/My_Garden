### MLJar

Similar to other AutoML pipelines, MLJar also includes data preprocessing, hypterparameter tuning and model selection, as well as model evaluation. What makes MLJar special is its detailed visualization output and the way it selects algorithms.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/mljar_process.png" width="823" height="424" />
</p>

#### MLJar Visualization Output

MLJar does some basic EDA (Exploratory Data Analysis) by showing the distribution of features and the target. But it is not recommended to use count in the distribution, since sometimes you need to compare the same feature from different data samples, the count may not be able to tell the real difference in percentages.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/mljar_eda.png" width="800" height="246" />
</p>

Leaderboard summarizes the training time and performance of each model.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/mljar_leaderboard.png" width="700" height="400" />
</p>

* MLJar "Ensemble" uses greedy approach to create weighted ensemble from already trained ML models.
* MLJar "Stacked" uses stacking. In stacking, there are multiple stages of base model forecasting, in each stage, there is k-fold cross validation, the predicted values from each fold will be appended together as a new feature for the next stage. When there are m base models in a stage, there will be m new features generated for the next stage.
  * In this example, the base model is default LightGBM.
* MLJar "Ensemble_Stacked" will ensemble all the previous stacked and unstacked models.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/stack_ensemble.png" width="766" height="79" />
</p>


