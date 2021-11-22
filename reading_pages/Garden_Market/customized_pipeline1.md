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

Whenever Lady H. wants to forecast sales or monitor the data drifting, just update the config file and execute `run`, the pipeline will finish the operation automatically.

#### Run Luigi Pipeline

The code came from `run.py`, where users define which task or pipeline to run. In order to make the config parameters accessible to all the luigi tasks, you need to load the config file here and pass it as the parameter of the task instance. At the same time, the task here just need to be the last task of the pipeline, such as `ModelEvaluationTask` in this case, because luigi defines the dependencies between tasks, which allows it to track back to previous tasks.

🌻 [Check run.py code >>][1]

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/code_luigi_run.png" width="452" height="439" />
</p>


#### Task - Data Collection

This is the first task of the forecasting pipeline, the purpose is to merge all the stores' data and the sales data into 1 file and save it for following tasks.

1. In luigi, every task is defined as a class which inherited from `luigi.Task`.
2. Config file is accessible to luigi tasks, since it's been passed as task parameter in `run.py`.
3. Each luigi task has an `output()` function to define the location of the output. This allows luigi to re-run the pipeline from a failed task directly, when there is a task failure during the execution.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/luigi_skip_output.png" width="766" height="79" />
</p>

4. The core logic of a task is defined in its `run()` function.
5. Since the `output()` function doesn't automatically save the output, users need to save the output through `run()` function.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/code_luigi_data_collection.png" width="827" height="518" />
</p>

🌻 [Check data_collection.py code >>][2]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/run.py
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/data_collection.py
