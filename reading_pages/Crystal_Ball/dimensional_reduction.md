## Dimensional Reduction

When we try to visualize the data, each column is considered as a dimension. For example, data ploted on x-axis and y-axis is 2 dimensional data, ploted on x-axis, y-axis and z-axis is 3 dimensional data.

To plot the data into axes space is a straightforward way to understand the data. However, for data with more than 3 dimensions, such plot is challenging. With crystal ball's power, Lady H. can project higher dimensional data into lower dimensions while trying to keep the data structure within the data. This power is called as "Dimensional Reduction".


### PCA 

PCA (Principal Component Analysis) is a popular dimensional reduction method. It outputs several principle components, PC1, PC2, ..., PCn. Imagine each principle component is a line in the axes space, it will try to minimize the distances from data to their projections on the line, by doing so, the spread of data projections on this line can be maximized, therefore the data variance in this dimension is maximized. PC1 captures the highest proportion of the data variance, then PC2 captures the highest proportion of the remaining variance. All the principle components capture the data variance in descending order.

In a word, PCA transforms the data in a way that enables us to capture the maximum amount of variance in each subsequent dimension.


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_campaign.ipynb
