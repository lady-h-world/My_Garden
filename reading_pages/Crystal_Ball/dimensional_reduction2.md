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


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
