### Forecast on PU Learning

Let's solve PU Learning (Positive-Unlabeled Learning), it's a problem only has a portion of positive labels and have the rest of positive class or other classes unlabeled. We will show you a DIY PU learning solution and then compare with sklearn built-in PU learning solution. Let's understand how does the solution work!

The data used in this experiment has 90% records masked, so only 10% records kept the original positive labels. Among all the masked data, there are 58.50% negative and 41.50% positive records.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_90mask_pu.png" width="902" height="232" />


#### How to Solve PU Learning Problem

To main idea is to get `P(positive_label=1 | data)`, given all the data, what's  the probability of each record to be positive.

1. Based on conditional probability, we can have `P(positive_label=1 | data) * P(data) = P(has_label=1 | data) * P(data) / P(has_label=1 | positive_label=1)`, and this equation can be converted to `P(positive_label=1 | data) = P(has_label=1 | data) / P(has_label=1 | positive_label=1)`. Therefore, in order to get the final output `P(positive_label=1 | data)` we just need `P(has_label=1 | data)` and `P(has_label=1 | positive_label=1)`.
2. Replace the original label column with `has_label`, indicating whether each record has a label. Split the dataset into train, test datasets, and it's stratified split based on `has_label`.
3. To get `P(has_label=1 | data)`, we just need to use an estimator to train on the training data, the prediction on the testing data is `P(has_label=1 | data)`.
4. `P(has_label=1 | positive_label=1 | sample)` is the probability of "has label" given each the positive label in the training data. Averaging these values, we can get `P(has_label=1 | positive_label=1)`.
5. `P(positive_label=1 | data) = P(has_label=1 | data) / P(has_label=1 | positive_label=1)` gets the final output, the probability of being positive for each record.

This method is called as E&N ([Elkan & Noto][2]) method, and it seems that it can be applied to both binary-class and multi-class problems.


#### DIY PU Learning Solution

The DIY solution follows exactly the same steps mentioned above. It outputs the probability of positive class for each data record.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_diy_output.png" width="562" height="124" />

🌻 [Check DIY PU Learning solution here >>][1]

The interesting part is, how are we going to evaluate the results? 🤔

In the perfect situation, you know the labels of all the data, and can apply normal machine learning evaluation metrics, such as AUC, Average Precision, etc. In our example, if we compare predicted probability of positive class with the real labels, we can get 0.71 AUC, as shown in the notebook.

However, in reality, most of the time, you really don't know all the data labels except a small portion of positive labels 🥲. To evaluate the performance, let's get following metrics:
* `real_pos_perct`: real positive class percentage in the data. Normally this can be business estimated percentage, if you don't know the ground truth.
* `pred_pos_perct`: predicted positive class percentage. It's the percentage of records with `predicted probability >= threshold`.
* `known_recall`: the recall among known positive labels. If `predicted probability >= threshold` gets predicted positive class and `predicted probability < threshold` gets predicted negative class, comparing them with the known positive labels, we can get the recall.

Here's the code of `pred_pos_perct` and `known_recall`:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_eval_code.png" width="786" height="196" />

We can plot the performance with different thresholds to decide the optimal threshold. The ideal threshold has a decent `known_recall` and `pred_pos_perct` is closer to `real_pos_perct`. In this example, we can choose a threshold between 0.7 ~ 0.75. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_eval_exp.png" width="912" height="455" />

🌻 [Check DIY PU Learning evaluation code >>][1]


#### Sklearn Built-in PU Learning Solution

PULEARN is Sklean built-in PU learning library, it supports 3 classifiers:
* `ElkanotoPuClassifier`: is E&N method, same as above DIY solution.
* `WeightedElkanotoPuClassifier`: also came from E&N paper, it adds weights to unlabeled data.
* `BaggingPuClassifier`: applies a bagging SVM on positive and unlabeled data.

Let's look at their usage and performance!




[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/try_diy_pu_learning.ipynb
[2]:https://cseweb.ucsd.edu/~elkan/posonly.pdf