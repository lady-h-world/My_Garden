### Customized ZenML Pipeline

Airflow was designed for workflow instead of data flow, therefore it doesn't support transfering data of different formats across tasks. ZenML is a new tool published in 2020, it can smooth out your airflow user experience with easier setup and flexible data transfering.

#### ZenML Setup

Open your terminal, and follow these steps for the first time setup:

1. `pip install zenml`
2. `pip install google-cloud-bigquery-storage`
3. `sudo python -m pip install google-cloud`
4. Run initialization commands:
* `pip install zenml tensorflow`
* `git init`
* `zenml init`
5. [Follow all the steps here to setup the environment for your airflow DAG][2]

Later to reuse the same environment, only need to run:

* `zenml orchestrator up` to start Airflow
  * If there is an error showing PID file already exists, remove that file and run this command again
* `python [my_DAG.py]` to execute your DAG file
  * After executing this command, it might take a few minutes to find the DAG on http://0.0.0.0:8080 
  * Without http://0.0.0.0:8080, you can still see the pipeline execution results in your local terminal
* `zenml orchestrator down` to shut down Airflow


#### Super Mini ZenML Pipeline

Lady H. built this pipeline with the identical 2 tasks used in the super mini airflow pipeline, data spliting task followed by model training task.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/correct_zenml_flow.png" width="268" height="79" />
</p>

🌻 [Check ZenML super_mini_pipeline.py DAG >>][3]

Comparing with the airflow pipeline, there are 3 major differences in ZenML:

1. User configurable parameters can be defined in a class that's accessible to all the functions. In this example, you can see parameters in `pipeline_config` can be called by both `split_data` step and `train_evaltor` step.
2. Pandas dataframe can be passed across tasks. As you can see, the output of `split_data` step can be the input of step `train_evaltor`.
3. In `DAG = pipeline.run()`, "DAG =" is needed in order to make sure your DAG will appear in Airflow UI http://0.0.0.0:8080 

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/zenml_has_dag.png" width="766" height="79" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/zenml_code.png" width="1000" height="830" />
</p>

ZenML also allows you to inspect each step of the pipeline. For instance, the code below was trying to inspect step `train_evaltor`:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/zenml_inspection.png" width="900" height="200" />
</p>

🌻 [Check ZenML pipeline inspection code >>][3]

The airflow UI of ZenML pipeline looks the same as the airflow pipeline:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/zenml_flow.png" width="418" height="156" />
</p>


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Get your gifts >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]
 


[1]:https://docs.zenml.io/quickstart-guide#install-and-initialize
[2]:https://docs.zenml.io/guides/low-level-api/chapter-7
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/zenml_pipeline/super_mini_pipeline_zenml.py
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline7.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline5.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/zenml_pipeline/pipeline_inspect.py
