## Association

When building machine learning models, exploring the relationships between variables is crucial. It enhances our 
understanding of the data, helps meet model assumptions (e.g. linear regression assumes variables are independent), 
and aids in removing unnecessary variables in order to improve model efficiency.

Association is a popular method for exploring data relationships. It appears between numerical variables, 
categorical variables, and mixed types of variables, revealing how these variables move together.


### About the Data

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/garden_bank.png" width="253" height="240" />

We have a garden bank known for its excellent management of customers' money. Many customers from the outside world 
chose to save their money here, drawn by the bank's reputation for security and its attractive investment opportunities.
  
Every month, the bank creates interesting investment opportunities and sends advertisements to potential customers 
who are likely to be interested. Such ads-sending event is called as a <b>campaign</b>.

The data used here came from one of these campaigns, aimed at selling a term deposit product. This product requires 
customers to keep their money in the bank for several years, during which they earn interest.
  
</p>

The campaign data example looks as below, `deposit` is the label, indicating whether a customer had acquired this 
term deposit product.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/campaign_data.png" width="972" height="170" />

🌻 [The code to get campaign data >>][1] 


### Association between Numerical Variables

#### Correlation between 2 Numerical Variables

Correlation is a type of association often applied between two numerical variables. It measures the strength and direction of the relationship between the two variables.
* Strength: How closely the variables are related. Strong correlation means the variables move together closely.
* Direction: Whether the relationship is positive (both variables increase together) or negative (one variable increases as the other decreases).

We have 3 common methods to check the correlation between each pair of variables:
* `Pearson` is a measure of the strength and the direction of a <b>linear relationship</b> between two variables.
* `Spearman` equals to, Pearson correlation using rank values of those two variables, it assesses a <b>monotonic 
  relationship</b>.
* `Kendall` is similar to Spearman which measures monotonic relationship using rank values of the 2 variables, but it's more robust (smaller gross error sensitivity) and more efficient (smaller asymptotic variance) than Spearman.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/ges_av.png" width="766" height="79" />
</p>

Both Spearman and Kendall uses rank values, therefore they can be applied to both continuous and ordinal variables. They are both non-parametric method and therefore the input data is not required to be in a bell curve as what Pearson assumes.

Using all the numerical variables in our campaign data, let's look at the correlation triangle first. In the code below, you can choose one of the correlation methods, also decide whether you want to show absolute correlation values or not.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_visual.png" width="823" height="260" />
</p>

The correlation triangle is in a heatmap format, so that you can find highly correlated pairs quickly based on the color. In this example, we can see, `previous` (number of contacts performed for this client before this campaign) and `pdays` (number of days that passed after the client was contacted last time) have a high spearman correlation.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_visual_out.png" width="806" height="485" />
</p>

The code below uses this correlation triangle to list out all the correlated pairs with their correlation higher than the specified threshold.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_drop.png" width="1012" height="372" />
</p>

And the output does align with the above visualization. Using the output drop list, we can remove unnecessary features from the data directly.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_drop_out_v3.png" 
width="859" height="188" />
</p>

🌻 [Look into code details here >>][2] 


#### Multicollineary

Sometimes, we can't find correlation between every 2 variable pairs, but it exists in a combo of more than 2 variables. This type of "correlation" is multicollineary. 

VIF (Variance Inflation Factor) is often used to measure multicollineary. It provides an index that measures how much the variance (the square of the estimate's standard deviation) of an estimated regression coefficient is increased because of collinearity.

The code below generates a dataframe of VIF score for each numerical variable in the data. Normally when VIF score is higher than 10, there's high multicollineary, and you can drop the variables with VIF above the threshold.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/multi_corr_code.png" width="948" height="244" />
</p>

In the example below, the threshold is set as 5. Sometimes, it takes a long time to generate VIF of each variable, so save the output `vif_df` as a file will save you lots of time if you want to try different thresholds.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/multi_corr_out.png" width="625" height="393" />
</p>

🌻 [Look into code details here >>][2] 

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][4]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_campaign.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/var_relationships/association.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/rel2.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/about_resplendent_tree.md
