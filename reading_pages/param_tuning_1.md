# Hyperparameter Optimization (HPO)

In order to be able to bloom in winter, the Queen had optimized her genes in the past hundreds of years. When the cold weather comes, her body parameters can be adjusted to the best status.

Similar to the Queen, in Applied Data Science, we can adjust the hyperparameters of a model in order to get an optimal output, this process is known as “Hyperparameter Optimization” (HPO).

<p align="center">🌱 <b>Seeds Collection Time!</b> 🌱</p>

The seeds in this stop has the power of appliying the latest HPO technology in classical classification & regression as well as deep learning problems, using FLAML, Optuna and Keras Tuner.
<p>&nbsp;</p>

## FLAML vs Optuna - HPO for Classical Machine learning

Optuna is a hyperparameter optimization framework published in 2019, it was designed for improving cost effectiveness of HPO with efficient parameter searching strategy and pruning algorithm. Till 2021, it has become a mature tool that supports different frameworks of machine learning and deep learning.

FLAML is an automated HPO library published in 2021, powered by self-invented parameter searching algorithms, it aims at freeing users from selecting learners and hyperparameters while delivering fast and economical HPO results.

While working on some garden business, Lady H. has experimented with these powerful seeds. Let's look at a comparison between FLAML and Optuna through her experiments:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/The_Queen_images/flaml_vs_optuna.png" width="922" height="409" />
</p>

* Leaves30 has 14 features and 340 records in total, with 30 different specimens to classify, it is a typical multi-class classification dataset. 
  * 🌻 [To get Leaves30 data >>][1]
* Sales data has 18 features and 693861 records in total, it is used to forecast sales, a regression problem. 
  * 🌻 [To get Sales data >>][2]

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/market_crystal.png" width="766" height="79" />
</p>

In the classification problem, Lady H. was using [balanced accuracy][3] to measure the percentage of correctly predicted specimens in the testing data, with its value closer to 1, the better model performance we get. In the regression problem, [R2 (r-square)][4] was used to measure how close the forecasted sales to the real sales, with its value closer to 1, the better model performance we get.

We have summarized Lady H.'s notes in Table 1.1, by comparing the baseline model vs FLAML vs Optuna, we can see FLAML has an overall better performance in both classification and regression. Now let’s look into details.


### The Baseline Model
The baseline model provides a bottomline performance. In Lady H.'s experiments, she was using LightGBM (LGBM) with default settings. 

LGBM is an ensembling model that is widely used in the industry and data science competitions, it has been proved to be an excellent estimator in both model performance and computation efficiency. 

Another benefit of choosing LGBM is the saved efforts in data preprocessing:
* Numerical features in different scales are not required to be scaled. Because, as a type of tree model, LGBM is not sensitive to the variance in features.
* LGBM handles missing values automatically by allocating them to wherever reduces the loss most. 
* LGBM offers good accuracy with integer-coded categorical features. It is safe to label encoding categorical features without worrying about the order in the data as numerical features. Users only need to convert the integer-coded categorical features as “category” data type in python pandas.
* LGBM is a non-parametric method which doesn’t make assumptions on the data, so preprocessing methods such as data normalization or reducing data correlation are not required either.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Next page >>][1]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_1.md


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_leaf.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_sales.ipynb
[3]:https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html
[4]:https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score
