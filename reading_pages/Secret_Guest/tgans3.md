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

Tabular data is typically a combination of discrete variables and continuous variables. GANs can readily manage one-hot encoded vectors, making the representation of discrete variables straightforward. However, the challenge lies in effectively representing the more intricate distributions inherent in continuous variables. Therefore, CTGAN proposes <b>Mode-specific Normalization</b> to address the challenge and the representation of continuous variables is one-hot format too.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_msn.png" width="961" height="330" />


[1]:https://github.com/lady-h-world/My_Garden/discussions
[2]:https://arxiv.org/pdf/1907.00503.pdf