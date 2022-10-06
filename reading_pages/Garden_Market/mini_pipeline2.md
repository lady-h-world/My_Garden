### TPOT

TPOT builds different pipelines with different data preporocessors, feature constructors, feature selectors, models and hyperparameters. All these pipelines form a population from where TPOT will choose the best pipeline that can optimize the model performance. 

It is built upon sklearn, therefore, lots of these operators are using sklearn built-in functions. Meanwhile, [genetic algorithm][1] is used in pipeline selection, which guaranteets the computational cost of TPOT can't be small 😓, even though TPOT added [Feature Set Selector (FSS) and Template][2] to improve the scalability.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/top_architecture.png" width="820" height="406" />
</p>

#### Regression with TPOT

Let's see how to use TPOT in a regression problem.

* `generations` is the number of iterations to run the pipeline selection
* `population_size` specifies the number of pipelines to retrain in each generation

Both `generations` and `population_size` are used in the genetic algorithm, the larger they are, the longer time to run the whole TPOT pipeline, and it doesn't mean you can get better results with larger generations or population.

* `config_dict` allows you to choose different [TPOT configurations][3]. In the code below, Lady H. chose "TPOT light" so that only simpler and fast-running operators will be used in the pipeline, otherwise it takes even longer time to run TPOT. You can try other configurations, such as 
  * "Default TPOT" will select a broad range of operators into the pipeline
  * "TPOT NN" adds more neural network estimators upon all the choices of "Default TPOT"
  * "TPOT cuML" supports the search using GPU
  * And other choices

By default, K-fold cross validation is used in TPOT, and at the end of the pipeline selection, the best pipeline is trained on the entire training data, which is a good practice.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tpot_reg.png" width="1068" height="574" />
</p>

In the code above, we can see, even though Lady H. was using light settings, the pipeline still took 4 hours and the final performance is no better than what FLAML achieved in 5 minutes.

🌻 [Look into TPOT regression experiment details >>][4]

One of the benefits of using TPOT is the saved `.py` file which contains the code of running the selected pipeline, so that in the future you can just run this python file to reproduce the optimized results.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tpot_reg_out.png" width="769" height="642" />
</p>

#### Classification with TPOT

The classification data is much smaller and it only took 61 seconds to finish the TPOT pipeline, with a decent testing performance.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tpot_cla.png" width="1068" height="608" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tpot_cla_out.png" width="810" height="694" />
</p>

🌻 [Look into TPOT classification experiment details >>][4]

Although TPOT finished classification in a short time with good performance, we should keep in mind that most real world datasets are much larger than the classification data used here (14 features, 340 records, 30 classes), even much larger than the regression data here (18 features, 693,861 records). In those cases, TPOT's speed will be concerning.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][5]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<< Looking back][6]
 


[1]:https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3
[2]:https://academic.oup.com/bioinformatics/article/36/1/250/5511404
[3]:http://epistasislab.github.io/tpot/using/#built-in-tpot-configurations
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/mini_pipelines/tpot.ipynb
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline3.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline1.md
