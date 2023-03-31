
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

You must had been reminded many times that "correlation is not causation". People still check correlation very often, sometimes it's because a certain algorithm has made an assumption that there should be no or little correlation in the data, such as linear regression; sometimes it helps remove unnecessary features in algorithms that are robust to correlation, such as tree models; sometimes people just want to observe the relationship between variables.

Correlation is not limited within numerical variables, it can happen between categorical variables as well, and in fact it can happen between numerical and categorical variables too. Now you will see how to check correlation in each category.

### Correlation between Numerical Variables
#### Correlation between 2 Variables
We have 3 common methods to check the correlation between each pair of variables:
* `Pearson` is a measure of the strength and the direction of a <b>linear relationship</b> between two variables.
* `Spearman` is equal to the Pearson correlation between the rank values of those two variables, it assesses a <b>monotonic relationship</b>.
* `Kendall` is similar to Spearman which measures monotonic relationship using rank values of the 2 variables, but it's <b>more robust</b> than Spearman.

Both Speaman and Kendall uses rank values, which means they can be applied to both continuous and ordinal variables. They are both non-parametric method and therefore data doesn't need to be in a bell curve as whta Pearson assumes.


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_campaign.ipynb
