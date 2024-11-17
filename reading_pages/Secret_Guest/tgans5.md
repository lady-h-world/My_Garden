### Generate Tabular Synthetic Data

#### About the Data

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/safe_bank.png" width="216" height="202" />
  
If you have already visited [Resplendent Tree][2], you must have heard of our Garden Bank.

Our Garden Bank is renowned for its robust security, which has attracted substantial investments and deposits from clients cosmos-wide. To protect our customers' sensitive data, we employ an innovative strategy that confounds hackers by blending real and decoy data locations. For every genuine piece of data, we create multiple look-alike decoys stored in different locations, making it exceedingly difficult for hackers to identify the true data sources.

One of the key technologies driving this strategy is synthetic data generation, which allows us to seamlessly create these decoys and enhance our security measures!
</p>

The deposit campaign data has:
* 11,162 records
* 7 numerical variables
* 9 categorical variables
* The target is a binary value, indicating has deposit or not
* The target has 52.6% negative records and 47.4% positive records

🌻 [To get campaign data >>][3] 

Let's take look at the snapshot of the real data and the generated synthetic data:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/real_vs_syn.png" width="931" height="441" />


#### Evaluation Metrics
Lady H. used two methods to assess the effectiveness of the generated synthetic data.

<b>The first method</b> involved comparing the distributions of variables between the real data and the synthetic data. For continuous variables, the PSI (Population Stability Index) score was used, while JS (Jensen-Shannon) Distance was employed for comparing the distributions of discrete variables.

PSI often employees these thresholds:
* `PSI < 0.1`: no significant distribution change
* `0.1 <= PSI < 0.2`: moderate distribution change
* `PSI >= 0.2`: significant distribution change

Therefore, if more variables have a PSI score below 0.2, or even below 0.1, it indicates that the generated synthetic data closely resembles the real data.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/continuous_dist_comp.png" width="996" height="525" />

JS Distance can be used to compare the distributions of discrete variables, yielding a score between 0 and 1, where 0 indicates identical distributions and 1 indicates completely different ones. Lady H. set a threshold of 0.1, if more variables have a JS Distance below 0.1, it suggests that the generated synthetic data closely matches the real data.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/discrete_dist_comp.png" width="908" height="503" />

<b>The second</b> evaluation method was to apply a machine learning model on two training datasets, one came from the real data and the other came from the synthetic data, then compare their performance on the same testing data formed by real data. The smaller performance difference indicates a higher similarity between the real and the synthetic.

🌻 [See example code >>][4] 

Lady H. used the second evaluation method in most experiments after she found it is more effective in making the comparison.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][5]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][6]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/corr1.md#about-the-data
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/about_resplendent_tree.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_campaign.ipynb
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/syn_ctgan.ipynb
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans6.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans4.md