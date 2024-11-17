#### Setup Environment

* [Follow this guidance][15] to create a virtual environment, it can simplify python packages' installation and their version control.
* The required python version is <b>Python 3.9</b>.
* [Follow this guidance][18] to set up required python packages.
  * [required requirements.txt][16]
  * [required setup.sh][17] 
* If there will be any package version problem, you can check the full list of python packages [here][19].


#### Install & Execute TGANs

* <b>Install & Execute CTGAN</b>
  * CTGAN was included in `requirements.txt` and has been installed during environment setup step.
  * To generate the synthetic data only takes a few lines of code, and you can adjust [these parameters][14]. See example code below:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_syn_gen_code.png" width="903" height="444" />
  
🌻 [Check detailed code here >>][5] 


* <b>Install & Execute CTABGAN+</b>
  * CTABGAN+ wasn't included in `requirements.txt` because it needs manually installation, and it doesn't have a version.
  * Download CTABGAN+ repo by typing `git clone https://github.com/Team-TUD/CTAB-GAN-Plus.git` through your terminal.
  * Make sure your input real data is in "CSV" format.
  * To generate synthetic data, you can adjust [these parameters][4], output has to save as a "CSV" file, and the code looks as below:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+_syn_gen_code.png" width="903" height="385" />

🌻 [Check detailed code here >>][3] 


* <b>Install & Execute CasTGAN</b>
  * CasTGAN wasn't included in `requirements.txt` because it needs manually installation, and it doesn't have a version. 
  * Download CasTGAN repo by typing `git clone https://github.com/abedshantti/CasTGAN.git` in your terminal.
  * Edit the code in CasTGAN repo by adding your dataset name in [this list][8]. Lady H. added "campaign" in this list.
  * [Edit this code file to update seeds for your dataset][9]. Lady H. updated seeds for dataset "campaign".
  * Generate the data input as below:
    * Split the real data into training and testing data.
    * Save the real training data in CasTGAN's `Data/` folder, naming it as "{your_dataset_name}_train.csv".
    * Save the real testing data in CasTGAN's `Test_Data/` folder, naming it as "{your_dataset_name}_test.csv".
    * Save features' data type in `Data/` folder, making sure categorical features are using `str` as data type.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/castgan_data_input.png" width="528" height="277" />
  
  * Through your terminal, locate `CasTGAN/` folder.
  * Run `python -m main --dataset="campaign" --epochs=10`, replace "dataset" with your dataset's name.
  * Besides `epochs` you can specify other parameters in above command, [check CastGAN parameters][10] for more.

🌻 [Check detailed code here >>][13] 


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
[13]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_castgan.ipynb
[14]:https://github.com/sdv-dev/CTGAN/blob/main/ctgan/synthesizers/ctgan.py#L107-L144
[15]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Rainbow_Moss/virtual_env/virtual_env1.md#how-to-create-python-virtual-environments
[16]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/requirements.txt
[17]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/setup.sh
[18]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Rainbow_Moss/virtual_env/virtual_env1.md#how-to-install-requirements
[19]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/full_requirements_bk.txt