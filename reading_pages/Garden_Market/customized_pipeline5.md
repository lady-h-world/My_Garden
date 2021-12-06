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




[1]:https://airflow.apache.org/docs/apache-airflow/stable/start/local.html
[2]:https://github.com/lady-h-world/My_Garden/discussions/categories/show-and-tell

