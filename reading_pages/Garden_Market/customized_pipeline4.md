#### Task Data Drift Monitoring

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/work_late.png" width="323" height="326" /></p>

Lady H.'s first full-time role as a data scientist was with a financial fraud detection company, where one of her main clients was a giant bank. Every two months, the client sent her new data for fraud analysis.

One December afternoon, the office was nearly empty by 5 p.m., with most of her colleagues either on vacation or having left early. Determined to wrap up the client's fraud report using her trained model, Lady H. planned to finish quickly and head home.

But as she processed the new data, the fraud detection rate came out much lower than usual. "Why is this happening? This looks strange—I need to dig deeper," she thought. After some investigation, she realized the problem: the client had accidentally sent the wrong dataset, causing the unexpected result.

This is just one of many stories about data drift.


##### About Data Drift
Data drift isn’t always the result of mistakes—there can be other reasons as well. Regardless of the cause, changes in the data can reduce the predictive power of a trained model. When this happens, data scientists must investigate the underlying causes and may even need to retrain the model.

There are 2 main types of data drift:

* `Concept Drift` means, the statistical properties of the <b>forecasting target</b> have changed.
* `Covariate Drift` means, the statistical properties of the <b>input features</b> have changed.


##### Suggested Data Drift Detection Methods
There are many statistical methods to detect data drift, some need to satisfy certain assumptions, some aren't as effective as expected, some python built-in libraries set constraints on the data input. After trying out different methods, Lady H. suggested 2 methods she often uses:

* To detect concept drift: use PSI (Population Stability Index).
* To detect covariate drift: use a machine learning model and feature importance.

Let's look into the details.


##### PSI to Detect Concept Drift
`PSI = sum((actual_percentage_i - expected_percentage_i) * ln(actual_percentage_i / expected_percentage_i))`

When using PSI to detect concept drift, you need two sets of target data: the "actual" data, which represents the latest target values, and the "expected" data, which corresponds to an older set without any drift. PSI works by binning the numerical target values, where "_i" refers to the i-th bin. The "percentage" in the formula reflects the proportion each bin occupies within the total population.

🌻 [Check PSI python implementation >>][2]

The main goal of PSI is to measure the overall percentage change between two datasets, helping to identify potential drift.

* `PSI < 0.1`: no significant population change
* `0.1 <= PSI < 0.2`: moderate population change
* `PSI >= 0.2`: significant population change

Using PSI, Lady H. applied it to two target sets without concept drift. The PSI value is below 0.1, indicating that the distributions of the two target sets are similar."

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/psi_normal.png" width="911" height="333" />
</p>

She then applied it to another pair of target sets, where one dataset had drifted from the other. The difference in their distributions and the PSI value both indicate a significant change.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/psi_drift.png" width="912" height="336" />
</p>

🌻 [Check concept drift detection experiments >>][4]

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/classification_target_drift.png" width="766" height="79" />
</p>

In Lady H.'s experiments, she focused on detecting concept drift for regression problems. For classification targets, she typically compares the distributions first, as many are binary classification tasks, making distribution comparisons straightforward. For multi-class classification, PSI is also effective since it relies on the concept of binning, allowing the PSI formula to be applied directly without additional binning.


##### Machine Learning to Detect Covariate Drift
Feature drift can lead to more complex mathematical discussions, and many statistical methods have limited applicability. Lady H. discovered a simple yet effective approach for detecting covariate drift: combining the old and new datasets and labeling them as "old" or "new". A machine learning model is then used to predict these labels. If the model achieves high accuracy, it indicates covariate drift, as the dataset reveals clear differences between the two datasets. To identify the features caused the drift, we can analyze the feature importance.

The code is as simple as training the data with an LGBM model using cross-validation and evaluating the average forecasting performance:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/covariate_drift_detection_code.png" width="919" height="323" />
</p>

When applying this method on the dataset without covariate drift, the forecasting is showing accuracy near 0.5, similar to random guessing. This means the model can't tell any difference between the new and the old data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/covariate_drift_normal.png" width="882" height="417" />
</p>

Examining the feature importance from the trained model highlights "Store" as a key feature, suggesting it plays a significant role in distinguishing between the old and new data. This implies that "Store" contributes to the covariate drift.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/covariate_drift_drift.png" width="888" height="418" />
</p>

And if we look at the feature importance from this trained model, it points to feature "Store", indicating that this feature plays an important role in differentiating the old and the new data. So we can assume this feature contributes to the covariate drift.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/drifted_feature.png" width="794" height="362" />
</p>

🌻 [Check covariate drift detection experiments >>][4]

##### Data Drift Monitoring Pipeline Code
As we saw in `run.py`, the Task Data Drift Monitoring operates independently of the model pipeline and can be executed at any time. In practice, you can schedule periodic data monitoring jobs, display the results on a dashboard, or trigger alerts whenever unexpected changes occur.

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
It's good practice to include both unit and integration tests in the pipeline to ensure that code changes don't break any functionality. Some companies use mockup data for testing, but Lady H. strongly recommends using real client data whenever possible. This makes it easier to debug real-world use cases early and provides more flexibility for scalability testing. Mockup data is useful for covering all edge cases, and creating a dataset that captures all potential scenarios throughout the pipeline is also a good approach.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/scalability_test.png" width="766" height="79" />
</p>

🌻 [Check unit tests >>][12]

🌻 [Check integration tests >>][11]

Unit tests are used to test single functions, while each integration test can be used to test each Luigi task in this pipeline.


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
