### t-SNE

Similar to Isomap, t-SNE (t-Distributed Stochastic Neighbor Embedding) aims to project data into a lower-dimensional space while preserving the local neighborhood information. However, t-SNE takes a different approach to achieve this goal. Let's explore how t-SNE works:

1. <b>Similarity Calculation with Normal Distribution</b>: For each data point, t-SNE measures the similarity to all other points by placing them on a <b>normal distribution curve</b> and calculating the distances. This process is repeated for every data point, resulting in a matrix that records the similarity scores between all data pairs.
2. <b>Mapping to Lower Dimensions with t-Distribution</b>: t-SNE then randomly maps the data into a lower-dimensional space and recalculates the similarities using a <b>t-distribution</b> instead of a normal distribution. The t-distribution, with its flatter shape and higher tails, helps spread the data points further apart. This step produces another similarity matrix in the lower-dimensional space.
3. <b>Minimizing KL Divergence</b>: Finally, t-SNE uses gradient descent to minimize the Kullback-Leibler (KL) divergence between the two similarity matrices (the one from step 1 and the one from step 2). Through an iterative process, t-SNE adjusts the positions of the data points, moving them closer to their nearest neighbors while pushing them away from distant ones, as recorded in the first matrix. This optimization continues until it reaches the maximum number of iterations, resulting in a lower-dimensional representation that preserves the original local neighborhood structure.

To understand more details of t-SNE, check [here][6].

To reduce our campaign data into 3 dimensions using t-SNE, the code looks like:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/code_tsne.png" width="757" height="316" />

An important parameter in the above code is `perplexity`, it specifies the density of neighborhoods. Smaller value leads to larger number of small groups and larger value leads to fewer but tightly packed groups. Normally, you can start with values between 5 and 50.

The data plot looks like: 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_tsne.png" width="459" height="356" />

🌻 [Check t-SNE code here >>][1]


### LLE

LLE (Locally Linear Embedding) also projects the data into a lower dimensional space while preserving the local neighborhoods' information. 

1. Similar to Isomap, it applies KNN to find the k nearest neighbors for every data point.
2. It then constructs a cost function to minimize the total absolute differences between each data point and its weighted neighbors. The sum of the neighbors' weights is set to 1 for each data point, and a weight matrix is created where each data point's weights are determined by minimizing the cost function.
3. When seeking a lower-dimensional representation, LLE tries to build a similar cost function where the data points are replaced by their lower-dimensional representations. The weights from step 2 are preserved, and LLE finds the lower-dimensional space that minimizes this new cost function.

To understand more details of LLE, check [here][2].

The code of LLE is as simple as other dimensional reduction methods. One note for parameter `method`:
* By default, the value is "standard", which is using the algorithm described above.
* Value "modified", "hessian" and "lsta" are modified versions of the algorithm, aiming at improving the regularization of LLE. [Check wiki to learn more about them][3]. Most of the time, "modified" is a recommended choice.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/code_lle.png" width="404" height="196" />

But look at the data plot after LLE dimensional reduction, too simple to be true, right? 😅

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_lle.png" width="447" height="285" />

🌻 [Check LLE code here >>][1]

As we can see, Isomap, MDS, t-SNE and LLE are all focusing on maintaining the local structure while doing the dimensional reduction, then what about the global structure? Is there any method takes care of both local and global data structure?

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/magic_dimensional_reduction.ipynb
[2]:https://towardsdatascience.com/lle-locally-linear-embedding-a-nifty-way-to-reduce-dimensionality-in-python-ab5c38336107
[3]:https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction4.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction2.md
[6]:https://towardsdatascience.com/t-sne-machine-learning-algorithm-a-great-tool-for-dimensionality-reduction-in-python-ec01552f1a1e
