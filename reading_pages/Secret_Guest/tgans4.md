First of all, CTABGAN+ added an extra estimator to predict each variable of the tabular data. For discrete variable, it predicts the probability of each category, for continuous variable, it predicts the regression value. The assumption behind is the same as [ACGAN mentioned before][1], by introducing this auxiliary estimator, the quality of the output can be enhanced.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+_auxiliary.png" width="961" height="330" />

The second major change happened in feature encoding:

* <b>Mixed-Type</b> is the same as CTGAN's Mode-specific Normalization, aiming at representing both discrete and continuous variables well.
* <b>Long-Tail</b> applies log transform to better handle continuous variables with long tails. Because VGM used in Mode-specific Normalization has difficulty to encode values towards the tail, log transform compresses and reduces the distances between the tail and the bulk data, allowing VGM to encode all the data easier.
* <b>General Transform</b> (GT) encodes a variable into (-1, 1) range so that the encoding directly compatible with the output of `tanh` activation function used by the generator. GT is selectively applied to single mode continuous variables because VGM can't effectively handle such variables. At the same time, because GT doesn't provide the mode indicator, applying VGM to multi-mode continuous variables is more effective than using GT. GT is also applied on high cardinality discrete variables, because a high cardinality variable has too many unique values and can cause dimensionality explosion after one-hot encoding. However, GT is not recommended for other discrete variables, because, comparing with one-hot vectors, its integer output can impose artificial distances between the different categories which do not reflect the reality.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+_feature_encoder.png" width="961" height="330" />


#### CasTGAN

CasTGAN (Cascade Tabular GAN) was [published in 2023][2]. At the first glance, its architecture looks overwhelming:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/CasTGAN.png" width="961" height="454" />

Let's break it down!

Firstly, you're seeing CasTGAN has several generators (marked as orange square), they get the same noise input.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/CasTGAN1.png" width="961" height="454" />

The generators are arranged in a sequence, each generator produces one of the variables in the tabular data and passes the generated variable to the next generator, this means the last generator will send all the generated variables to the discriminator (marked as blue square).

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/CasTGAN2.png" width="961" height="454" />

Meanwhile, you must have noticed each generator links to the discriminator. If the last generator sends all the output variables to the discriminator, why does CasTGAN have each generator communicates to the discriminator? Lady H. checked throughout the paper and didn't find the reason, but in her opinion, this is to create shortcut connections to relieve gradient vanishing during backpropagation in the hierarchical communication.

Such shortcut connection had been used other neural networks too. The example below came from 2 versions of ResNet, both versions allow the feature map information skip multiple layers and reach to the shallow layer directly.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/resnet_shortcut.png" width="544" height="529" />

What do you think? Feel free to share your ideas [here][3]!


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans2.md
[2]:https://arxiv.org/pdf/2307.00384.pdf
[3]:https://github.com/lady-h-world/My_Garden/discussions
