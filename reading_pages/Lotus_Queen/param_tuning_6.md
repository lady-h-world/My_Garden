## Optuna vs Keras Tuner - HPO for Deep Learning

When Lady H. planned to end her HPO experiments, a type of new sprout discovered in the garden 🌱. The gardeners said this sprout contains the power called, "Keras Tuner", which can be used in HPO of deep learning. "Ah! Deep Learning HPO, I haven't tried that out. Let me take a quick look", Lady H. thought.

### A Glance of Graden Flowers

Every year, gardeners will bring in new flower species to decorate the garden. These flowers don't have any superpower as Lady H.'s treasure but their beauty 
is making the garden a real wonderland throughout 4 seasons. As a flower expert, Lady H. doesn't really need any tool to classify these beauties, but she loves to pick anything handsome as her dataset. So she turned on her crystal ball to collect a sample of garden flowers.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/crystal_ball_later.png" width="766" height="79" />
</p>

Wanna take a peek at some of our flowers?

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/flowers_sample.png" width="515" height="523" />
</p>

There are 102 flower species, 7169 flower observations in the training data and 1020 observations in the testing data. Each observation had been shapped into the same 300x300 resolution.

🌻 [To get Flowers data >>][1]

### Optuna HPO in Deep Learning

FLAML doesn't outperform Optuna all the time. When it comes to deep learning where tunable hyperparameters don't gather in one place, the documentation of [FLAML deep learning][2] poses the biggest challenge that, it's hard for users to find where to tune which hyperparameters. Its modularization design and pytorch specific tutorials also limit its user acceptability.

By comparison, Optuna is easier to learn and use. The way to tune deep learning models is almost the same as its classical machine learning HPO where users build the model and calculate evaluation metric in an objective function and a study will be created to execute the optimization. At the same time, as we can see from the code below, it's flexible to tune hyperparameters in different places.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/code_optuna_cnn.png" width="1067" height="723" />
</p>

A quick look is a quick look, Lady H. wanted to see the functionalities more than the performance. Therefore, she only used a basic CNN ([Convolutional Neural Network][4]) with 100 epochs, 128 batches and 30 trials for the optimization. In real world practice, such high resolution image dataset often requires a more complex neural network with larger epochs and batch size.

🌻 [Look into Optuna experiment details >>][3]

Even with very low expectation, the output still disappointed Lady H., since the code took more than 6 hours to finish running and the best performance only got 34.2629 validation loss and 0.0892 validation accuracy... 

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/NN_val_loss_accuracy.png" width="766" height="79" />
</p>

### Keras Tuner HPO in Deep Learning

But without setting off against Optuna, how can we realize Keras Tuner is a nice tool?!

Similar to Optuna, Keras Tuner allows users to define the model and tune hyperparameters in different places. The interesting difference is, while Optuna needs users to do model building and the evaluation within 1 function, Keras Tuner requires an independent function to define the model only:

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

With the same simple CNN settings, in this quick experiment, Keras Tuner's bayesian tuner works in a more efficient way, comparing with Optuna and other tuners. And it seems that hyperband tuner didn't speed up as it's designed to be:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Lotus_Queen_images/optuna_vs_keras_tuner.png" width="874" height="389" />
</p>

Can't say the performance is ideal, but it's just a quick check to know how to use Keras Tuner. After this experiment, Lady H. decided to end her HPO experiments and move on to other work. Before visiting other stops, we have a gifts for you!

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
[2]:https://github.com/microsoft/FLAML/blob/main/notebook/flaml_pytorch_cifar10.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/optuna_experiments/optuna_cnn.ipynb
[4]:https://en.wikipedia.org/wiki/Convolutional_neural_network
[5]:https://keras.io/api/keras_tuner/tuners/random/
[6]:https://keras.io/api/keras_tuner/tuners/hyperband/
[7]:https://keras.io/api/keras_tuner/tuners/bayesian/
[8]:https://keras.io/api/keras_tuner/tuners/sklearn/
[9]:https://github.com/lady-h-world/My_Garden/blob/main/code/queen_lotus/keras_tuner_experiments/keras_tuner_cnn.ipynb
[10]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_5.md
[11]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_7.md
