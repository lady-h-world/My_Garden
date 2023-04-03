
## About the Data

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/garden_bank.png" width="253" height="240" />

We have a bank in the garden. For us garden residents, we make lots of money but don't spend a lot, saving it in the bank is a good choice. The bank often teaches us how to spend money and live a happy life. For example, we get monthly newsletter of tourism spots in the universe, where we can spend a great vacation and experience different culture; sometimes we get donation opportunities to help people in need from the outside world, because each time there're only 2 ~ 5 randomly selected people can donate, we all actively participate and feeling lucky if we got selected to donate 😄!
  
People from the outside of the world also save their money in our bank because of its security and attractive investment opportunities. Every month, our bank will launch a campaign to recommend some bank products to most promising customers. For example, this month the bank just launched a saving product campaign. Before launching this campaign, it will collect customers' profile to predict whether they will deposit more money, and product offers will be sent to those who got higher prediction score.
  
</p>

The data example looks as below:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/campaign_data.png" width="972" height="170" />

🌻 [To get campaign data >>][1] 

And this piece of data will be used to show the power of sprouts here as well 😉!


## Correlation

You must had been reminded many times that "correlation is not causation". People still check correlation very often, sometimes it's because a certain algorithm has made an assumption that there should be no or little correlation in the data, such as linear regression; sometimes it helps remove unnecessary features in algorithms that are robust to correlation, such as tree models; sometimes people just want to understand better the relationship between variables.

Correlation is not limited to numerical variables, it can happen between categorical variables as well, and in fact it can happen between numerical and categorical variables too. Now let's see how to check correlation in different data types.

### Correlation between Numerical Variables
#### Correlation between 2 Variables
We have 3 common methods to check the correlation between each pair of variables:
* `Pearson` is a measure of the strength and the direction of a <b>linear relationship</b> between two variables.
* `Spearman` equals to Pearson correlation between the rank values of those two variables, it assesses a <b>monotonic relationship</b>.
* `Kendall` is similar to Spearman which measures monotonic relationship using rank values of the 2 variables, but it's more robust (smaller gross error sensitivity) and more efficient (smaller asymptotic variance) than Spearman.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/ges_av.png" width="766" height="79" />
</p>

Both Speaman and Kendall uses rank values, therefore they can be applied to both continuous and ordinal variables. They are both non-parametric method and therefore the input data is not required to be in a bell curve as what Pearson assumes.

Using all the numerical variables in the data, let's look at their the correlation triangle first. In this code, you can choose one of the correlation method, also decide whether you want to show absolute correlation values or not.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_visual.png" width="823" height="260" />
</p>

The correlation triangle is in a heatmap format, so that you can find highly correlated pairs quickly based on the color. In this example, we can see, `previous` (number of contacts performed before this campaign and for this client) and `pdays` (number of days that passed by after the client was last contacted from a previous campaign) have a high spearman correlation.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_visual_out.png" width="806" height="485" />
</p>

The code below uses this correlation triangle to list out all the correlated pairs with their correlation higher than the specified threshold.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_drop.png" width="1012" height="372" />
</p>

And the output does align with the above visualization. Using the output drop list, we can remove unnecessary features from the data directly.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_drop_out.png" width="843" height="178" />
</p>

🌻 [Look into code details here >>][2] 


#### Multicollineary



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_campaign.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/correlation/correlations.ipynb
