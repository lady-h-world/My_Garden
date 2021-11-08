### TPOT

The goal of TPOT is to find the best pipeline that can optimize the model performance. Different pipelines are constructed with different data preorocessors, feature constructors, feature selectors, models and hyperparameters. It is built upon sklearn, therefore, lots of these operators are using sklearn built-in functions. Meanwhile, [genetic algorithm][1] is used in pipeline selection, which guaranteets the computational cost of TPOT can't be small, even though TPOT added [Feature Set Selector (FSS) and Template][2] to improve the scalability.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/top_architecture.png" width="820" height="406" />
</p>

#### Regression with TPOT

Let's see how to use TPOT in a regression problem.

* `generations` is the number of iterations to run the pipeline selection
* `population_size` specifies the number of pipelines to retrain in each generation

Both `generations` and `population_size` are used in the genetic algorithm, the larger they are, the longer time to run the whole TPOT pipeline, and it's not guaranteed to get better results wither larger generations or population.

* `config_dict` allows you to choose [different configurations][3]. In the code below, Lady H. chose "TPOT light" so that only simpler and fast-running operators will be used in the pipeline, otherwise it takes even longer time to run TPOT. You can try other configurations, such as "Default TPOT" which will select a broad range of operators into the pipeline; "TPOT NN" adds more neural network estimators upon all the choices of "Default TPOT"; "TPOT cuML" supports the search using GPU, and there are other choices too.

K-fold cross validation is used in TPOT, and at the end of the pipeline selection, the best pipeline is trained on the entire training data, which is a good practice.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tpot_reg.png" width="1068" height="574" />
</p>

In the code above, we can see, even though Lady H. was using light weighted settings, the pipeline still took 4 hours and the final performance is no better than what FLAML got in 5 minutes.

🌻[Look into TPOT regression experiment details >>][4]

One of the benefits of using TPOT is the saved .py file which contains the code of running the selected pipeline, so that in the future you can just run this python file to reproduce the optimized results.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tpot_reg_out.png" width="769" height="642" />
</p>

#### Classification with TPOT


[1]:https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3
[2]:https://academic.oup.com/bioinformatics/article/36/1/250/5511404
[3]:http://epistasislab.github.io/tpot/using/#built-in-tpot-configurations
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/mini_pipelines/tpot.ipynb
