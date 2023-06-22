## Semi-Supervised Learning

So far you have seen the power of supervised and unsupervised learning. Have you veer wonder whether there's anything in between? 

Semi-supervised learning is! It's trying to solve problems with a combination of labeled data and unlabeled data.


### About the Data

The raw data is the same as the [source data in correlation section][1]. To get partially labeled data, we need to mask the data. In real world, 2 types of scenario often appear:
1. Each class has labeled and unlabeled data.
2. Only 1 class is partially labeled and all the other data is unlabeled.

So, we will create both types of data masking. Our data has 2 classes.


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/corr1.md#about-the-data