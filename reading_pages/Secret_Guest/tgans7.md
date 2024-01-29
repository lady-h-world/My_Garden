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

If we compare synthetic data's prediction performance with real data's, using their best LGBM performance, CasTGAN's synthetic data was the winner, but both AUC and AVP are low performance, lower than 0.6. Considering CTABGAN+ took longer data generation time and got lowest performance, in later experiments, Lady H. only compared between CTGAN and CasTGAN



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctgan.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctabgan%2B.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_castgan.ipynb