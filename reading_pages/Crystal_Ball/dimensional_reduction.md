## Dimensional Reduction

When we try to visualize the data, each column is considered as a dimension. For example, data ploted on x-axis and y-axis is 2 dimensional data, and data ploted on x-axis, y-axis and z-axis is 3 dimensional data.

To plot the data into axes space is a straightforward way to understand the data. However, for data with more than 3 dimensions, such plot is challenging. With crystal ball's power, Lady H. can project higher dimensional data into lower dimensions while keeping the original information as much as possible. This power is called as "Dimensional Reduction".

### About the Data

The data input used here is our Garden Bank's campaign data, [described here][2].


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
