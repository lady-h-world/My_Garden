### MLJar

Similar to other AutoML pipelines, MLJar also includes data preprocessing, hypterparameter tuning and model selection, as well as model evaluation. What makes MLJar special is its detailed visualization output and the way it selects algorithms.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/mljar_process.png" width="823" height="424" />
</p>

#### MLJar Visualization Output

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

MLJar generates SHAP dependent plot for each feature. The example below came from "4_Default_LightGBM_Stacked", where predicted results from formerly trained models became the features, this is why you are seeing features like "Ensemble_prediction", "Decision_Tree_prediction", etc.

The way SHAP dependent plot works is:

* Red color means higher (or more positive) prediction value
* Blue color means lower (or more negative) prediction value

When a feature is showing positve correlation with its SHAP value, this feature tend to be more important, such as feature Ensemble_prediction and feature 4_Default_LightGBM_prediction shown below.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/mljar_shap_dependent.png" width="1000" height="500" />
</p>


