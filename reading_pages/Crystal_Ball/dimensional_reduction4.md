### UMAP
UMAP (Uniform Manifold Approximation and Projection) is a dimensional reduction method that considers <b>both local and global structures</b>. To give a brief summary on how does UMAP work:
1. <b>Construct a Neighborhood Graph</b>: For each data point, identify its nearest neighbors based on a distance metric (such as Euclidean distance). UMAP uses a local neighborhood approach, meaning it considers only a fixed number of nearest neighbors for each point.
2. <b>Fuzzy-Simplicial Set Approximation</b>: Convert the nearest neighbors graph into a fuzzy representation of a simplicial set. This involves determining the likelihood of each pair of data points being connected by an edge in the low-dimensional representation.
3. <b>Optimize Low-Dimensional Embedding</b>: Optimize the low-dimensional representation of the data by minimizing the mismatch between the fuzzy-simplicial set in the original data space and the low-dimensional space. This optimization is achieved through stochastic gradient descent.
4. <b>Preserve Global and Local Structure</b>: Local structure is preserved by ensuring that nearby points in the original space remain close in the low-dimensional space. Global structure is preserved by maintaining the broader connectivity patterns in the data.

To understand more details of UMAP, check [here][1].

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



[1]:https://umap-learn.readthedocs.io/en/latest/how_umap_works.html
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction3.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/crystal_power.md
[5]:https://github.com/lady-h-world/My_Garden/discussions
