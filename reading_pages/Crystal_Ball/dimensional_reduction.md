## Dimensional Reduction

When we try to visualize the data, each column is considered as a dimension. For example, data ploted on x-axis and y-axis is 2 dimensional data, and data ploted on x-axis, y-axis and z-axis is 3 dimensional data.

To plot the data into axes space is a straightforward way to understand the data. However, for data with more than 3 dimensions, such plot is challenging. With crystal ball's power, Lady H. can project higher dimensional data into lower dimensions while keeping the original information as much as possible. This power is called as "Dimensional Reduction".


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

PCA (Principal Component Analysis) is a popular dimensional reduction method. It outputs several principle components, PC1, PC2, ..., PCn, and reduces total number of features. 

Imagine each principle component is a line in the axes space, it will try to minimize the distances from data to their projections on this line, so that, the spread of data projections on this line can be maximized, therefore the data variance in this dimension is maximized. PC1 captures the highest proportion of the data variance, then PC2 captures the highest proportion of the remaining variance. These principle components capture the data variance in descending order.

Dimensional reduction will inevitably lose some original information. One of the approaches to keep the original information is to keep the data variance. PCA transforms the data in a way that enables us to capture the maximum amount of variance in each subsequent dimension.

Dimensional reduction is not only used to project data into lower dimensional plots, but also can be used to reduce the number of features used in other machine learning models, especially in cases when models suffer from the curse of dimensionality. Therefore, dimensional reduction sometimes can improve model performance.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/benefits_of_lossing_variance.png" width="766" height="79" />
</p>



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/corr1.md#about-the-data
[3]:https://contrib.scikit-learn.org/category_encoders/targetencoder.html
