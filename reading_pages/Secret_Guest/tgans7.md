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

When comparing model LGBM's prediction performance of synthetic data with real data, CasTGAN outperformed. However, both the AUC and AVP values were relatively low, falling below 0.6. Considering CTABGAN+ took longer data generation time and got lowest performance, Lady H. later focused the comparison solely between CTGAN and CasTGAN in subsequent experiments. CasTGAN still outperformed in XGBoost, CatBoost comparisons and maintained a low performance. Lady H. applied Stacking as well, by stacking the optimized LGBM, XGBoost and CatBoost, only got worse performance.

🌻 [Check CTGAN data generation & LGBM baseline code >>][1] 
🌻 [Check CTABGAN+ data generation & LGBM baseline code >>][2] 
🌻 [Check CasTGAN+ data generation & LGBM baseline code >>][3] 
🌻 [Check optimizaed LGBM code >>][4] 
🌻 [Check Stacking code >>][5] 
🌻 [Check optimized XGBoost code >>][6] 
🌻 [Check optimized CatBoost code >>][7] 

[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctgan.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctabgan%2B.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_castgan.ipynb
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/hpo_lgbm.ipynb
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/stacking_vecstack.ipynb
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/hpo_xgboost.ipynb
[7]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/hpo_catboost.ipynb