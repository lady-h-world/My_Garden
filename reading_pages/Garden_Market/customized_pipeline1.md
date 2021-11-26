### Customized Luigi Pipeline

In order to make more profits for the garden, Lady H. often needs an estimation of the perfume sales periodically, in order to make better decisions for the garden market. No matter the decision is about how much flowers to harvest, or what marketing campaign to do, or innovations in perfume design, or many other things, having a good sales estimation on time is the key. This is how did this luigi pipeline was born.

Since every time the sales forecasting follows the same process, building this process into an automated pipeline is more efficient.

* To forecast future sales, the process often go through `Data Collection --> Feature Engineering --> Data Preprocessing --> Model Selection --> Model Evaluation`, each step is called as a luigi "task".
* Data Drift Monitoring is to keep an eye on abnormal behaviors in the features or in the forecast target of the data. The cause of the data drifting varis, but all tend to downgrade the forecasting power. Whenever the data drifitng is detected, it is worthy to investigate further to find out reasons.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/luigi_pipeline.png" width="520" height="430" />
</p>

In this Luigi pipeline, 

* The configurable parameters used in each task is specified in the `config` file. Users can change the values of these parameters to adjust the pipeline.
* Each `helpers` function can be called by multiple luigi tasks.
* It is a better practice to have `unit tests` and `integration tests` for the pipeline. Unit tests are testing single functions while integration tests are testing a set of functions together. Whenever there is a code change in the pipeline, these tests can examine whether the change will break other parts of the code.

The command center is `run.py`, once Lady H. decides to run either forecasting or data drift monitoring, she just needs to hit the button here and the whole pipeline will be executed automatically.

#### Run Luigi Pipeline

This is `run.py`, where users define which task or pipeline to run. In order to make the config parameters accessible to all the luigi tasks, you need to load the config file here and pass it as the parameter of the task instance. At the same time, the task here just need to be the last task of the pipeline, such as `ModelEvaluationTask` in this case, because luigi defines the dependencies between tasks, which allows it to trace back to previous tasks.

🌻 [Check run.py config >>][5]

🌻 [Check run.py code >>][1]

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/code_luigi_run.png" width="452" height="439" />
</p>


#### Task - Data Collection

This is the first task of the forecasting pipeline, the purpose is to merge all the stores' data and the sales data into 1 file and save it for later tasks.

1. In luigi, every task is defined as a class that inherits from `luigi.Task`.
2. Config file is accessible to luigi tasks, since it's been passed as a task parameter in `run.py`.
3. Each luigi task has an `output()` function to define the location of the output. This is helpful when there is an interruption of the execution, then luigi can re-run from where it stopped.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/luigi_skip_output.png" width="766" height="79" />
</p>

4. The core logic of a task is defined in its `run()` function.
5. Since the `output()` function doesn't automatically save the output, users need to save the output through `run()` function.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/code_luigi_data_collection.png" width="827" height="518" />
</p>

🌻 [Check data_collection config >>][5]

🌻 [Check data_collection.py code >>][2]

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][4]
 

[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/run.py
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/data_collection.py
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline2.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline5.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml#L9
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml#L6-L7
