### Why Synthetic Tabular Data?

There are several benefits of using synthetic tabular data across different industries. For example:
* <b>Enabling data privacy and ethical AI</b>
  * Health researchers use synthetic tabular data to protect real patients' data while conducting their research.
  * Banks build machine learning models on synthetic tabular data to protect customer data privacy.
* <b>data simulation</b> is often used when existing real data has limited scenarios
  * Banks simulate synthetic data to create more real-world scenarios, such as customer behavior data to improve personalized banking services and customer interactions to enhance relationships.
  * Supply chain systems simulate synthetic data to mimic the supply chain process, optimizing logistics, production schedules, and inventory management.

Have you ever used synthetic tabular data? Welcome to share your experience or ideas [here][1]!


### Tabular GANs

Numerous GANs (Generative Adversarial Networks) have been applied to image and text data. However, given the significance role that tabular data plays in data science, can GANs be employed to generate synthetic tabular data? Indeed, there are, and these GANs are called as TGANs (Tabular GANs). 


#### CTGAN

CTGAN (Conditional Tabular GAN) was [published in 2019][2], and later multiple promising Tabular GANs were built upon it, so we can consider it as the vanilla version of Tabular GANs!

The architecture of CTGAN can be summarized as below:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_architecture.png" width="961" height="330" />

Comparing with the architecture of DCGAN (the vanilla version of GANs), it has 2 major changes: <b>Mode-specific Normalization</b> and <b>Train-by-Sample & Conditional Vector</b>.

Tabular data is typically a combination of discrete variables and continuous variables. Discrete variables can be represented as one-hot format and be processed by GANs directly. However, the challenge lies in effectively processing the more intricate distributions inherent in continuous variables. Therefore, CTGAN proposes <b>Mode-specific Normalization</b> to address this challenge.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_msn_rep.png" width="961" height="330" />

Let's delve deeper into Mode-specific Normalization by breaking it down into 3 steps:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/msn.png" width="768" height="262" />

1. Apply VGM (variational Gaussian mixture model) to estimate the number of modes in a continuous variable's distribution, and fit into a Gaussian mixture, the learned Gaussian mixture forms a normal distribution for each mode. In the example above, the continuous variable distribution represented by a blue dashed curve has 3 estimated modes, so 3 normal distributions got created.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/VGM_mode.png" width="880" height="90" />
</p>

2. Each value of this continuous variable can be represented as `Ci,j` (ith column, jth row in the Tabular data), plot it on the Gaussian mixture and get the probability of each mode. Choose the mode with the highest probability. In the example above `ρ3` is the highest probability, so the 3rd mode is selected.
3. Use the selected mode's mean `η` and standard deviation `φ` to calculate a normalized value `αi,j = (Ci,j - η) / (4 * φ)`, representing the original value in the mode. Meanwhile, use a binary vector `βi,j` to record which mode was selected. In above example, the 3rd one was selected so `βi,j = [0, 0, 1]`.

Now the original value `Ci,j` is encoded as a vector through `αi,j ⊕ βi,j` where ⊕ is the vector concatenation operator. 

Traditionally, the generator may not be trained well if there are imbalanced discrete variables, because the minority categories can't be sampled evenly. <b>Train-by-Sample & Conditional Vector</b> is trying to evenly (but not necessary uniformly) explore all categories in each discrete variable during training process and recover the real data distribution during test. "Conditional vector" means, given a particular categorical value, its rows in the real data have to appear in the data sample. Generator trained by such conditional distributions is called as "conditional generator", which is also why CTGAN is named as "conditional".


<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctgan_cv.png" width="961" height="330" />


#### CTABGAN+

CTABGAN+ was [published in 2022][3]. See its architecture below, looks quite like CTGAN's architectures, right? Comparing with CTGAN, it has made 2 major changes. Let's look into details!

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+.png" width="961" height="330" />

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]


[1]:https://github.com/lady-h-world/My_Garden/discussions
[2]:https://arxiv.org/pdf/1907.00503.pdf
[3]:https://arxiv.org/pdf/2204.00401.pdf
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans4.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans2.md