### Customized ZenML Pipeline
Airflow is designed for workflow management rather than data flow, so it doesn't support transferring data between tasks. ZenML, introduced in 2020, enhances the Airflow experience with easier setup and more flexible data transfer capabilities.


#### ZenML Setup
Open your terminal, and follow these steps for the first time setup:

1. `pip install zenml`
2. `pip install google-cloud-bigquery-storage`
3. `sudo python -m pip install google-cloud`
4. Run initialization commands:
* `pip install zenml tensorflow`
* `git init`
* `zenml init`
5. [Follow all the steps here to set up the environment for your Airflow DAG][2]


#### Simple ZenML Airflow Pipeline
Lady H. built this pipeline with the identical 2 tasks used in the simple Airflow pipeline, data spliting task followed by model training task.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/correct_zenml_flow.png" width="268" height="79" />
</p>

🌻 [Check Simple ZenML Airflow DAG >>][3]

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

🌻 [Check ZenML pipeline inspection code >>][6]

The user interface looks the same as the Airflow pipeline:

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/zenml_flow.png" width="418" height="156" />
</p>


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Get your gift >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]
 

[1]:https://docs.zenml.io/quickstart-guide#install-and-initialize
[2]:https://docs.zenml.io/stack-components/orchestrators/airflow
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/zenml_pipeline/super_mini_pipeline_zenml.py
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline7.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline5.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/zenml_pipeline/pipeline_inspect.py
