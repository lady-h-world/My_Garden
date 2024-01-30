#### Experiments

The experiment results are summarized in table 5.1. To do the experiments,
* Each TGAN generates "synthetic" training data, which shares the same number of records as the "real" training data.
* Every ensembling model was trained using "synthetic" training data and subsequently tested on the "real" testing data. Its performance was then compared with that of the model trained on the "real" training data.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/syn_exp_table.png" width="930" height="441" />

With each TGAN, Lady H. tried different settings and used the best performed synthetic dataset to summarize table 5.1. 

* To generate the synthetic data:
  * CTGAN used 17 minutes
  * CTABGAN+ used 28.8 minutes
  * CasTGAN used 15 minutes

When comparing datasets' LGBM performance, CasTGAN outperformed. However, both AUC and AVP values were relatively low, falling below 0.6. Considering CTABGAN+ took longer data generation time and got lowest LGBM performance, Lady H. later focused the comparison solely between CTGAN and CasTGAN in subsequent experiments. CasTGAN continued to outperform XGBoost and CatBoost in terms of performance, while the performance consistently to be low. Lady H. applied Stacking as well, by stacking the optimized LGBM, XGBoost and CatBoost, only got worse performance.

* 🌻 [Check CTGAN data generation & LGBM baseline code >>][1] 
* 🌻 [Check CTABGAN+ data generation & LGBM baseline code >>][2] 
* 🌻 [Check CasTGAN+ data generation & LGBM baseline code >>][3] 
* 🌻 [Check optimizaed LGBM code >>][4]
* 🌻 [Check optimized XGBoost code >>][6] 
* 🌻 [Check optimized CatBoost code >>][7] 
* 🌻 [Check Stacking code >>][5] 

Finally, Lady H. got both AUC and AVP above 0.6 by employing "ASDGP Method". How does this method work? 😉


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][8]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][9]

[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctgan.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctabgan%2B.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_castgan.ipynb
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/hpo_lgbm.ipynb
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/stacking_vecstack.ipynb
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/hpo_xgboost.ipynb
[7]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/hpo_catboost.ipynb
[8]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans8.md
[9]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans6.md