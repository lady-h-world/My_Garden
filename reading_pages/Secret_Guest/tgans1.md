## Generate Tabular Synthetic Data with TGANs

### About GANs

Generative Adversarial Network, commonly known as "GAN", is gaining increasing popularity on the Earth. They have been applied across a wide range of fields, including music generation, style transfer in paintings, the creation of realistic gaming environments, virtual try-ons in the fashion industry, deepfakes, poem writing, and more.

While GANs have found extensive use in manipulating image and text data, a question arises: can they be effectively applied to tabular data? In the stop, we will explore the generation of synthetic tabular data through TGANs (Tabular GANs). Before delving into this, let's gain a brief understanding of how GANs operate.


### Generator vs Discriminator

All the GANs contain 2 key components: generator and discriminator. 

Their roles are like a criminal and a police. The criminal (generator) creates fake diamonds and the police (discriminator) needs to distinguish between the real diamonds and the fake ones. Both of the criminal and the police will enhance their skills through iterative trainings until, finally, the police can hardly differentiate between the real diamonds and the counterfeits.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/manga_dcgan.png" width="744" height="359" />


### DCGAN 

To understand GANs, we can start from DCGAN (Deep Convolutional GAN), as it's like the vanilla version of GANs. DCGAN kept executing 2 trainings steps iteratively:

<p>
<img align="left" src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/dcgan_step1.png" width="623" height="310" />
<p>&nbsp;</p>

<b>Step 1: train the discriminator</b>.

In this step, the generator gets noise data as input and output a set of fake data labeled as "0". Meanwhile, there is a set of real data labeled as "1". Both real data and fake data are the input of discriminator. The discriminator will update its parameters after the training and output predicted probabilities (probabilities of being real class) that later sent to loss function to evaluate.

</p>
<p>&nbsp;</p>

<p>
<img align="left" src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/dcgan_step2.png" width="623" height="320" />
<p>&nbsp;</p>

<b>Step 2: adversarial training, train the generator</b>.

Unlike standard backpropagation, where gradients should update the discriminator's parameters, in this case, the discriminator's parameters stay frozen. The gradients are directed to the generator to enhance its learning process. The trained generator produces a new set of fake data, labeling this artificial dataset as "1," and subsequently submits it to the discriminator for real class prediction.

</p>
<p>&nbsp;</p>

