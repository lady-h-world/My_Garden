#### Task Data Drift Monitoring

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/work_late.png" width="243" height="246" /></p>

Lady H.'s first full time data scientist job was in a financial fraud detection company. One of her clients was a giant bank. Every 2 months, that client would send her new data for fraud analysis. It was a December afternoon when the office was almost empty at 5 pm, most of her colleagues were on vacation or left earlier. Lady H. was planning to quickly finish the client's fraud report using her trained model, then go home.

But the new data gave her a very different fraud detection rate, a rate much lower than usual. "Why this happened? It looks so strange and the client will definitely ask why. I have to investigate", Lady H. thought. Later, she figured it out, the client sent her the wrong data and caused the problem. 

This is a typical story of data drifting.

##### About Data Drifting

Data drifting is not always caused by mistakes, there can be other reasons too. But regardless of the causes, the changes in the data can lower the forecasting power of the trained model. When this happened, data scientists need to investigate the causes and sometimes even need to retrain the model.

There are 2 main types of data drifting:

* `Concept Drift` means, the statistical properties of the <b>forecasting target</b> have changed.
* `Covariate Drift` means, the statistical properties of the <b>input features</b> have changed.

##### Suggested Data Drifting Detection Methods

There are many statistical methods to detect data drifting, some need to satisfy certain assumptions, some aren't as effective as expected, some python built-in libraries set constraints on the data input. After trying out different methods, Lady H. suggested 2 methods she often uses:

* To detect concept drift: use PSI (Population Stability Index).
* To detect covariate drift: use a machine learning model and feature importance.

Let's look into the details.

##### PSI to Detect Concept Drift

`PSI = sum((actual_percentage_i - expected_percentage_i) * ln(actual_percentage_i / expected_percentage_i))`

When applying PSI to detect concept drift, you need 2 sets of target data, "actual" can be the latest target data, "expected" can be the older target data that didn't have data drifting. PSI will binning the numerical target values and "_i" means the ith bin, the "percentage" in the formula indicates how many percent each bin occupies in the population. The general purpose of PSI is to get the overall percentage change, when comparing 2 sets of data.

🌻 [Check PSI python implementation >>][2] ([Reference][3])

* `PSI < 0.1`: no significant population change
* `0.1 <= PSI < 0.2`: moderate population change
* `PSI >= 0.2`: significant population change

With PSI, Lady H. applied it to 2 sets of taregts that didn't have concept drift, we can see PSI is lower than 0.1 and the distributions of the 2 target sets are similar to each other.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/psi_normal.png" width="911" height="333" />
</p>

Then she applied it to another pair of targets, that one of the data set drifted from the other, and we can see the difference in the distributions and the PSI value all indicate a significant change.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/psi_drift.png" width="912" height="336" />
</p>

🌻 [Check concept drift detection experiments >>][4]

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/classification_target_drift.png" width="766" height="79" />
</p>

In Lady H.'s experiments, she only did the concept drift detection for regression problems. For classification targets, she often compares the distributions first, since many problems are binary classification and the distribution comparison is straightforward. For multi-class classification, PSI also works because it's built upon binning idea, [so you can apply PSI formula without binning the data][5].

##### Machine Learning to Detect Covariate Drift

Drifting in features can bring up more complex math discussions, and many statistical methods can only be used in a limited scope. Lady H. has found a simple and effective method to detect covariate drift, that is to mix the old and the new data sets together, labeling them as the "old" or the "new" data, then use a machine learning model to do the forecast. If the forecasting result is showing high accuracy, then it means there is covariate drift since the dataset can tell obvious differences between the old and the new data. To figure out which features might caused the drift, we can check the feature importance.

The code is as simple as using a LGBM model to train the data with cross validation, and check the average forecasting performance:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/covariate_drift_detection_code.png" width="919" height="323" />
</p>

When applying this method on the dataset without covariate drift, the forecasting is showing accuracy near 0.5, similar to random guessing. This means the model can't tell any difference between the new and the old data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/covariate_drift_normal.png" width="882" height="417" />
</p>

And if we look at the forecasting results in a dataset with feature "Store" changed significantly, the high forecasting accuracy sends a warning sign of the feature differences between the new and the old data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/covariate_drift_drift.png" width="888" height="418" />
</p>

And if we look at the feature importance from this trained model, it points to feature "Store", indicating that this feature plays an important role in differentiating the old and the new data. So we can assume this feature contributes to the covariate drift.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/drifted_feature.png" width="794" height="362" />
</p>

🌻 [Check covariate drift detection experiments >>][4]

##### Data Drift Monitoring Pipeline Code

As we saw in `run.py`, Task Data Drift Moniroting is independent from the model pipeline, it can be executed at any time. In the industry, you can also schdule a periodical data monitoring job and display the output on a dashboard, or send alerts whenever something unexpected happened.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/run_monitoring.png" width="453" height="440" />
</p>

The pipeline code has helpers functions to calculate PSI for concept drifting and use LGBM for covariate drifting. Then in the task class, just need to call these helpers functions.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/task_drift_monitoring_code.png" width="1000" height="804" />
</p>

🌻 [Check data drift monitoring config >>][8]

🌻 [Check data drift monitoring task >>][9]

🌻 [Check data drift monitoring helpers >>][10]


#### Tests

It is a better practice to have unit tests and integration tests in the pipeline, so that after each code change, you can test whether any where has been broken by the changes. In some companies, the input data for the tests can be mockup data, but Lady H. strongly recommends to use client's real data for the pipeline's tests, if possible. Because this helps debugging for the real clients' use cases earlier, and it's more flexible for scalability tests. If you want to cover all the edge cases in the data, then simulating a larger set of mockup data to be used throughout the pipeline is also a good practice.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/scalability_test.png" width="766" height="79" />
</p>

🌻 [Check unit tests >>][12]

🌻 [Check integration tests >>][11]

Unit tests are used to test single functions, while each integration test can be used to test each luigi task in this pipeline.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][6]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][7]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/data_drift_detection.ipynb
[2]:https://github.com/mwburke/population-stability-index/blob/master/psi.py
[3]:https://github.com/mwburke/population-stability-index
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/data_drift_detection.ipynb
[5]:https://github.com/mwburke/population-stability-index/blob/master/psi.py#L50-L67
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline5.md
[7]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline3.md
[8]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml#L61
[9]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/data_drift_monitoring.py
[10]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/helpers/data_drift_monitoring_helpers.py
[11]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/tests/integration_test.py
[12]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/tests/unit_tests.py
