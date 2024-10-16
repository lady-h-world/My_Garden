### Forecast on Type 2 Data Mask

Now let's solve PU Learning (Positive-Unlabeled Learning) problem, it only has a portion of positive labels and the rest of data is unlabeled. We will show you a DIY PU learning solution and compare it with sklearn built-in PU learning solution. Guess which solution is better!? 😁

The data used in this experiment has 90% records masked, so only 10% records kept the original positive labels. Among all the masked data, there are 58.50% negative and 41.50% positive records.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_90mask_pu.png" width="902" height="232" />


#### How to Solve PU Learning Problem

The main idea is, given all the data, get the probability of being positive for each record `P(positive_label=1 | data)`.

1. Based on conditional probability, we can have `P(positive_label=1 | data) * P(data) = P(has_label=1 | data) * P(data) / P(has_label=1 | positive_label=1)`, and this equation can be converted to `P(positive_label=1 | data) = P(has_label=1 | data) / P(has_label=1 | positive_label=1)`. Therefore, in order to get the final output `P(positive_label=1 | data)` we just need `P(has_label=1 | data)` and `P(has_label=1 | positive_label=1)`.
2. In the data, we replace the original label column with `has_label`, indicating whether each record has a label. Then, split the dataset into train, test datasets, and it's stratified split based on `has_label`. To get `P(has_label=1 | data)`, we just need to use an estimator to train on the training data, the prediction on the testing data is `P(has_label=1 | data)`.
3. `P(has_label=1 | positive_label=1 | sample)` is the probability of "has label", given each positive label in the training data. Averaging these probabilities, we can get `P(has_label=1 | positive_label=1)`.
4. `P(positive_label=1 | data) = P(has_label=1 | data) / P(has_label=1 | positive_label=1)` gets the final output, the probability of being positive for each record.

This method is called as E&N ([Elkan & Noto][2]) method, and seems that, it can be applied to both binary-class and multi-class problems.


#### DIY PU Learning Solution

The DIY solution follows exactly the same steps mentioned above. It outputs the probability of positive class for each data record.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_diy_output.png" width="562" height="124" />

🌻 [Check DIY PU Learning solution here >>][1]

The interesting part is, how are we going to evaluate the results? 🤔

In the perfect situation, you know the labels of all the data, and can apply normal machine learning evaluation metrics, such as AUC, Average Precision, etc. In our example, if we compare predicted probability of positive class with the real labels, we can get 0.71 AUC, as shown in the notebook.

However, in reality, most of the time, you really don't know all the data labels except a small portion of positive labels 🥲. To evaluate the performance, let's calculate following metrics:
* `real_pos_perct`: real positive class percentage in the data. If you don't know the ground truth, this can be business estimated percentage.
* `pred_pos_perct`: predicted positive class percentage. It's the percentage of records with `predicted probability >= threshold`.
* `known_recall`: the recall among known positive labels. If `predicted probability >= threshold` gets predicted positive class and `predicted probability < threshold` gets predicted negative class, comparing them with the known positive labels, we can get this recall.

Here's the code of `pred_pos_perct` and `known_recall`:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_eval_code.png" width="786" height="196" />

We can plot the performance with different thresholds to decide the optimal threshold. The ideal threshold has a decent `known_recall` and `pred_pos_perct` is closer to `real_pos_perct`. In this example, we can choose a threshold between 0.7 ~ 0.75. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_eval_exp.png" width="912" height="455" />

🌻 [Check DIY PU Learning evaluation code >>][1]


#### Sklearn Built-in PU Learning Solution

PULEARN is sklean built-in PU Learning library, it supports 3 classifiers:
* `ElkanotoPuClassifier`: is E&N method, same as above DIY solution.
* `WeightedElkanotoPuClassifier`: also came from E&N paper, it adds weights to unlabeled data.
* `BaggingPuClassifier`: applies a bagging SVM on positive and unlabeled data.

Let's check performance by applying them on our 90% masked data!

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pulearn_classifier1.png" width="977" height="624" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pulearn_classifier2.png" width="1029" height="623" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pulearn_classifier3.png" width="1046" height="632" />

🌻 [Check Built-in PU Learning code >>][3]

Obviously, `ElkanotoPuClassifier` gets the best performance. But the DIY solution has slightly better performance, because at the best threshold where`pred_pos_perct` intersects with `real_pos_perct`, DIY solution has higher `known_recall`.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/diy_pu_eval_0.9.png" width="906" height="459" />

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