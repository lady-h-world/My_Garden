## Association
Exploring relationships between variables is crucial when building machine learning models. It deepens our understanding of the data, helps validate model assumptions (e.g., the independence assumption in linear regression), and supports the removal of unnecessary variables to improve model efficiency.

Association is a common technique for examining data relationships. It applies to numerical, categorical, and mixed variable types, revealing how these variables interact or vary together.


### About the Data
<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/garden_bank.png" width="253" height="240" />

Our garden bank is renowned for its exceptional management of customers' funds. Many customers from the outside world 
chose to save their money here, attracted by the bank's reputation for security and appealing investment opportunities.
  
Each month, our bank develops engaging investment offers and sends advertisements to potential customers likely to be interested. This process of sending advertisements is referred to as a <b>campaign</b>.

The data presented here comes from one such campaign, which aimed to promote a term deposit product. This product requires customers to maintain their funds in the bank for several years, during which they earn interest.

In the campaign data, the label `deposit` indicates whether a customer has acquired this term deposit product.
  
</p>

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
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/ges_av.png" width="777" height="89" />
</p>

Both Spearman and Kendall uses rank values, therefore they can be applied to both continuous and ordinal variables. They are both non-parametric method and therefore the input data is not required to be in a bell curve as what Pearson assumes.

Using all the numerical variables in our campaign data, let's look at the correlation triangle first. In the code below, you can choose one of the correlation methods through `corr_method`, also decide whether you want to show absolute correlation values through `abs_corr`.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_visual.png" width="823" height="260" />
</p>

The correlation triangle is displayed as a heatmap, allowing you to quickly identify highly correlated pairs by color. In this example, we observe a strong Spearman correlation between `previous` (the number of contacts made with each client before this campaign) and `pdays` (the number of days since the client was last contacted).

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_visual_out.png" width="806" height="485" />
</p>

The code below utilizes this correlation triangle to list all pairs with correlations exceeding the specified threshold.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_drop.png" width="1012" height="372" />
</p>

The output aligns with the visualization above. By using the output drop list, we can directly remove unnecessary features from the data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/corr_drop_out_v3.png" 
width="859" height="188" />
</p>

🌻 [Look into code details here >>][2] 


#### Multicollineary

Sometimes, we can't find correlation between every 2 variable pairs, but it exists in a combo of more than 2 variables. This type of "correlation" is multicollineary. 

VIF (Variance Inflation Factor) is often used to measure multicollineary. It provides an index that measures how much the variance of an estimated regression coefficient is increased because of collinearity.

Typically, a VIF score above 10 indicates high multicollinearity, suggesting that variables with VIFs exceeding this threshold can be removed. The code below creates a dataframe of VIF scores for each numerical variable in the dataset.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/multi_corr_code.png" width="948" height="244" />
</p>

In the example below, the threshold is set to 5. Calculating the VIF for each variable can sometimes take a while, so saving the output vif_df as a file can save significant time if you plan to test different VIF thresholds.

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
