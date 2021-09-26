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


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_leaf.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_sales.ipynb
