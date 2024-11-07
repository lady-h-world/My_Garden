## Semi-Supervised Learning
So far, you’ve seen both supervised and unsupervised learning. But have you ever wondered if there’s something in between?

That’s where semi-supervised learning comes in! It tackles problems by combining both labeled and unlabeled data.


### About the Data
The raw data is the same as the [campaign data used in association][1]. It has 2 classes and all the records are labeled.

In real world, 2 types of scenario could happen:
1. Each class has labeled and unlabeled data.
2. Only 1 class is partially labeled and all the other data is unlabeled.

To simulate these two real-world scenarios, we can mask the data.


#### Scenario 1 Data Mask
In this scenario, we mask a portion of the data from both classes as unlabeled and allow for flexible adjustment of the mask_rate. The goal is, <b>for the original labeled data to retain their 0 or 1 labels, while the unlabeled data is marked as -1</b>.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_type1_mask.png" width="765" height="111" />

When splitting the data into training and testing sets, we use stratified splitting to ensure that the proportion of each label in the training data matches that in the testing data. In the example below, 95% of the data has been masked:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_splittraintest_mask1.png" width="820" height="512" />

Before beginning any forecasting work, we can visualize the data in 2D or 3D space to understand its distribution and assess the complexity of the problem. To do this, we can use UMAP for dimensionality reduction, projecting the dataset into a 2D space. Each data point will be color-coded based on its mask and true label: "0False" indicates a masked negative class, "0True" represents the original negative class, "1False" is the masked positive class, and "1True" is the original positive class. Let's examine the plot of the training data:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/train_umap.png" width="1377" height="313" />

and the plot of testing data:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/test_umap.png" width="1380" height="309" />

Not seeing any clear patterns to distinguish between the classes, right? 😅 No problem! With this data, we'll work on classifying all the masked instances!

* 🌻 [Check scenario 1 data mask code here >>][2]
* 🌻 [Learn more about UMAP dimensional reduction here >>][3]


#### Scenario 2 Data Mask
In this scenario, we mask most of the data and only keep a portion of positive data labeled. This type of problem is called "PU Learning" (Positive-Unlabeled Learning).

The code to mask the data with configurable masking rate is here:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_mask_pu.png" width="891" height="268" />

When setting `mask_rate=0.95`, it means we will mask 95% data and the rest 5% data will be positive class. Therefore, in the output below, you can see there's 95% labeled as "-1" and 5% labeled as "1". Among all the masked data, there are 55.4% negative class and 44.6% positive class.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_high_rate_pu.png" width="901" height="216" />

When setting `mask_rate=0.3`, it meant to have 70% positive class remain labeled as positive, but because all the positive data only occupies 47.4% population, in this case, we will only get 47.4% labeled data, and all the negative data will be unlabeled.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_low_rate_pu.png" width="896" height="217" />

🌻 [Check scenario 2 mask code here >>][2]

Now let's see how to classify these unlabeled data!


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/rel1.md#about-the-data
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/mask_labels.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/dimensional_reduction4.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/semi_sup2.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/about_resplendent_tree.md