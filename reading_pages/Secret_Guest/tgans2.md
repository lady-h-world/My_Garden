#### GANs Carousel

After DCGAN, numerous improvements had been made to enhance GANs' performance. For example:

CGAN (Conditional GAN) allows you to <b>decide the output class</b>.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/exp_cgan.png" width="560" height="280" />

Training GANs is notoriously challenging due to the delicate balance they strive to maintain between 2 competing components, the generator and the discriminator. Throughout this process, stability issues such as gradient vanishing and mode collapse frequently arise.
* <b>Gradient Vanishing</b> occurs when the discriminator becomes confident in its classification, ceasing to update parameters. The gradients become small and diminish significantly as they propagate to the generator layer, leading to the failure of the generator to converge.
* <b>Mode Collapse</b> occurs when the generator consistently produces identical or a limited variety of outputs, failing to sufficiently capture the full diversity of the target data.
* 
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/exp_mode_collapse.png" width="560" height="280" />

WGAN (Wasserstein GAN), LSGAN (Least Squares GAN) were designed to address such stability challenges by employing new loss functions, in contrast to CDGAN.

LSGAN also helps <b>improve output images' perceptive quality</b>, so does ACGAN (Auxiliary Classifier GAN).

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/exp_perceptive.png" width="560" height="180" />

What's noteworthy is the architecture of ACGAN, it added a classifier to the discriminator. Rather than solely predicting the probability of being real, the discriminator is also tasked with classifying the classes of the output. The underlying assumption is that by introducing this additional classification task, the quality of the output can be enhanced.

Disentangled Representation GANs like InforGAN, StackedGAN allows you to change the output properties, such as shape, rotation, thickness, etc.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/exp_properties.png" width="560" height="150" />

Cross-Domain GANs like CycleGAN, CyCADA (Cycle-Consistent Adversarial Domain Adaptation) enables the style transfer of the input. Have you ever played with this popular game on the Earth? By providing a photo, you can change it to a painting style you like:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/exp_style_transfer.png" width="671" height="421" />
