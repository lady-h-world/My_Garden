### t-SNE

Similar to Isomap, t-SNE (t-Distributed Stochastic Neighbor Embedding) also has the goal to project the data into a lower dimensional space while preserving the local neighborhoods' information. But the way it achieves this goal is different, let's look deeper into t-SNE's approach:
1. It measures the similarity of data points by placing all the points on a <b>Normal distribution</b> curve, and calculates the distances between the point of interest and other points. This is done for every data point, and output a <b>matrix</b> to record the similarity score of each data pair.
2. Then t-SNE randomly maps the data into a lower dimensional space, and calculates the similarity using <b>t-distribution</b>. The reason it uses t-distribution in this step rather than Normal distribution, is because t-distribution has flatter shape with higher tails, which can help spread the data out. This step will output a similarity matrix too.
3. Finally t-SNE will apply gradient descent to minimize KL divergence (Kullback–Leibler divergence) to make the 2nd similarity matrix close to the 1st one through an iterative approach until reaching to the max number of iterations. In each iteration, data points will move toward their closest neighbors and away from the distant ones recorded in step 1.

[You can check more details here][6]

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
2. Then it builds a cost function to minimize the total absolute differences between each data point and their weighted neighbors. The sum of neighbors' weights is 1 for each data point, and a weight matrix will be constructed where each data point's weights are determined by minimizing the cost function.
3. When looking for a lower dimensional space, it will try to build a similar cost functions where the data points are replaced by their lower dimensional representations. The weights kept the same as step 2, and LLE will find a lower dimension that can minimize the new cost function.

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



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
[2]:https://towardsdatascience.com/lle-locally-linear-embedding-a-nifty-way-to-reduce-dimensionality-in-python-ab5c38336107
[3]:https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction4.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction2.md
[6]:https://towardsdatascience.com/t-sne-machine-learning-algorithm-a-great-tool-for-dimensionality-reduction-in-python-ec01552f1a1e
