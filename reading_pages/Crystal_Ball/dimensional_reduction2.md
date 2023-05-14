### LDA

LDA (Linear Discriminant Analysis) has a clear goal, to maximize the separatability of the classes in the label, while reducing the dimensions.

To better understand how does LDA work, we can compare with PCA:
* PCA is unsupervised learning while LDA is supervised, you need to provide data labels to LDA.
* PCA projects data on a new dimension is trying to maximize the data spread on this new dimension. LDA also projects data on a new dimension, but with the goal to maximize the distances between classes.
  * For 2 classes, the distance means the differences between the mean of the 2 classes.
  * For 3 or more classes, LDA find a central point of all the data, then measures the distance between each class' mean and the central point.

When LDA is trying to maximize the separation between classes, it can lose more data variance than PCA.

🌻 [Check LDA code here >>][1]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/magic_dimensional_reduction.ipynb
