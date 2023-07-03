### Forecast on PU Learning

Let's solve PU Learning (Positive-Unlabeled Learning), it's a problem only has a portion of positive labels and have the rest of positive class or other classes unlabeled. We will show you a DIY PU learning solution and then compare with sklearn built-in PU learning solution. Let's understand how does the solution work!


#### How to Solve PU Learning Problem

To main idea is to get `P(positive_label=1 | data)`, given all the data, what's  the probability of each record to be positive.

1. Based on conditional probability, we can have `P(positive_label=1 | data) * P(data) = P(has_label=1 | data) * P(data) / P(has_label=1 | positive_label=1)`, and this equation can be converted to `P(positive_label=1 | data) = P(has_label=1 | data) / P(has_label=1 | positive_label=1)`. Therefore, in order to get the final output `P(positive_label=1 | data)` we just need `P(has_label=1 | data)` and `P(has_label=1 | positive_label=1)`.
2. Replace the original label column with `has_label`, indicating whether each record has a label. Split the dataset into train, test datasets, and it's stratified split based on `has_label`.
3. To get `P(has_label=1 | data)`, we just need to use an estimator to train on the training data, the prediction on the testing data is `P(has_label=1 | data)`.
4. `P(has_label=1 | positive_label=1 | sample)` is the probability of "has label" given each the positive label in the training data. Averaging these values, we can get `P(has_label=1 | positive_label=1)`.
5. `P(positive_label=1 | data) = P(has_label=1 | data) / P(has_label=1 | positive_label=1)` gets the final output, the probability of being positive for each record.

Seems that this method applies to both binary-class and multi-class problems.


#### DIY PU Learning Solution