#### Task Data Preprocessing

This is the step where you can do whatever data operation in order to make sure the data set can be directly used for later model training. 

In Lady H.'s use case, she just wanted to convert some features into "category" type. Because for models like LGBM (LightGBM), categorical features can be handled automatically if they are specified as "category" type. 

* `le_col` represents a feature that originally has a combo of numerical and string values, models won't be able to undrstand the data type and will report errors. So Lady H. converted them into integer format with label encoding first, then convert to "category" type.
* `int_cat_col` represents a categorical feature that originally appears to be integer format, they can be converted to "category" directly.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/data_preprocessing_code.png" width="812" height="291" />
</p>

🌻 [Check data preprocessing config >>][1]

🌻 [Check data preprocessing task >>][2]


#### Task Model Selection

Time to fit the model with our preprocessed data. In an automated machine learning pipeline, it will be great to enable model selection so that the pipeline can choose an optimal model when the dataset changes. As we have seen in [mini pipelines][3] that MLJar is a great model selection tool, therefore in model selection task, we can simply create a configurable MLJar automl instance to fit the data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/model_selection_code.png" width="758" height="264" />
</p>

🌻 [Check model selection config >>][4]

🌻 [Check model selection task >>][5]

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/lazy_feature_set.png" width="766" height="79" />
</p>

#### Task Model Evaluation

After fitting the selected model with the training data, time to evaluate the model performance on the testing data.

In this model evaluation task, R2 score is expected to be used for this regression problem. At the same time, Lady H. has generated the lower bound and the upper bound of model confidence interval. But what is "model confidence interval"?

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/model_evaluation_code.png" width="764" height="255" />
</p>

The confidence interval (CI) of a model indicates our confidence on the testing performance score, about whether it is the true model performance.

For example, Lady H. applied model CI on a regression problem and got the value range between `[0.9365995068246098, 0.9388730216990719]`, the sepcified confidence level is 95%, indicating that, if the testing modle performance (R2 score in this case) is within this value range, then there is 95% likelihood that the model performance is true.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/regression_CI.png" width="994" height="107" />
</p>

Similarly, in the classification example, if the testing model performance (balanced accuracy in this case) is within `[0.768882850241546, 0.8991]`, then there is 95% likelihood that the performance is true.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/classification_CI.png" width="993" height="119" />
</p>

🌻 [Check model confidence details >>][9]

The core logic of calculating the model confidence interval can be summarized into 2 steps:

1. Bootstrap samples from the testing data and get the model performance of each sample, collecting them into a list.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/bootstrap.png" width="766" height="79" />
</p>

2. With user specified confidence level and the performance list got from step 1, the confidence interval is calculated as below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/model_ci_code.png" width="1019" height="530" />
</p>

Then, in the luigi pipeline, Lady H. just needs to put this confidence interval core logic into a helper function that can be called by model evaluation task.


🌻 [Check model evaluation config >>][6]

🌻 [Check model evaluation task >>][7]

🌻 [Check model evaluation_helpers >>][8]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][10]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][11]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml#L39
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/data_preprocessing.py
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline1.md#mini-pipelines
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml#L44
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/model_selection.py
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml#L58
[7]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/model_evaluation.py
[8]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/helpers/model_evaluation_helpers.py
[9]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/model_confidence.ipynb
[10]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline4.md
[11]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline2.md
