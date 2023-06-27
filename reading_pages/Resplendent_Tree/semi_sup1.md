## Semi-Supervised Learning

So far you have seen the power of supervised and unsupervised learning. Have you veer wonder whether there's anything in between? 

Semi-supervised learning is! It's trying to solve problems with a combination of labeled data and unlabeled data.


### About the Data

The raw data is the same as the [source data in correlation section][1]. To get partially labeled data, we need to mask the data. In real world, 2 types of scenario often appear:
1. Each class has labeled and unlabeled data.
2. Only 1 class is partially labeled and all the other data is unlabeled.

So, we will create both types of data masking. Our data has 2 classes.

#### Type 1 Mask

In the first type of masking, we mask some data in both classes as unlabeled, and allow flexible settings on unlabeled data percentage.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_type1_mask.png" width="765" height="111" />

The original labeled data still keep their 0 or 1 labels, and the unlabeled data will be marked as -1. If we apply stratified split to get train & test data, the percentage of each data label in training data stays the same in testing data. In the example below, we have masked 95% data:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_splittraintest_mask1.png" width="820" height="512" />

If we apply UMAP dimensional reduction to reduce the dataset into 2 dimensions, coloring the data point based on their masks and real labels ("0False" means masked negative class, "0True" means original negative class, "1False" means masked positive class, "1True" means original positive class), let's look at the plot of training data:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/train_umap.png" width="1377" height="313" />

and the plot of testing data:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/test_umap.png" width="1380" height="309" />

Can't find any pattern to differentiate classes well, right? Cool! With this type of data, we will try to classify all the masked data.

* 🌻 [Check type 1 mask code here >>][2]
* 🌻 [Learn more about UMAP dimensional reduction here >>][3]


#### Type 2 Mask

In the second type of masking, we will mask most the data and only keep the labels of a portion of positive data. This type of problem is called "PU Learning" (Positive-Unlabeled Learning).

The code to mask the data with any masking rate is here:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_mask_pu.png" width="891" height="268" />

When setting `mask_rate=0.95`, it means we will mask 95% data and the rest 5% data will be positive class. Therefore in the output below, you can see there's 95% "-1" and 5% "1". Among all the masked data, there are 55.4% negative class and 44.6% positive class.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_high_rate_pu.png" width="901" height="216" />

When setting `mask_rate=0.3`, it meant to have 70% positive class remain labeled, but because all the positive data only occupies 47.4% population, in this case, we will only get 47.4% labeled data, and all the negative data will be unlabeled.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_low_rate_pu.png" width="896" height="217" />

🌻 [Check type 2 mask code here >>][2]

After masking the data, let's see how does the forecasting perform.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/corr1.md#about-the-data
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/mask_labels.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction4.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/semi_sup2.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/about_resplendent_tree.md