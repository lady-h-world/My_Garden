#### Install & Execute TGANs

* <b>Install & Execute CTGAN</b>
  * `pip install ctgan` or `conda install -c pytorch -c conda-forge ctgan` to install CTGAN.
  * To generate the synthetic data only takes a few lines of code, like below:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_syn_gen_code.png" width="903" height="444" />
  
🌻 [Check detailed code >>][5] 


* <b>Install & Execute CTABGAN+</b>
  * Download CTABGAN+ repo through `git clone https://github.com/Team-TUD/CTAB-GAN-Plus.git`
  * Make sure your input real data is in "CSV" format.
  * To generate synthetic data, you can adjust [these parameters][4], output has to save in "CSV" file, and the code look as below:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+_syn_gen_code.png" width="903" height="385" />

🌻 [Check detailed code >>][3] 


* <b>Install & Execute CasTGAN</b>
  * Download CasTGAN repo through `git clone https://github.com/abedshantti/CasTGAN.git`


#### Experiments

The experiment results are summarized in table 5.1:
* Each TGAN generates synthetic training data, which shares the same number of records as the real training data.
* Every ensembling model was trained using synthetic training data and then tested on real testing data. The testing performance of the model was compared with the actual testing performance of the real data.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/syn_exp_table.png" width="930" height="441" />


[1]:https://github.com/sdv-dev/CTGAN?tab=readme-ov-file#use-the-ctgan-standalone-library
[2]:https://github.com/sdv-dev/CTGAN?tab=readme-ov-file#usage-example
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctabgan%2B.ipynb
[4]:https://github.com/Team-TUD/CTAB-GAN-Plus/blob/main/model/ctabgan.py#L17-L25
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctgan.ipynb
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_castgan.ipynb

