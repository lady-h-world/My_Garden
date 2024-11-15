## Generate Tabular Synthetic Data with TGANs

### About GANs

Generative Adversarial Network, commonly known as "GAN", is gaining increasing popularity worldwide. They have been applied across a wide range of fields, including music generation, style transfer in paintings, the creation of realistic gaming environments, virtual try-ons in the fashion industry, deepfakes, poem writing, and more.

While GANs have found extensive use in manipulating image and text data, a question arises: can they be effectively applied to tabular data? In this stop, we will explore the generation of synthetic tabular data through TGANs (Tabular GANs). Before delving into this, let's gain a brief understanding of how GANs work.


#### Generator vs Discriminator

All the GANs contain 2 key components: generator and discriminator. 

Their roles are like a criminal and a police. The criminal (generator) creates fake diamonds and the police (discriminator) needs to distinguish between the real diamonds and the fake ones. Both of the criminal and the police will enhance their skills through iterative trainings until, finally, the police can hardly differentiate between the real diamonds and the counterfeits.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/manga_dcgan.png" width="744" height="359" />


#### DCGAN 

To understand GANs, we can start from DCGAN (Deep Convolutional GAN), as it's like the vanilla version of GANs. DCGAN kept executing 2 training steps iteratively:

<p>
<img align="left" src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/dcgan_step_1.png" width="623" height="310" />
<p>&nbsp;</p>

<b>Step 1: train the discriminator</b>.

In this step, the generator gets the noise data as input and output a set of fake data labeled as "0". Meanwhile, there is a set of real data labeled as "1". Both real data and fake data are the input of discriminator. The discriminator will update its parameters after the training and output predicted probabilities (probabilities of being the real class) that later sent to loss function to evaluate.

</p>
<p>&nbsp;</p>

<p>
<img align="left" src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/dcgan_step_2.png" width="623" height="320" />
<p>&nbsp;</p>

<b>Step 2: adversarial training, train the generator</b>.

Unlike standard backpropagation, where gradients are used to update the discriminator's parameters, here the discriminator's parameters remain frozen. Instead, the gradients are directed toward the generator to improve its learning process. The trained generator then produces a new set of fake data, labels it as "1" and sends it to the discriminator for a real vs. fake classification.

</p>
<p>&nbsp;</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/gradients.png" width="880" height="90" />
</p>

These 2 steps are executed iteratively until the discriminator can hardly distinguish the real data and the synthetic.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][1]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][2]

[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans2.md
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/secret_guest.md
