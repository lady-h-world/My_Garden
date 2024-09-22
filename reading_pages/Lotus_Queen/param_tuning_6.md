## Optuna vs Keras Tuner - HPO for Deep Learning

### A Glance of Graden Flowers

There are thousands of flower species in this garden. Occasionally, Lady H. gazes into her crystal ball to enjoy the enchanting view of the blooms. Would you like to take a peek at some of our flowers?

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/flowers_sample.png" width="515" height="523" />
</p>

In the experiment below, there are 102 flower species, with 7,169 flower observations in the training data and 1,020 observations in the testing data. Each observation has been standardized to a 300x300 resolution.

🌻 [To get Flowers data >>][1]


### Optuna HPO in Deep Learning

FLAML doesn't outperform Optuna all the time. In deep learning, where tunable hyperparameters are scattered across different components, [FLAML's deep learning][2] presents a major challenge: it's difficult for users to identify where and how to tune specific hyperparameters. Additionally, its modular design and PyTorch-specific tutorials limit its broader user adoption.

In contrast, Optuna is easier to learn and use. The process for tuning deep learning models is nearly the same as its classical machine learning hyperparameter optimization: users define the model and compute the evaluation metric within an objective function, and a study is created to perform the optimization. Additionally, as shown in the code below, Optuna offers flexibility in tuning hyperparameters across different components.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/code_optuna_cnn.png" width="1067" height="723" />
</p>

Here, Lady H. only used a basic CNN ([Convolutional Neural Network][4]) with 100 epochs, 128 batches and 30 trials for the optimization. In real world practice, such high resolution image dataset often requires a more complex neural network with larger epochs and batch size.

🌻 [Look into Optuna experiment details >>][3]

However, the code took more than 6 hours to finish running and the best performance only got 34.2629 validation loss and 0.0892 validation accuracy... 

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/NN_val_loss_accuracy.png" width="766" height="79" />
</p>

### Keras Tuner HPO in Deep Learning

Now let's look at Keras Tuner.

Like Optuna, Keras Tuner allows users to define the model and tune hyperparameters in different parts of the code. However, the key difference is that while Optuna requires users to handle both model building and evaluation within a single function, Keras Tuner uses a separate function specifically for model definition:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/code_keras_tuner_build_model.png" width="1000" height="406" />
</p>

The defined model will be the input of a tuner, such as the bayesian tuner (`BayesianOptimization`) shown below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/code_keras_tuner_bayesian_tuner.png" width="1068" height="408" />
</p>

The tuners are working as the hyperparameters search strategy, to find an optimal set of parameters that lead to a better model performance. In Keras Tuner, there are 4 major tuners:

* [Random Tuner][5] applies random search, similar to the random search in classical machine learning HPO.
* [Hyperband Tuner][6] is a search algorithm designed to speed up random search through adaptive resource allocation and early-stopping.
* [Bayesian Tuner][7] applies bayesian optimization, an adaptive strategy that keeps updating its prior based on captured behaviour to form the posterior distribution over the objective function, which is used to determine the next point.
* [Sklearn Tuner][8] is mainly used for Sklearn supported estimators and it is off the topic here.

As you might have noticed in the code above, function `get_optimized_model()` reads the tuner instance as the input and generates the optimized model as well as the tuner summary. Now let's look into this function. With the design of Keras Tuner, it encourages users to find the optimal hyperparameters first, then use this best parameter set to find the best epoch number, and finally retrain the model with the best parameters and the best epoch found. This process is a better practice in deep learning HPO.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/code_keras_tuner_optimize_model.png" width="1063" height="563" />
</p>

🌻 [Look into Keras Tuner experiment details >>][9]

In this quick experiment using the same simple CNN settings, Keras Tuner's Bayesian tuner performed more efficiently compared to Optuna and other tuners. However, the Hyperband tuner didn't seem to accelerate the process as it was designed to.

The purpose of the experiments here is to evaluate how Optuna and Keras Tuner perform in tuning hyperparameters for deep learning, so achieving high model performance is a lower priority.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/optuna_vs_keras_tuner.png" width="874" height="389" />
</p>

This is the end of this stop, and we have a gift for you!

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Get your gifts >>][11]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<< Looking back][10]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_flowers.ipynb
[2]:https://github.com/microsoft/FLAML/blob/main/notebook/tune_pytorch.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_cnn.ipynb
[4]:https://en.wikipedia.org/wiki/Convolutional_neural_network
[5]:https://keras.io/api/keras_tuner/tuners/random/
[6]:https://keras.io/api/keras_tuner/tuners/hyperband/
[7]:https://keras.io/api/keras_tuner/tuners/bayesian/
[8]:https://keras.io/api/keras_tuner/tuners/sklearn/
[9]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/keras_tuner_experiments/keras_tuner_cnn.ipynb
[10]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_5.md
[11]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_7.md
