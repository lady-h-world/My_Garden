### UMAP

UMAP (Uniform Manifold Approximation and Projection) is a dimensional reduction method that considers both local and global structures when it's trying to reduce data dimensions. To preserving the local structures, it builds a neighborhood graph by considering the varying distances between different densities, local connectivity with different levels of certainties, and the edge weights between connected points. When projecting the data to a lower dimensional space, it uses global euclidean distance to control the minimum spread of points, and looking for optimal edge weights that can minimize the cross entropy through stochastic gradient descent. For more details, [check here][1].

Meanwhile, UMAP supports both unsupervised and supervised dimensional reduction! Look at the code below, the only difference is in `fit_transform()` function:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/code_umap.png" width="999" height="321" />

After the data had been reduced to 3 dimensions, the unsupervised output looks like this:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_umap_unsupervised.png" width="379" height="283" />

For supervised output, let's look at the projections from both training data and testing data: 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_umap_supervised.png" width="996" height="531" />

🌻 [Check UMAP code here >>][2]

After seeing all these methods, how do you plan to do dimensional reduction in the future? You're more than welcome to share you ideas [here][5]!

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Crystal Power >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]



[1]:https://towardsdatascience.com/umap-dimensionality-reduction-an-incredibly-robust-machine-learning-algorithm-b5acb01de568
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction3.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/crystal_power.md
[5]:https://github.com/lady-h-world/My_Garden/discussions
