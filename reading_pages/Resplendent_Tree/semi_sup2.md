### Classification on Scenario 1 Data Mask

We will begin by classifying the data when unlabeled instances appear within each class.

To do this, we will experiment with three approaches using a dataset where 90% of the labels are masked. In this dataset, only 10% of the records retain their original labels, with 5.37% being negative and 4.63% positive. Among the masked data, 52.50% are negative records, while 47.50% are positive.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_90mask.png" width="899" height="251" />

After comparing the following 3 approaches, we will select the best one to experiment on datasets with varying mask rates.


#### Approach 1: Label Propagation
Label Propagation assigns labels to unlabeled data by assuming that similar data points share the same label. The process of labeling the unlabeled data involves the following steps:
1. <b>Graph Construction</b>: It creates a connected graph by drawing edges between data nodes. You can limit the number of nodes each point connects to using the `n_neighbors` parameter, which reduces the computational resources required. Conversely, building a fully connected graph demands significantly more resources.
2. <b>Edge Weighting</b>: On this graph, edges between more similar nodes receive higher weights, while edges between less similar nodes receive lower weights. A higher weight makes it easier for a label to propagate, increasing the likelihood that it will spread to neighboring nodes.
3. <b>Random Walk</b>: For each unlabeled node, a random walk is performed to determine the probability distribution of reaching labeled nodes. This helps identify which label has the highest probability of being correct. The random walk continues until convergence is achieved, meaning either all paths have been explored or the probabilities of each possible label no longer change.

Let's apply Label Propagation to our dataset with 90% masked labels! Scikit-learn's Label Propagation algorithm supports two kernel options: `knn` and `rbf`. The kernel determines how similarity between data points is measured. The KNN kernel uses the number of neighbors to assess similarity, while the RBF kernel measures similarity based on distances.

Here's how to apply label propagation with KNN kernel:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/lp_knn.png" width="581" height="611" />

And here's the code of label propagation with RBF kernel:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/lp_rbf.png" width="809" height="651" />

The performance above is quite similar, if we consider AUC as the main metric, RBF kernel works slightly better than KNN kernel in this case.

🌻 [Check label propagation code here >>][1]


#### Approach 2: Label Spreading
Label Spreading is similar to Label Propagation, but with a key difference: Label Propagation uses hard clamping, meaning labeled data points never change their labels. In contrast, Label Spreading adopts soft clamping, controlled by the parameter alpha. This parameter determines the balance between the influence of neighboring data and the original label. When `alpha=0`, the model fully preserves the original labels, while `alpha=1` means the initial labels are entirely replaced by information from neighboring points. To learn more details, [check this article][2].

The supported kernels in label spreading are `knn` and `rbf` too. Let's apply label spreading with KNN on our 90% masked data first:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_lspeading_knn.png" width="646" height="704" />

The parameter settings for RBF's Label Spreading differ slightly. In addition to adding the `gamma` parameter required by RBF, we adjusted `alpha` from 0.5 to its default value of 0.2 and increased `n_neighbors` from 7 to 20. These changes were made to improve performance.

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
