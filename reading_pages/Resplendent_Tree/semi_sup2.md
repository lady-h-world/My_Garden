### Forecast When Each Class Has Unlabeled Data

We will start with classifying the data when each class has unlabeled data. There are multiple approaches to address this. We will:
* compare 3 approaches under the same mask rate, and choose the best approach
* check forecasting performance under different mask rates, using the best approach selected above

The data used in this experiment has 90% records masked, so only 10% records kept the original labels. Among this 10%, there are 5.37% negative and 4.63% positive records. Meanwhile, in all the masked data, there are 52.50% negative and 47.50% positive records.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_90mask.png" width="899" height="251" />

#### Label Propagation

Label Propagation will propagate labels to unlabeled data by assuming closer data points have similar labels. The way it assigns labels to unlabeled data follows these steps:
1. It creates a connected graph by drawing edges between data nodes. `n_neighbors` can limit the number of nodes you want to connect and therefore reduce the demanding resources from your machine, and of course, to build a fully connected graph, it will cost lots of computer resources.
2. On the graph, the edge between more similar nodes gets higher weight while the edge between less similar nodes gets lower weights. A larger weight allows the label to travel through easier so that the probability of propagating the label is higher.
3. From each unlabeled node, performing random walk to find the probability distribution of reaching labeled nodes in order to decide which label has the highest probability. The random walk won't stop until reaching the convergence, such as all paths had been explored, or the probabilities of each possible label no longer change.

Let's apply label propagation on our 90% masked data! Sklearn's label propagation supports 2 kernels, `knn` and `rbf`. The kernel is to measure the similarity between data points. KNN measures the similarity based on the number of neighbours while RBF measures the similarity based on distances.

Here's how to apply label propagation with KNN kernel:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/lp_knn.png" width="581" height="611" />

And here's the code of label propagation with RBF kernel:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/lp_rbf.png" width="809" height="651" />

Looking at the overall performance, RBF kernel works slightly better than KNN kernel in this case.

🌻 [Check label propagation code here >>][1]


#### Label Spreading


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/try_diff_algs.ipynb