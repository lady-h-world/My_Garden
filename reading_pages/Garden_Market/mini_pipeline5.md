### Mini Pipeline Summary

Comparing the overall performance and user experience, MLJar is a better choice for AutoML mini pipelines.

<p align="center">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/tb4.2.png" width="730" height="422" />
</p>

Although we have different AutoML mini pipelines to choose, they are still working like a blackbox that users can't fully control all the settings and the process. In the industry environment, companies often have more complex requirements on their machine learning pipelines, being able to customize the pipeline is crucial.

## Customized Pipelines

Now it's time to show how can we build customized pipelines in python.

* [Luigi][1] allows you to build every stage of a machine learning pipeline, users have the ultimate freedom to customize the operations of each stage.
* [Airflow][2] is a platform to programmatically author, schedule, and monitor workflows.
* [ZenML][3] saves your efforts when building Airflow based machine learning pipelines.

To manage the business in this garden, Lady H. only needs to build a small scale pipeline, Luigi is enough to use. Airflow supports larger scale pipelines but comparing with Luigi, it's a bit more difficult to learn. To make your tour more fun, Lady H. built 2 super mini pipelines using Airflow and ZenML, but covered the key components, might be a good starting point for your learning!

Time to dive into details!

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<< Looking back][5]
 



[1]:https://github.com/spotify/luigi
[2]:https://github.com/apache/airflow
[3]:https://github.com/zenml-io/zenml
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/customized_pipeline1.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline4.md



