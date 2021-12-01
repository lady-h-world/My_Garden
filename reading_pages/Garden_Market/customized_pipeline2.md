#### Task - Feature Engineering

Feature Engineering is a creative step. Besides using the existing data columns as features, users can add new features that might improve the model forecasting. The process of creating new features is called "feature engineering".

In order to create new features effectively, it's often worthy to explore the data for more insights first. Let's look at some basic methods that Lady H. often uses in her data exploration.

##### Data Exploration - Univariate Analysis

Univariate analysis is to look at the statistics of each single data column, such as checking feature distribution and target distribution. This type of analysis provides an overall view of the data. For example:

We can check the distribution of the forecasting target. From the sales plot we can see, there's some perfume sales appear to be 0, there is also a larger percentage of sales ranging between [100, 10000], and the distribution has a long tail of high value perfume sales. Starting from here, we can explore further to understand the reasons behind, which may help feature engineering.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/uni_ana_target.png" width="500" height="226" />
</p>

The distributions of categorical feature can be plotted as bar charts, so that we can see the comparison between all the values of a feature. Such as StoreType 1 occupies a much smaller population than other store types; there is less records between August and December, comparing with other months.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/uni_ana_cat_dist.png" width="1090" height="318" />
</p>

The distributions of numerical features often look like skewed normal distribution such as "Customers" distribution below, or look like skewed normal distribution with bumps such as "CompetitionDistance" distribution below. It is also common to see a very long tail in these distributions, and we can try out binning the feature values, so that a numerical feature will be converted to a categorical feature.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/binning.png" width="766" height="79" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/uni_ana_num_dist.png" width="1084" height="267" />
</p>

🌻 [Check data exploration details >>][1]


##### Data Exploration - Bivariate Analysis

Bivariate analysis often looks into the relationship between 2 variables, such as the relationship between 2 features or the relationship between a feature and the target. During the feature enginerring stage, Lady H. often checks feature vs target distribution first. Because if a feature's values can better differentiate different values of the target, then this feature tend to improve the forecast.

For example, from the univariate analysis above, we are seeing the distribution of "Customers" is showing a large bump before 3000 and a long tail after 3000, then what does the sales distributions look like for "Customers < 3000" and "Customers >= 3000"? The answer is shown below, and there is an obvious sales difference between these 2 groups. When the number of customers are larger than 3000, there is higher sales. Therefore, we can create a new feature that simply divides feature "Customers" into 2 bins, "Customers < 3000" and "Customers >= 3000".

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/bin_ana_cat_dist.png" width="1084" height="254" />
</p>

We can also look at sales distributions for categorical features, such as the sales of StoreType 1 appears to be more different from other store types, so that we can create a new feature to indicate whether the StoreType is 1 or not; the sales distribution of each year looks quite similar, indicating feature "Year" may not be an important feature.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/bin_ana_num_dist.png" width="982" height="594" />
</p>

🌻 [For more insights, check the full data exploration details >>][1]


##### Feature Engineering Pipeline Code

In the pipeline, we start with specifying functions that can create new features through `feature_adding_dct` in the config file. Then in the feature engineering task, it will call every specified function from the helpers file.

In this example, Lady H. was adding 2 functions:

* `add_date_feature()` is to add Year, Month, Quarter as new features, they were all generated from the "date" column. Although "Year" may not be a good feature as we saw in above bivariate analysis, it is common to generate these time elements as new features when we have a date column.
* `add_threshold_grouping_features()` is to generate a binary feature based on specified thereshold. In this case, "Customers" has been used to generate feature "Customers_larger_then_3000" to indicate whether the customers amount is larger than 3000.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/feature_engineering_code.png" width="1233" height="859" />
</p>

🌻 [Check feature engineering config >>][2]

🌻 [Check feature engineering task >>][3]

🌻 [Check feature engineering helpers >>][4]


You might have noticed this `requires()` function in feature engineering task. It builds the dependency between tasks. Because feature engineering can only be executed after finishing data collection task, and `requires()` function indicates this relationship, so that luigi will know the order of tasks.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/feature_engineering_dependent.png" width="301" height="62" />
</p>


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][5]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][6]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/data_exploration_sales.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml#L29
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/feature_engineering.py
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/helpers/feature_engineering_helpers.py
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline3.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline1.md
