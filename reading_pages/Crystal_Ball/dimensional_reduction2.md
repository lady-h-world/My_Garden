### LDA

LDA (Linear Discriminant Analysis) has a clear goal, that is to maximize the separatability of the classes in the label, while reducing the dimensions.

To better understand how does LDA work, we can compare with PCA:
* PCA is unsupervised learning while LDA is supervised, you need to provide data labels to LDA.
* PCA looks for a new dimension that can maximize the data spread on this new dimension. LDA looks for a new dimension with the goal to maximize the distances between classes and to minimize the variance within each class.
  * For 2 classes, the distance means the differences between the mean of the 2 classes.
  * For 3 or more classes, LDA find a central point of all the data, then measures the distance between each class' mean and the central point.
  * LDA can lose more data variance than PCA.

The dimensions of LDA's output is the minimum of "the number of features of data input" and "the number of classes - 1". Therefore, our banking campaign data will be reduced to 1 dimension after applying LDA. Let's look at how did LDA separate the 2 classes:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_lda.png" width="859" height="454" />

🌻 [Check LDA code here >>][1]


### Isomap

Both PCA and LDA are linear methods, meaning they look for a hyperplane (line or curve) to separate the data. Isomap is non-linear as such hyperplane doesn't exist in its algorithms, instead, it applies non-linear method such as KNN (K-Nearest Neighbors). 

Let's dive deeper to understand how does Isomap work:
1. It applies KNN to find k nearest neighbors for every data point.
2. Then it builds a neighborhood graph to remain the connections between neighbours. Non neighbours are not connected.
3. Applies MDS (multidimensional scaling) to compute each data pair's shortest distance and project to a lower dimension while maintaining the between-point distances.

As we can see, Isomap is a non-linear dimensional reduction method aiming at preserve the local structure.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/local_vs_global.png" width="766" height="79" />

To reduce our campaign data into 3 dimensions using Isomap, the code looks like:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/iso_code.png" width="759" height="398" />

and the data plot looks like: 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Crystal_Ball_images/camapign_dim_redu_images/data_isomap.png" width="594" height="354" />

🌻 [Check Isomap code here >>][1]


### MDS

MDS (Multidimensional Scaling) is used in Isomap, it can be independently used as a dimensional reduction method too.



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
