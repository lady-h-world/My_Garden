#### Task Data Drift Monitoring

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/miss_mooncake.png" width="200" height="250" /></p>

Lady H.'s first full time data scientist job was in a financial fraud detection company. One of her clients was a giant bank. Every 2 months, that client would send her new data for fraud analysis. It was 5pm in a December when the office was almost empty, most of her colleagues were on vacation or returned back home earlier. Lady H. was planning to quickly finish the client's fraud report using her trained model, then go home.

But the new data gave her a very different fraud detection rate, a rate much lower than usual. "Why this happened? It looks so strange and the client will definitely ask why. I have to invetigate", Lady H. thought. Later, she figured it out, the client sent her the wrong data and caused the problem. 

This is a typical story of data drifting.

##### About Data Drifting

Data drifting is not always caused by mistakes, there can be other causes too. But regardless of the causes, the changes in the data can lower the forecasting power of the trained model. When this happened, data scientists need to investigate the causes and sometimes even need to retrain the model.

There are 2 main types of data drifting:

* Concept Drift: the statistical properties of the forecasting target have changed.
* Covariate Drift: the statistical properties of the input features have changed.

##### Suggested Data Drifting Detection Methods

There are many statistical methods to detect data drifting, some need to satisfy certain assumptions and weren't effective, some python built-in libraries set constraints on the data input. After trying out different methods, Lady H. suggested 2 methods she often uses:

* To detect concept drift: use PSI (Population Stability Index)
* To detect covariate drift: use a machine learning model and feature importance

Let's look into the details.

##### PSI to Detect Concept Drift

`PSI = sum((actual_percentage - expected_percentage) * ln(actual_percentage / expected_percentage))`

When applying PSI, you need 2 sets of target data, "actual" can be the latest target data, "expected" can be the old target data that didn't have data drifting. PSI will binning the numerical target values, and the "percentage" in the formula indicates how much percent each bin occupies. The general purpose of PSI is to find the overall percentage change, when comparing the 2 sets of data.

🌻 [Check PSI python implementation >>][2] [Reference][3]

* `PSI < 0.1`: no significant population change
* `0.1 <= PSI < 0.2`: moderate population change
* `PSI >= 0.2`: significant population change

With PSI, Lady H. applied it to 2 sets of taregts that didn't have concept drift, and we can see PSI lower than 0.1 and the distributions between the 2 target sets are similar to each other.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/psi_normal.png" width="911" height="333" />
</p>

Then she applied it to another pair from targets where one of the data set drifted from the other, and we can see the difference in the distributions and the PSI value indicates a significant change.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/psi_drift.png" width="912" height="336" />
</p>

🌻 [Check concept drift detection experiments >>][4]

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/classification_target_drift.png" width="766" height="79" />
</p>

In Lady H.'s experiments, she only did the concept drift detection for regression problems. For classification targets, she often compares the distributions first, since many problems are binary classification and the distribution comparison is straightforward. For multi-class classification, PSI also works because it's built upon binning idea, [so you can apply PSI formula without binning the data][5].



[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/data_drift_detection.ipynb
[2]:https://github.com/mwburke/population-stability-index/blob/master/psi.py
[3]:https://github.com/mwburke/population-stability-index
[4]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/data_drift_detection.ipynb
[5]:https://github.com/mwburke/population-stability-index/blob/master/psi.py#L50-L67
