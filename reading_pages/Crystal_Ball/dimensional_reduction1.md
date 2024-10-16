## Dimensional Reduction

When we try to visualize the data, each column is considered as a dimension. For example, data ploted on x-axis and y-axis is 2 dimensional data, and data ploted on x-axis, y-axis and z-axis is 3 dimensional data.

To plot the data into cartesian coordinate (x, y coordinate system) is a straightforward way to understand the data. However, for data with more than 3 dimensions, such plot is challenging. With crystal ball's power, Lady H. can project higher dimensional data into lower dimensions while keeping the original information as much as possible. This power is called as "Dimensional Reduction".


### About the Data

The data input used here is our Garden Bank's campaign data, [described here][2].
Before dimensional reduction, we need to do some data preprocessing first:
1. Categorical features need to be coverted into numerical values, so that dimensional reduction algorithms can consume them. A common practice is through "encoding", such as one-hot encoding. Lady H. often uses [Target Encoding][3], this method sometimes helps improve model performance, because when converting the categorical values into numerical, it considers both prior knowledge of the target over all the training data and the posterior knowledge of the target given each categorical value. See this encoding results below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/cat2num.png" width="859" height="440" />
</p>

2. Next is to standardize all the numerical features into the same scale, so that features with wider ranges won't dominate the distance metric. This step is necessary before using most of the dimensional reduction algorithms, because they measure euclidean distances.

🌻 [Check data preprocessing code here >>][1]


### PCA 

PCA (Principal Component Analysis) is a popular dimensional reduction method. It outputs several principle components, PC1, PC2, ..., PCn. 

Consider each principal component as a line in the cartesian coordinate system. The objective is to minimize the distances from the data points to their projections on this line, so that the spread of data projections on this line is maximized, leading to the maximization of data variance in this dimension. PC1 captures the highest proportion of data variance, followed by PC2, which captures the highest proportion of the remaining variance. This pattern continues with all subsequent principal components (PCx). This allows PCA to capture the maximum amount of variance in each dimension, sequentially reducing overall information loss.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/about_pca.png" width="1000" height="500" />

Dimensional reduction is not only used to project data into lower dimensional plots, but also can be used to reduce the number of features used in other machine learning models, especially in cases when models suffer from the curse of dimensionality. Therefore, dimensional reduction sometimes can improve model performance.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/benefits_of_lossing_variance.png" width="766" height="79" />

To fit PCA in python, the number of principle components `n_components` can't be larger than the number of features in the data. There're 16 features in the data. The code below is trying to fit PCA and output 16 principle components.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/fit_plot_pca.png" width="609" height="506" />

The generated principle components and their explained variance look as below:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/pca16.png" width="914" height="460" />

Then if you choose `x` for `n_components` within its limit (16 in this case), PCA will keep the same variance for all the 16 principle components but output the top x ones. For example, if we set `n_components = 3`, the output 3 principle components have the save variance as the top 3 ones plotted above.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/pca3_code.png" width="391" height="84" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/pca3.png" width="546" height="396" />

If we plot the top 3 principle components in 3D space, and color the 2 classes in label "deposit", it looks as below:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_pca.png" width="643" height="368" />

🌻 [Check PCA code here >>][1]

Can we find a dimensional reduction method that can differentiate the 2 classes better in 3D space? Or the data can't be differentiate well in a 3D space? Let's explore more!

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Back to Crystal Power][5]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/magic_dimensional_reduction.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/rel1.md#about-the-data
[3]:https://contrib.scikit-learn.org/category_encoders/targetencoder.html
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction2.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/crystal_power.md
