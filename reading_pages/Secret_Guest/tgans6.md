#### Install & Execute TGANs

* <b>Install & Execute CTGAN</b>
  * `pip install` or `conda install` [like this][1] will install CTGAN easily.
  * To generate the synthetic data only takes a few lines of code, [like this][2].
* <b>Install & Execute CTABGAN+</b>


#### Experiments

The experiment results are summarized in table 5.1:
* Each TGAN generates synthetic training data, which shares the same number of records as the real training data.
* Every ensembling model was trained using synthetic training data and then tested on real testing data. The testing performance of the model was compared with the actual testing performance of the real data.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/syn_exp_table.png" width="930" height="441" />


[1]:https://github.com/sdv-dev/CTGAN?tab=readme-ov-file#use-the-ctgan-standalone-library
[2]:https://github.com/sdv-dev/CTGAN?tab=readme-ov-file#usage-example
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctabgan%2B.ipynb

