First of all, CTABGAN+ added an extra estimator to predict each variable of the tabular data. For discrete variable, it predicts the probability of each category, for continuous variable, it predicts the regression value. The assumption behind is the same as [ACGAN mentioned before][1], by introducing this auxiliary estimator, the quality of the output can be enhanced.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+_auxiliary.png" width="961" height="360" />

The second major change happened in feature encoding:

* <b>Mixed-Type</b> is the same as CTGAN's Mode-specific Normalization, aiming at representing both discrete and continuous variables well.
* <b>Long-Tail</b> applies log transform to better handle continuous variables with long tails. Because VGM used in Mode-specific Normalization has difficulty to encode values towards the tail, with log transform it can compress and reduce the distances between the tail and the bulk data, allowing VGM to encode all the data easier.
* <b>General Transform</b> (GT) encodes a variable into (-1, 1) range so that the encoding directly compatible with the output of `tanh` activation function used by the generator. GT is selectively applied to single mode continuous variables because VGM can't effectively handle such variables. At the same time, because GT doesn't provide the mode indicator, applying VGM to multi-mode continuous variables is more effective than using GT. GT is also applied on high cardinality discrete variables, because a high cardinality variable has too many unique values and can cause dimensionality explosion after one-hot encoding. However, GT is not recommended for other discrete variables, because, comparing with one-hot vectors, its integer output can impose artificial distances between the different categories which do not reflect the reality.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+_feature_encoder.png" width="961" height="360" />


#### CasTGAN

CasTGAN (Cascade Tabular GAN) was [published in 2023][2], it introduced a cascaded architecture:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/CasTGAN.png" width="961" height="454" />

The architecture looks complex, but it's still a combination of generator, discriminator and auxiliary estimator. Let's break it down!

Firstly, you're seeing CasTGAN has several generators (marked as orange squares), they get the same noise input.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/CasTGAN1.png" width="961" height="454" />

The generators are arranged in a sequence, each generator produces one of the variables in the tabular data and passes the generated variable to the next generator. Consequently, the last generator sends all the generated variables to the discriminator (marked as blue square).

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/CasTGAN2.png" width="961" height="454" />

Meanwhile, you must have noticed each generator connects to the discriminator. If the last generator sends all the output variables to the discriminator, why does CasTGAN have each generator communicates to the discriminator? Lady H. checked throughout the paper and didn't find the reason, but in her opinion, this is to create shortcut connections to relieve gradient vanishing during backpropagation in the hierarchical communication.

Such shortcut connection had been used in other neural networks too. The example below came from 2 versions of ResNet, both versions allow the feature map information skip multiple layers and reach to the shallow layer directly.

What do you think? Feel free to share your ideas [here][3]!

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/resnet_shortcut.png" width="344" height="329" />

CasTGAN also has multiple auxiliary estimators (marked as purple squares). Each generator has a corresponding auxiliary estimator to predict the same the variable that the generator attempts to generate. Each auxiliary estimator is a pretrained LightGBM model, it's trained on the rest of variables in order to predict the target variable. The benefit of using LightGBM here is, it can handle categorical variables without using ont-hot encoding. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/CasTGAN3.png" width="961" height="454" />

<p>
<img align="left" src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/castgan_al_details.png" width="527" height="813" />


</p>
According to CasTGAN's paper, its cascaded architecture is able to capture the correlations and interdependence between variables, and therefore making generated synthetic data more realistic. 

This makes sense if we dive into each individual auxiliary estimator. 

Next, you will Lady H.'s experiments using these 3 Tabular GANs. Guess which TGAN got better results? 😉

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]



[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans2.md
[2]:https://arxiv.org/pdf/2307.00384.pdf
[3]:https://github.com/lady-h-world/My_Garden/discussions
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans5.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans3.md
