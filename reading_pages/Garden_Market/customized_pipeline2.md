#### Task - Feature Engineering

Feature Engineering is a creative step. Besides using the existing data columns as features, users can add new features that might improve the model forecasting. The process of creating new features is called "feature engineering".

In order to create new features effectively, it's often worthy to explore the data for more insights first. Let's look at some basic methods Lady H. often uses in her data exploration.

##### Data Exploration - Univariate Analysis

Univariate analysis is to look at the statistics of each single data column, such as checking feature distribution and target distribution. This type of analysis provides an overall view of the data. For example,

We can check the distribution of the forecasting target. From the sales plot we can see, there's some perfume sales appear to be 0, there is also a larger percentage of sales ranging between [100, 10000], and the distribution has a long tail of high value perfume sales. Starting from here, we can explore further to understand the reasons behind, which may help feature engineering.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/uni_ana_target.png" width="500" height="226" />
</p>

The distributions of categorical feature can be plotted as bar charts, so that we can see the comparison between all the values of a feature. Such as StoreType 1 occupies a much smaller population than other store types; there is less records between August and December, comparing with other months.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/uni_ana_cat_dist.png" width="1090" height="318" />
</p>

The distributions of numerical features often look like skewed normal distribution such as Customers distribution below, or look like skewed normal distribution with bumps such as CompetitionDistance distribution below. It is also common to see a very long tail in these distributions, and we can try out binning the feature values, so that a numerical feature will be converted to a categorical feature.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/binning.png" width="766" height="79" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/uni_ana_num_dist.png" width="1084" height="267" />
</p>


🌻 [Check data exploration details >>][1]




[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/data_exploration_sales.ipynb
