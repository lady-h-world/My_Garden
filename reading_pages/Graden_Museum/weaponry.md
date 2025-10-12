## Weaponry

The tools displayed here are either <b>new promising tools</b> that you got no chance to see during your visit, or <b>popular tools with weaknesses</b> that Lady H. chose not to use in daily work.


### More on Data Exploration
* [Predictive Power Score][5] 
  * Besides the [Granger Causality you have seen here][6], later Lady H. learned [PPS (Predictive Power Score)][7], a method detects asymmetric correlation might also be helpful in telling "assumed causality". It helps finding which variable helps predict another dependent/independent variable better.


### More on AIML Models
* [TabM][11]: Advancing Tabular Deep Learning With Parameter-Efficient Ensembling
  * [Comparison with MLP and traditional boosting models][12]


### More on AuotML
* [MLflow][10]
  * It's a famous AutoML tool, but Lady H. didn't use it in the work is because it can't compare model performance viusally when she had done multiple experiments. 


### More on Time Series
* [AutoTS][1]
  * AutoML for Time Series 
* [Darts][2]
  * Time Series Forecasting and Anomaly Detection


### More on Causal Discovery
* We have explored [granger-causality][16] for potential influence. There is [LiNGAM][15] for causal discovery, and [this explains how does it work][14].


### More on Hyperparameter Tuning (HPO)
* [Ray Tune][4]
  * An HPO tool built upon Ray project to speed up HPO work, and has integrated many popular libraries, such as Optuna, FLAML, Keras, Scikit-learn, XgBoost, etc.
  * Ray is famous for its ability of scaling up AI applications, however when using Ray-Tune, it takes long time to load its final output, and if you run it on Windows, might get [this type of error][8].


### More on Prompt Optimization
* [AdalFlow][13]
  * It might have better prompt performance and better control on prompt template than DsPy. Lady H. will wait a bit before using it because it's very new when Lady H. just finihsed DsPy pipeline 


### More on Model Monitoring
* [Predict MAE or MSE of Regression Model][3]


### More on Synthetic Data Generation
* [Tabula][9] leverages language model structures to generate tabular synthetic data. Are you able to run its code?


[1]:https://github.com/winedarksea/AutoTS
[2]:https://github.com/unit8co/darts
[3]:https://towardsdatascience.com/you-cant-predict-the-errors-of-your-model-or-can-you-1a2e4a1f38a0
[4]:https://docs.ray.io/en/latest/tune/index.html
[5]:https://github.com/8080labs/ppscore
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts6.md
[7]:https://github.com/8080labs/ppscore
[8]:https://stackoverflow.com/questions/77101618/ray-tune-fit-function-file-not-found-on-windows
[9]:https://github.com/zhao-zilong/Tabula/tree/main
[10]:https://github.com/mlflow/mlflow
[11]:https://github.com/yandex-research/tabm
[12]:https://www.linkedin.com/posts/avi-chawla_we-now-have-a-new-candidate-for-ensembles-activity-7337403019795275776--yMt?utm_source=share&utm_medium=member_desktop&rcm=ACoAABUa5xMBAWvx7L2IKhfsBuLjhTEWJhTYoNk
[13]:https://github.com/SylphAI-Inc/AdalFlow
[14]:https://blog-en.fltech.dev/entry/2024/09/12/ecmlpkdd2024-layeredlingam-en
[15]:https://github.com/cdt15/lingam
[16]:https://lady-h-s-applied-data-science-wo.gitbook.io/applied-data-science-in-my-garden/penitent-arch/time-series-data-exploration#granger-causality
