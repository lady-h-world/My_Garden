### t-SNE

Similar to Isomap, t-SNE (t-Distributed Stochastic Neighbor Embedding) also has the goal to project the data into a lower dimensional space while preserving the local neighborhoods' information. But the way they achieve this goal is different, let's look deeper into t-SNE's approach:
1. It measures the similarity of data points by placing all the points on a Normal distribution curve, and calculates the distances between the point of interest and other points. This is done for every data point, and output a matrix to record the similarity score of each data pair.
2. Then t-SNE randomly maps the data into a lower dimensional space, and calculates the simiarity using t-distribution. The reason it uses t-distribution in this step rather than Normal distribution, is because t-distribution has flatter shape with higher tails, which can help spread the data out. This step will output a similarity matrix too.
3. Finally t-SNE will apply gradient descent to minimize KL divergence (Kullback–Leibler divergence). Speaking in human understandable language is to make the 2nd similarity matrix close to the 1st one through an iterative approach until reaching to the max number of iterations. In each iteration, data points will move toward their closest neighbors and away from the distant ones recorded in step 1.

To reduce our campaign data into 3 dimensions using t-SNE, the code looks like:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/code_tsne.png" width="757" height="316" />

An important parameter in the above code is `perplexity`, it specifies the density of neighborhoods. Smaller value leads to more small groups and larger value leads to fewer but tightly packed groups. Normally, you can start with values between 5 and 50.

The data plot looks like: 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_tsne.png" width="459" height="356" />

🌻 [Check t-SNE code here >>][1]


### LLE

LLE (Locally Linear Embedding) also projects the data into a lower dimensional space while preserving the local neighborhoods' information. 

The way it works is similar to Isomap:
1. It applies KNN to find the k nearest neighbors for every data point.
2. It builds a cost function to minimize the total absolute differences between each data point and their weighted neighbors. The sum of neighbors' weights is 1 for each data point, and a weight matrix will be constructed where each data point's weights are determined by minimizing the cost function.
3. When looking for a lower dimensional space, it will try to build a similar cost functions where the data points are replaced by their lower dimensional representations. The weights kept the same as step 2, and LLE will find a lower dimension that can minimize the new cost function.

To understand more details of LLE, check [here][2].





[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
[2]:https://towardsdatascience.com/lle-locally-linear-embedding-a-nifty-way-to-reduce-dimensionality-in-python-ab5c38336107
