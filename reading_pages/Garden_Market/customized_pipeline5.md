### Customized Airflow Pipeline

Airflow appeared 2 years after Luigi, but it is more popular now because of its scalability, visualization and flexibility in building the workflow.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/airflow_dag.png" width="766" height="79" />
</p>


#### Airflow Setup (Local Mac)

In order to use the Airflow ecosystem, it takes more effort than Luigi setup. Let's share Lady H.'s notes. She has tried both docker setup and local setup on windows and Mac, but found the easiest way was to setup on Mac or Linux locally. Here's how did she run Airflow on her local Mac:

* To install airflow, just need to follow the steps [here][1]
  * Better to take a note of which python version used by your Airflow, so that you can find its site packages later 
* After the installation succeeded, each time
  * Just need to type `airflow standalone` thorugh your terminal, to start Airflow
  * Then you can get access to http://localhost:8080/home, which is the interface of all the DAGs (workflows)
  * To create your own DAG
    * Make sure you have defined AIRFLOW_HOME path during the installation stage, like this `export AIRFLOW_HOME=~/airflow`
    * Find file `airflow.cfg` in your AIRFLOW_HOME folder, in this file, make sure to specify DAGs location like this `dags_folder = ~/airflow/dags`, this is where you will add new DAGs as .py files
    * When creating your DAG in the .py file, make sure to define the `dag_id`, this will be the file name shown in the DAG list
    * To check whether your DAG has been added to the DAG list, type `airflow dags list` through a terminal and you will see all the DAGs, to find DAGs through keywords, you can type `airflow dags list | grep [key_word]`

For example, here're the listed searched DAGs:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/dag_list.png" width="1149" height="48" />
</p>

  * If your DAG isn't shown in the list
    * Check whether all the imported packages were installed in the site packages of the python used by your airflow 
    * Check whether there is any error shown at the top of http://localhost:8080/home, if so, fix it

Once your DAG appeared in the list, you can run it through the localhost interface:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/trigger_airflow_dag.png" width="1000" height="155" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/windows_local_airflow.png" width="766" height="79" />
</p>

If you know how to setup Airflow in other ways, such as using docker or on Windows system, feel free to [show and tell us  details][2]! 💝

#### Super Mini Airflow Pipeline

The learning curve of Airflow is steeper than Luigi, Lady H. decided to use a small amount of super power from the sprouts, to exhibit a super mini Airflow pipeline that convers the key learning points from Airflow.

This super mini pipeline only has 2 steps, data spliting and baseline model training. This whole workflow is a DAG and can be defined within a .py file.

🌻 [Check Airflow super_mini_pipeline.py DAG >>][3]

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/correct_airflow_flow.png" width="326" height="82" />
</p>

At the very beginning of this DAG, you will import different python packages, besides built-in python and Airflow packages, other packages (such as `lightgbm`, `sklearn`) need to be installed in the site packages of the python used by Airflow, otherwise your DAG won't appear in the Airflow DAG list.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/airflow_code1.png" width="448" height="245" />
</p>

Then you need to specifiy the parameters of this DAG. Make sure `dag_id` and `tags` are unique for each DAG.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/airflow_code2.png" width="566" height="49" />
</p>

Now it's the core part where you need to define each step. As we can see, the logic of data spliting and model training is defined in functions, and each step is defined as a `PythonOperator`, whose id is specified in its `task_id` and its `python_callable` matches to the function name of this step, `op_kwargs` stores the (key, value) pairs of the function parameters. 

For example, `split_data_task` has its logic defined in function `split_data()`, therefore, its `python_callable` is "split_data". Meanwhile, function `split_data()` has used confgured parameter `label`, in this case the value of `label` is "species", so `'label':'species'` appears in the `op_kwargs` of this task.

You must also have noticed the `xcom_push()` and `xcom_pull()` used in the code. In this dag, they are used to transfer the data between tasks:

1. The split data was saved through `split_data()` function, `xcom.push()` is used to push the absolute path of the saved data. <b>Remember, Airflow only accepts the absolute path</b>.
2. In order to load the split data, `train_model()` function uses `xcom_pull()` to locate the pushed data through `task_ids` and the `key` specified in `xcom_push()`. In this example, `task_ids` points to the `task_id` of `split_data_task`.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/airflow_code3.png" width="1000" height="600" />
</p>

You might be wondering why not transfer the data directly between Airflow tasks. In this case, it is impossible, because the data output & input is pandas dataframe, Airflow only allows JSON string for data transfer.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/notes/airflow_xcom.png" width="766" height="79" />
</p>

After seeing your DAG appeared in the DAG list, you can run it, and may get error in a certain task, like this:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/airflow_error_flow.png" width="333" height="86" />
</p>

To check the error log, you can click the log of the error task, it will locate the lines of code from where the errors happened.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/airflow_error_log.png" width="1000" height="430" />
</p>

After trials and errors, finally you will get green lights on every task of the DAG 🎉, and through the Tree view, you can see an overview of all the historical attempts.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/airflow_flow.png" width="510" height="126" />
</p>

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]
 

[1]:https://airflow.apache.org/docs/apache-airflow/stable/start/local.html
[2]:https://github.com/lady-h-world/My_Garden/discussions/categories/show-and-tell
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/airflow_pipeline/super_mini_pipeline.py
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline6.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline4.md
