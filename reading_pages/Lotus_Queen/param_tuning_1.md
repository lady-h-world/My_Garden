# Hyperparameter Optimization (HPO)

To thrive in winter, Lotus Queen had optimized her genes over centuries, allowing her body to adapt perfectly to the cold weather. Similarly, in Applied Data Science, we can fine-tune a model's hyperparameters to achieve the best performance. This process is known as "Hyperparameter Optimization" (HPO).

In this chapter, we will apply the latest HPO technology in classical classification & regression as well as deep learning problems, using FLAML, Optuna and Keras Tuner.
<p>&nbsp;</p>


## FLAML vs Optuna - HPO for Classical Machine learning

[Optuna][7] is a hyperparameter optimization framework published in 2019, it was designed for improving cost effectiveness of HPO with efficient parameter searching strategy and pruning algorithm. Till 2024, it has become a mature tool that supports different frameworks of machine learning and deep learning.

[FLAML][6] is an automated HPO library published in 2021, powered by self-invented parameter searching algorithms, it aims at freeing users from selecting learners and hyperparameters while delivering fast and economical HPO results.

While working on some garden businesses, Lady H. has experimented with these tools. Let's look at a comparison between FLAML and Optuna through her experiments:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/Table1.1.png" width="917" height="406" />
</p>

* Leaves30 has 14 features and 340 records in total, with 30 different specimens to classify, it is a typical multi-class classification dataset. 
  * 🌻 [To get Leaves30 data >>][1]
* Sales data has 18 features and 693861 records in total, it is used to forecast sales, a regression problem. 
  * 🌻 [To get Sales data >>][2]

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/market_crystal.png" width="766" height="79" />
</p>

In the classification problem, Lady H. was using [balanced accuracy][3] to measure the percentage of correctly predicted specimens in the testing data, with its value closer to 1, the better model performance we get. In the regression problem, [R2 (r-square)][4] was used to measure how close the forecasted sales to the real sales, with its value closer to 1, the better model performance we get. Meanwhile, the computational efficiency is an important metrics too.

We have summarized Lady H.'s notes in Table 1.1, by comparing the baseline model vs FLAML vs Optuna, we can see FLAML has an overall better performance in both classification and regression. Now let’s look into details.


### The Baseline Model
The baseline model provides a bottomline performance. In Lady H.'s experiments, she was using LightGBM (LGBM) with default settings. 

LGBM is an ensembling model that is widely used in the industry and data science competitions, it has been proved to be an excellent estimator in both model performance and computation efficiency. 

Another benefit of choosing LGBM is the saved efforts in data preprocessing:
* Numerical features in different scales are not required to be scaled. Because, as a type of tree model, LGBM is not sensitive to the variance in features.
* LGBM handles missing values automatically by allocating them to wherever reduces the loss most. 
* LGBM offers good accuracy with integer-coded categorical features. It is safe to label encoding categorical features without worrying about the order in the data as numerical features. Users only need to convert the integer-coded categorical features as “category” data type in python pandas.
* LGBM is a non-parametric method which doesn’t make assumptions on the data, so preprocessing methods such as data normalization or reducing data correlation are not required either.

The baseline performance is the average balanced accuracy of cross validation (CV) results. By using cross validation, we can observe the performance of each fold as well as the performance variance among folds. Because of the variance, we average all folds' results as the final performance, in order to show a less biased view.

Leaves30 has small amount of data, so using 5-fold CV here:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/baesline_classification.png" width="1000" height="800" />
</p>

🌻 [Look into Leaves30 Baseline details >>][9]

Sales data is large enough to use 10-fold CV:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/reg_sales_baseline_code.png" width="1077" height="782" />
</p>

🌻 [Look into Sales Baseline details >>][10]

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][5]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][8]
 



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_leaf.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_sales.ipynb
[3]:https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html
[4]:https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_2.md
[6]:https://github.com/microsoft/FLAML
[7]:https://optuna.org/
[8]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/the_queen.md
[9]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/lgbm_baseline.ipynb
[10]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/lgbm_regression_baseline.ipynb
