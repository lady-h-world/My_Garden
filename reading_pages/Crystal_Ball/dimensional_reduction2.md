### LDA

LDA (Linear Discriminant Analysis) has a clear goal, that is to maximize the separatability of the classes in the label, while reducing the dimensions.

To better understand how does LDA work, we can compare with PCA:
* PCA is unsupervised learning while LDA is supervised, you need to provide data labels to LDA.
* PCA looks for a new dimension that can maximize the data spread on this new dimension. LDA looks for a new dimension that can maximize the distances between classes and to minimize the variance within each class.
  * For 2 classes, the distance means the differences between the average of the 2 classes.
  * For 3 or more classes, LDA find a central point of all the data, then measures the distance between each class' average and the central point.
  * LDA can lose more data variance than PCA.

The dimensions of LDA's output is `min(the number of features of data input, the number of classes - 1)`. Therefore, our bank campaign data will be reduced to 1 dimension after applying LDA. Let's look at how did LDA separate the 2 classes:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_lda.png" width="859" height="454" />

🌻 [Check LDA code here >>][1]


### Isomap

Both PCA and LDA are linear methods, meaning they look for a hyperplane (line or curve) to separate the data. Isomap is non-linear as such hyperplane doesn't exist in its algorithm, instead, it applies non-linear method such as KNN (K-Nearest Neighbors). 

Let's dive deeper to understand how does Isomap work:
1. It applies KNN to find k nearest neighbors for every data point.
2. Then it builds a neighborhood graph to maintain the connections between neighbours. Non neighbours are not connected.
3. Apply mMDS (metric multidimensional scaling) to compute each data pair's shortest geodesic distance on the graph, and project to a lower dimension while maintaining the between-point distances.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/about_isomap.png" width="1000" height="379" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/geodesic_distance.png" width="766" height="79" />

As we can see, Isomap is a non-linear dimensional reduction method aiming at preserve the local structure.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/local_vs_global.png" width="766" height="79" />

To reduce our campaign data into 3 dimensions using Isomap, the code looks like:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/iso_code.png" width="759" height="398" />

and the data plot looks like: 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_isomap.png" width="594" height="354" />

🌻 [Check Isomap code here >>][1]


### MDS

MDS (Multidimensional Scaling) is used in Isomap, it can be independently used as a dimensional reduction method too.

As described in Isomap, MDS will project the data into a lower dimensional space and try to maintain the shortest distance between each data-pair. It applies optimization algorithms to minimize the total differences between the original dimension's distance and the lower dimension's distance, [you can check more details here][2].

To reduce our campaign data into 3 dimensions using MDS, the code looks like:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/mds_code.png" width="639" height="432" />

and the data plot looks like: 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_mds.png" width="400" height="361" />

🌻 [Check MDS code here >>][1]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][4]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
[2]:https://towardsdatascience.com/mds-multidimensional-scaling-smart-way-to-reduce-dimensionality-in-python-7c126984e60b
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction3.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction1.md
