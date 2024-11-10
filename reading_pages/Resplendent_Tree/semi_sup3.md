### Forecast on Type 2 Data Mask
Next, let's tackle the PU Learning (Positive-Unlabeled Learning) problem, where only a portion of the positive labels are known, and the rest of the data is unlabeled. We'll demonstrate a DIY PU learning solution and compare it with Scikit-learn's built-in PU learning approach. Which one do you think will perform better? 😁

For this experiment, we're using a dataset where 90% of the records are masked, leaving only 10% with their original positive labels. Among the masked data, 58.50% are negative, and 41.50% are positive.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_90mask_pu.png" width="902" height="232" />


#### How to Solve PU Learning Problem
The main idea is, given all the data, calculate the probability of each record being positive, denoted as `P(positive_label=1 | data)`.

1. Using conditional probability, we can derive the equation: `P(positive_label=1 | data) * P(data) = P(has_label=1 | data) * P(data) / P(has_label=1 | positive_label=1)`, which simplifies to: `P(positive_label=1 | data) = P(has_label=1 | data) / P(has_label=1 | positive_label=1)`. Therefore, to obtain the final output `P(positive_label=1 | data)` we only need `P(has_label=1 | data)` and `P(has_label=1 | positive_label=1)`.
2. In the dataset, we replace the original label column with `has_label`, indicating whether each record has a label. We then split the dataset into training and testing sets using a stratified split based on `has_label`. To calculate `P(has_label=1 | data)`, we train an estimator on the training set, and the predictions on the test set provide us with `P(has_label=1 | data)`.
3. To find `P(has_label=1 | positive_label=1)`, we calculate the probability of "having a label" among the positive samples in the training set. By averaging these probabilities, we obtain `P(has_label=1 | positive_label=1)`.
4. Finally, we use the formula: `P(positive_label=1 | data) = P(has_label=1 | data) / P(has_label=1 | positive_label=1)` to compute the probability of each record being positive.

This approach is known as the [E&N (Elkan & Noto) method][2], and it can be applied to both binary and multi-class classification problems.


#### DIY PU Learning Solution
The DIY solution follows the exact steps outlined above, producing the probability of each data record belonging to the positive class.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_diy_output.png" width="562" height="124" />

🌻 [Check DIY PU Learning solution here >>][1]

The challenge now is, how do we evaluate the results? 🤔

In an ideal scenario, where you have labels for all the data, you can use standard machine learning evaluation metrics such as AUC, Average Precision, etc. For example, in our case, comparing the predicted probabilities of the positive class against the actual labels yields an AUC of 0.71, as demonstrated in the notebook.

However, in reality, you often don't have labels for the entire dataset—only a small fraction of positive labels are known 🥲. To assess performance in such cases, let's calculate the following metrics:
* `real_pos_perct`: the actual percentage of positive class in the dataset. If the ground truth is unknown, this can be estimated by business or domain experts.
* `pred_pos_perct`: the predicted percentage of the positive class. This is calculated as the proportion of records with `predicted probability >= threshold`.
* `known_recall`: the recall among the known positive labels. By classifying records as positive if `predicted probability >= threshold` and as negative otherwise, we can compare these predictions against the known positive labels to calculate this recall.

Here's the code of `pred_pos_perct` and `known_recall`:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_eval_code.png" width="786" height="196" />

We can plot the performance with different thresholds to decide the optimal threshold. The ideal threshold has a decent `known_recall` and `pred_pos_perct` is closer to `real_pos_perct`. In this example, we can choose a threshold between 0.7 ~ 0.75. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_eval_exp.png" width="912" height="455" />

🌻 [Check DIY PU Learning evaluation code >>][1]


#### Sklearn Built-in PU Learning Solution

PULEARN is a sklearn built-in PU Learning library, it supports 3 classifiers:
* `ElkanotoPuClassifier`: is E&N method, same as above DIY solution.
* `WeightedElkanotoPuClassifier`: also came from E&N paper, it adds weights to unlabeled data.
* `BaggingPuClassifier`: applies a bagging SVM on positive and unlabeled data.

Let's check performance by applying them on our 90% masked data!

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pulearn_classifier1.png" width="977" height="624" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pulearn_classifier2.png" width="1029" height="623" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pulearn_classifier3.png" width="1046" height="632" />

🌻 [Check Built-in PU Learning code >>][3]

Clearly, the `ElkanotoPuClassifier` delivers the best overall performance. However, the DIY solution performs slightly better because, at the optimal threshold, where `pred_pos_perct` intersect with `real_pos_perct`, the DIY solution achieves a higher `known_recall`.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/diypu_pulearn.png" width="908" height="611" />

All the experiments above were using 90% masked data. What does the performance look like with different mask rates?


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/try_diy_pu_learning.ipynb
[2]:https://cseweb.ucsd.edu/~elkan/posonly.pdf
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/try_pulearn.ipynb
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/semi_sup4.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/semi_sup2.md