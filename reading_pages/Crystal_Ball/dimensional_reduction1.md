## Dimensional Reduction
When visualizing data, each column represents a dimension. For instance, data plotted on the x-axis and y-axis is considered 2-dimensional, while data plotted on the x, y, and z axes is 3-dimensional.

Plotting data on a Cartesian coordinate system (x, y) is a simple and intuitive way to understand it. However, visualizing data with more than 3 dimensions becomes challenging. Thanks to the power of the Crystal Ball, Lady H. can project higher-dimensional data into lower dimensions while preserving as much of the original information as possible. This ability is known as "Dimensional Reduction".


### About the Data
The data input used here is our Garden Bank's [campaign data][2]. Before dimensional reduction, we need to do some data preprocessing first:
1. Categorical features need to be coverted into numerical values, so that dimensional reduction algorithms can consume them. A common practice is through "encoding", such as one-hot encoding. Lady H. often uses [Target Encoding][3], a technique that can sometimes enhance model performance. This method converts categorical values into numerical ones by incorporating both the prior knowledge of the target across all training data and the posterior knowledge of the target given each specific categorical value. See the results of this encoding below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/cat2num.png" width="859" height="440" />
</p>

2. The next step is to standardize all numerical features to the same scale, ensuring that features with larger ranges do not dominate the distance metrics. This step is crucial before applying most dimensional reduction algorithms, as they rely on Euclidean distances.

🌻 [Check data preprocessing code here >>][1]


### PCA 

PCA (Principal Component Analysis) is a popular dimensional reduction method. It outputs several principle components, PC1, PC2, ..., PCn. 

Each principal component can be thought of as a line in the Cartesian coordinate system. The objective is to minimize the distances between the data points and their projections onto this line, while maximizing the spread (variance) of the projected data along the line. By doing so, the principal component captures the maximum possible variance in this new dimension. PC1 captures the largest proportion of the data's variance, followed by PC2, which captures the highest proportion of the remaining variance. This pattern continues with each subsequent principal component (PCx). This approach allows PCA to sequentially capture the maximum possible variance in each dimension, thereby minimizing overall information loss.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/about_pca.png" width="1000" height="500" />

Dimensional reduction is not only used to project data into lower dimensional plots, but also can be used to reduce the number of features used in other machine learning models, especially in cases when models suffer from the curse of dimensionality. Therefore, dimensional reduction sometimes can improve model performance.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/benefits_of_lossing_variance.png" width="766" height="79" />

To fit PCA in python, the number of principle components `n_components` can't be larger than the number of features in the data. There're 16 features in the data. The code below is trying to fit PCA and output 16 principle components.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/fit_plot_pca.png" width="609" height="506" />

The generated principle components and their explained variance look as below:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/pca16.png" width="914" height="460" />

Additionally, if you choose a value `x` for `n_components` within its limit (16 in this case), PCA will retain the same variance for all 16 principal components but only output the top x components. For instance, if we set `n_components = 3`, the resulting 3 principal components will have the same variance as the top 3 components shown in the plot above.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/pca3_code.png" width="391" height="84" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/pca3.png" width="546" height="396" />

If we plot the top 3 principle components in 3D space, and color the 2 classes in label "deposit", it looks as below:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_pca.png" width="643" height="368" />

🌻 [Check PCA code here >>][1]

Is there a dimensional reduction method that can better separate the two classes in 3D space, or is it simply not possible to differentiate them effectively in three dimensions? Let’s explore further to find out!


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
