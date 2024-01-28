#### Install & Execute TGANs

* <b>Install & Execute CTGAN</b>
  * `pip install ctgan` or `conda install -c pytorch -c conda-forge ctgan` to install CTGAN.
  * To generate the synthetic data only takes a few lines of code, like below:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_syn_gen_code.png" width="903" height="444" />
  
🌻 [Check detailed code here >>][5] 


* <b>Install & Execute CTABGAN+</b>
  * Download CTABGAN+ repo by typing `git clone https://github.com/Team-TUD/CTAB-GAN-Plus.git` in your terminal.
  * Make sure your input real data is in "CSV" format.
  * To generate synthetic data, you can adjust [these parameters][4], output has to save in "CSV" file, and the code looks as below:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+_syn_gen_code.png" width="903" height="385" />

🌻 [Check detailed code here >>][3] 


* <b>Install & Execute CasTGAN</b>
  * Download CasTGAN repo by typing `git clone https://github.com/abedshantti/CasTGAN.git` in your terminal.
  * Make sure you have installed [required libraries][7].
  * Edit the code in CasTGAN repo by adding your dataset name in [this list][8]. Lady H. added "campaign" in this list.
  * [Edit this code file to update seeds for your dataset][9]. Lady H. updated seeds for dataset "campaign".
  * Generate the data input as below:
    * Split the real data into training and testing data.
    * Save the real training data in `Data/` folder, naming it as "{your_dataset_name}_train.csv".
    * Save the real testing data in `Test_Data/` folder, naming it as "{your_dataset_name}_test.csv".
    * Save features' data type in `Data/` folder, making sure categorical features are using `str` as data type.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/castgan_data_input.png" width="528" height="277" />
  
  * Through your terminal, `cd` to the cloned `CasTGAN/` folder.
  * Run `python -m main --dataset="campaign" --epochs=10`, replace "dataset" with your dataset's name.
  * Besides `epochs` you can specify other parameters in above command, [check CastGAN parameters][10] for more.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][11]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][12]


[1]:https://github.com/sdv-dev/CTGAN?tab=readme-ov-file#use-the-ctgan-standalone-library
[2]:https://github.com/sdv-dev/CTGAN?tab=readme-ov-file#usage-example
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctabgan%2B.ipynb
[4]:https://github.com/Team-TUD/CTAB-GAN-Plus/blob/main/model/ctabgan.py#L17-L25
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctgan.ipynb
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_castgan.ipynb
[7]:https://github.com/abedshantti/castgan#system-requirements
[8]:https://github.com/abedshantti/CasTGAN/blob/main/main.py#L19-L31
[9]:https://github.com/abedshantti/CasTGAN/blob/main/main.py#L206-L257
[10]:https://github.com/abedshantti/CasTGAN/blob/main/Model/CasTGAN.py#L380-L413
[11]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans7.md
[12]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans5.md

