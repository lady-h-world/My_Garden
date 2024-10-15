### Customized Luigi Pipeline
To make better business decisions in the garden market, Lady H. needs periodic estimates of perfume sales. Whether it's about determining the quantity of flowers to harvest, planning marketing campaigns, introducing innovations in perfume design, or other matters, having reliable sales estimates is essential. To meet these needs, she developed the Luigi pipeline.

* To forecast future sales, the process often go through `Data Collection -> Feature Engineering -> Data Preprocessing -> Model Selection -> Model Evaluation`, each step is called as a Luigi "task".
* Data drift monitoring involves detecting abnormal changes in the data. The causes of data drift can vary, but they generally reduce forecasting accuracy. When data drift is detected, it's important to investigate further to identify the underlying reasons.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/luigi_pipeline.png" width="520" height="430" />
</p>

In this Luigi pipeline, 

* The configurable parameters for each task are defined in the `config` file. Users can modify these parameters to adjust the pipeline as needed.
* Functions in `helpers` file can be shared across multiple Luigi tasks.
* It is a good practice to include both `unit tests` and `integration tests` for the pipeline. Unit tests evaluate individual functions, while integration tests assess how multiple functions work together. Whenever the pipeline code is modified, these tests help ensure that the changes do not disrupt other parts of the code.

The command center is `run.py`, once Lady H. decides to run either forecasting or data drift monitoring, she just needs to hit the button and the pipeline will be executed automatically.


#### Run Luigi Pipeline
Let's start by reviewing the code in `run.py`. Here, users specify which task or pipeline to execute. To make the configuration parameters accessible to all Luigi tasks, you need to load the config file and pass it as a task parameter, like the `config` shown in the code. Additionally, the task specified here only needs to be the final task of the pipeline, like `ModelEvaluationTask` in this example, this is because Luigi manages task dependencies, it can automatically trace back to previous tasks from the final one.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/code_luigi_run.png" width="452" height="439" />
</p>

🌻 [Check run.py config >>][7]

🌻 [Check run.py code >>][1]


#### Task - Data Collection
This is the first task of the forecasting pipeline, the purpose is to merge all the stores' data and the sales data into 1 file and save it for later tasks.

1. In Luigi, every task is defined as a class that inherits from `luigi.Task`.
2. Config file is accessible to Luigi tasks, since it's been passed as a task parameter in `run.py`.
3. Each Luigi task has an `output()` function to define the location of the output. This is helpful when there is an interruption of the execution, then luigi can re-run from where it stopped.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/luigi_skip_output.png" width="766" height="79" />
</p>

4. Each task has a `run()` function to define the core logic.
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
[7]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml
