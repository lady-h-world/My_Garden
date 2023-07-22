### Forecast on Type 1 Data Mask

We will start with classifying the data when unlabeled data appears in each class. 

We will experiment with 3 approaches on a 90% masked data. In this data, only 10% records kept the original labels, 5.37% negative and 4.63% positive. Among all the masked data, there're 52.50% negative and 47.50% positive records.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_90mask.png" width="899" height="251" />

After the comparison of 3 approaches, we will choose the best approach to experiment on datasets with different mask rates.


#### Approach 1: Label Propagation

Label Propagation will propagate labels to unlabeled data by assuming similar data points have same labels. The way it assigns labels to unlabeled data follows these steps:
1. It creates a connected graph by drawing edges between data nodes. `n_neighbors` can limit the number of nodes you want to connect and therefore reduce the demanding resources from your machine, on the contrary, to build a fully connected graph, it will cost lots of computer resources.
2. On the graph, the edge between more similar nodes gets higher weight while the edge between less similar nodes gets lower weights. A larger weight allows the label to travel through easier so that the probability of propagating the label is higher.
3. From each unlabeled node, performing random walk to find the probability distribution of reaching labeled nodes in order to decide which label has the highest probability. The random walk won't stop until reaching the convergence, such as all paths had been explored, or the probabilities of each possible label no longer change.

Let's apply label propagation on our 90% masked data! Sklearn's label propagation supports 2 kernels, `knn` and `rbf`. The kernel is to measure the similarity between data points. KNN measures the similarity based on the number of neighbours while RBF measures the similarity based on distances.

Here's how to apply label propagation with KNN kernel:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/lp_knn.png" width="581" height="611" />

And here's the code of label propagation with RBF kernel:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/lp_rbf.png" width="809" height="651" />

The performance above is quite similar, if we consider AUC as the main metric, RBF kernel works slightly better than KNN kernel in this case.

🌻 [Check label propagation code here >>][1]


#### Approach 2: Label Spreading

Label spreading is similar to label propagation. The main difference is, label propagation uses hard clamping, meaning, a labeled data point never changes its label. However, label spreading adopts soft clamping, it has a parameter `alpha` to control the proportion of information received from neighbors vs. from the initial label. When `alpha=0`, it keeps all the original information, but when `alpha=1`, it replaces all the initial information. To learn more details, [check this article][2].

The supported kernels in label spreading are "knn" and "rbf" too. Let's apply label spreading with KNN on our 90% masked data first:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_lspeading_knn.png" width="646" height="704" />

The parameter values used in RBF's label spreading is a bit different, not just adding `gamma` required by RBF, but also adjusted `alpha=0.5` to default value `alpha=0.2` and increased `n_neighbors=7` to `n_neighbors=20`, so that the performance won't look too bad.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_spreading_rbf.png" width="608" height="638" />

Still got similar performance, and RBF kernel has slightly better AUC.

🌻 [Check label spreading code here >>][1]


#### Approach 3: Self Training

Self training allows you to select an estimator supported by sklearn, such as XGBoost, LightGBM to train on the labeled data and predict on unlabeled data. Then use predictions as pseudo labels, adding them to existing labels and do another round of train & predict. Repeat till all the data got the label or reached to the max iteration.

Sklearn provides built-in `SelfTrainingClassifier`, and it can be used in this way:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_self_training.png" width="735" height="755" />

🌻 [Check self training code here >>][1]

Comparing with label spreading and label propagation, self training took much longer time to run, and unfortunately, it got the worst performance.
 

#### Performance with Different Mask Rates

Overall, label spreading with RBF kernel got a bit better performance on our 90% masked data. Now, let's apply it on data with different mask rates.

As we can see below, when there is more data got labeled (lower mask rate), the performance will get better. When labeled data occupies more than 50%, the performance difference becomes smaller when labeling percentage increases, for example, 50% labeled data and 80% labeled data have much less performance difference.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/ls_diff_mask.png" width="1187" height="922" />

🌻 [Check detailed code here >>][5]

The best performance we have above is 0.74 AUC and 0.65 Recall. If all the data is labeled, we can get 0.84 AUC and 0.85 Recall. In order to get closer to all-labeled-data performance, we can optimize model parameters or try more advanced algorithms. Would you like to share your ideas and experiments [here][7]? 😉

🌻 [Check all-labeled-data forecast >>][6]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/try_diff_algs.ipynb
[2]:https://towardsdatascience.com/how-to-benefit-from-the-semi-supervised-learning-with-label-spreading-algorithm-2f373ae5de96
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/semi_sup1.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/semi_sup3.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/diff_mask_perct.ipynb
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/all_real_forecast.ipynb
[7]:https://github.com/lady-h-world/My_Garden/discussions
