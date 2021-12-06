### Customized ZenML Pipeline

Airflow was designed for workflow instead of data flow, therefore it doesn't support transfering data in different formats across tasks. ZenML is a new tool published in 2020, it can smooth out your Airflow user experience with easier setup and flexible data transfering.

#### ZenML Setup

Open your terminal, and follow these steps for the FIRST TIME setup:

1. `pip install zenml`
2. `pip install google-cloud-bigquery-storage`
3. `sudo python -m pip install google-cloud`
4. Run initialization commands [here][1]
  4.1. `pip install zenml tensorflow`
  4.2. `git init`
  4.3. `zenml init`
5. [Follow all the steps here to setup the environment for your Airflow DAG][2]

Later to reuse the same environment, just need to run

* `zenml orchestrator up` to start Airflow
  * If there is an error showing PID file already exists, remove that file before executing this command
* `python [my_DAG.py]` ro execute the DAG file
* `zenml orchestrator down` to shut down Airflow


#### Super Mini ZenML Pipeline




[1]:https://docs.zenml.io/quickstart-guide#install-and-initialize
[2]:https://docs.zenml.io/guides/low-level-api/chapter-7
