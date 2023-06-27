### Forecast When Each Class Has Unlabeled Data

We will start with classifying the data when each class has unlabeled data. There are multiple approaches to address this. We will:
* compare 3 approaches under the same mask rate, and choose the best approach
* check forecasting performance under different mask rates, using the best approach selected above

The data used in this experiment has 90% records masked, so only 10% records kept the original labels. Among this 10%, there are 5.37% negative and 4.63% positive records. Meanwhile, in all the masked data, there are 52.50% negative and 47.50% positive records.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_90mask.png" width="899" height="251" />

#### Label Propagation

Label Propagation will propagate labels to unlabeled data by assuming closer data points have similar labels.