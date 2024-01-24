### Generate Tabular Synthetic Data

#### About the Data

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/safe_bank.png" width="216" height="202" />
  
If you have already visited [Resplendent Tree][2], you must be familiar with our Garden Bank and its [deposit campaign data][1].

Our Garden Bank is famous for its safety, attracting significant investments and deposits from the outside world. To safeguard customers' data, we employed a strategy to confuse hackers by interspersing real and fake data locations. Each genuine data piece has multiple look-alike fake data pieces stored in various locations, making it challenging for hackers to pinpoint the actual location of each set of real data.

Synthetic data generation is one of the solutions to make this strategy come true!
</p>

This dataset has:
* 11,162 records
* 7 numerical variables
* 9 categorical variables
* The target is a binary value, indicating has deposit or not
* The target has 52.6% negative records and 47.4% positive records

The experiments you're going to see are using deposit campaign data again. Let's take look at the snapshot of the real data and the generated synthetic data:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/real_vs_syn.png" width="931" height="441" />

🌻 [To get campaign data >>][3] 


#### Evaluation Metrics

To evaluate the effectiveness of generated synthetic data, Lady H. employed 2 methods.

<b>The first</b> evaluation method was to compare variables' distributions between real data and synthetic data. PSI score was used to compare continuous variable's distributions and JS Distance was used to compare discrete variable's distributions.

PSI often employees these thresholds:
* `PSI < 0.1`: no significant distribution change
* `0.1 <= PSI < 0.2`: moderate distribution change
* `PSI >= 0.2`: significant distribution change

So, if we can find more variables have PSI score lower than 0.2 or even lower than 0.1, then the generated synthetic data is closer to the real data.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/continuous_dist_comp.png" width="996" height="525" />

JS Distance (or JS Divergence) can be used to compare discrete variable's distributions, it's a score between `[0, 1]`, "0" corresponds to identical distributions and "1" to absolutely different. Lady H. was using "0.1" as the threshold, if more variables got JS Distance lower than 0.1, then the generated synthetic data is closer to the real data.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/discrete_dist_comp.png" width="908" height="503" />

<b>The second</b> evaluation method was to apply a machine learning model on two training datasets, one came from the real data and the other came from the synthetic data, then compare their performance on the same testing data formed by real data. The smaller performance difference indicates a higher similarity between the real and the synthetic.

🌻 [See example code >>][4] 

Lady H. used the second evaluation method in most experiments after she found it is more effective in comparing the real data and the synthetic data.

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