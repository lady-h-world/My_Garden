### Customized Luigi Pipeline

In order to make more profits for the garden, Lady H. often needs an estimation of the perfume sales periodically, in order to make better decisions for the garden market. No matter the decision is about how much flowers to harvest, or what marketing campaign to do, or changes in perfume design, or many other things, having a good sales estimation on time is the key. This is how did this luigi pipeline was born.

Since every time the sales forecasting follows the same process, building this process into an automated pipeline is more efficient.

* To forecast future sales, the process often go through `Data Collection --> Feature Engineering --> Data Preprocessing --> Model Selection --> Model Evaluation`, each step is called as a luigi "task".
* Data Drift Monitoring is to keep an eye on abnormal behaviors in the features or the the forecast target of the data. The causes of the data drifting vary, but all tend to downgrade the forecasting power. Whenever the data drifitng is detected, it is worthy to investigate further to find out reasons.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/luigi_pipeline.png" width="520" height="430" />
</p>

In this Luigi pipeline, 

* The configurable parameters used in each task is specified in the `config` file. Users can change the values of these parameters to adjust the pipeline.
* A `helpers` function can be called by multiple luigi tasks.
* It is a better practice to have `unit tests` and `integration tests` for the pipeline, in order to reduce the chance of breaking the pipeline after a certain code change. Unit tests are testing single functions while integration tests are testing a set of functions together.
