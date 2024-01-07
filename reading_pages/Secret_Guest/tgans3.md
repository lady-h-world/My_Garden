### Why Synthetic Data?

Before we dive into how to generate synthetic data, have you ever thought about, why do we need synthetic data?

You will get a long list of answers if asking ChatGPT. Lady H. summarized a few situations based on her experience:
* Data Sharing: Synthetic data can be shared with other teams when data privacy is a concern but those teams require realistic data to perform their tasks.
* Testing: To assess the quality or efficiency of a product, real data might have incomplete test cases or limited data size. By using synthetic data you can generate additional test cases to ensure the product quality, you can also create datasets of various sizes to conduct load tests on the product.
* Data Augmentation: Computer vision often employees this method, by using synthetic data it increases the diversity of training data, with the aim to enhance model performance.

Any other use cases can't be covered by these 3 categories? You're very welcome to share your ideas [here][1]!


### Tabular GANs

Numerous GANs (Generative Adversarial Networks) have been applied to image and text data. However, given the significance of tabular data as a crucial data source, can GANs be employed to generate synthetic tabular data? Indeed, there are, and these GANs are called as TGANs (Tabular GANs). 

#### CTGAN

CTGAN (Conditional Tabular GAN) was [published in 2019][2], and later multiple promising Tabular GANs were built upon it, so we can consider it as the vanilla version of Tabular GANs!

The architecture of CTGAN can be summarized as below:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_architecture.png" width="961" height="330" />

Comparing with the architecture of DCGAN (the vanilla version of GANs), it has 2 major changes: <b>Mode-specific Normalization</b> and <b>Train-by-Sample & Conditional Vector</b>.

Tabular data is typically a combination of discrete variables and continuous variables. GANs can readily manage one-hot encoded vectors, making the representation of discrete variables straightforward. However, the challenge lies in effectively representing the more intricate distributions inherent in continuous variables. Therefore, CTGAN proposes <b>Mode-specific Normalization</b> to address the challenge by converting continuous variables into one-hot format.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_msn.png" width="961" height="330" />

Let's delve deeper into Mode-specific Normalization by breaking it down into 3 steps:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/msn.png" width="768" height="262" />

1. Apply VGM (variational Gaussian mixture model) to estimate the number of modes (peaks) in a continuous variable's distribution, and fit into a Gaussian mixture, the learned Gaussian mixture forms a normal distribution for each mode. In the example above, the continuous variable distribution represented by a blue dashed curve has 3 modes, so 3 normal distributions got created.
2. Each value of this continuous variable can be represented as `Ci,j` (ith column, jth row in the Tabular data), plot it on the Gaussian mixture and get the probability of each mode. Choose the normal distribution with the highest probability. In the example above `ρ3` is the highest probability, so the 3rd normal distribution is selected.
3. Use the selected normal distribution's mean `η` and standard deviation `φ` to calculate a normalized value `αi,j = (Ci,j - η) / (4 * φ)`. Meanwhile, use a binary vector `βi,j` to record which mode was selected. In above example, the 3rd mode was selected so `βi,j = [0, 0, 1]`.

Now the original value `Ci,j` is encoded as one-hot format through `αi,j ⊕ βi,j` where ⊕ is the vector concatenation operator.

Traditionally, the generator may not be trained well if there are imbalanced discrete variables, because their minority categories can't be sampled evenly. <b>Train-by-Sample & Conditional Vector</b> is trying to evenly (but not necessary uniformly) explore all categories in each discrete variable during training process and recover the real data distribution during test. "Conditional vector" means, given a particular categorical value, its rows in the real data have to appear in the data sample. Generator trained by such conditional distributions is called as "conditional generator", which is also why CTGAN is named as "conditional".


<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_cv.png" width="961" height="330" />


[1]:https://github.com/lady-h-world/My_Garden/discussions
[2]:https://arxiv.org/pdf/1907.00503.pdf