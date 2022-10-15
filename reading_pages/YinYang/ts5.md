### Cointegration Test

As we have already known, a multivariate time series has more than one time dependent variables, each variable is a time series. Cointegration test checks the significant connections between 2 or more time series. When multiple time series are cointegrated, it means they have a long term, statistically significant relationship. Because cointegration is the premise of some models, such as Vector Autoregression (VAR), we need to do cointegration test before applying these models.

Then what does "cointegration" mean, statistically? We need to understand what is the "order of integration (d)" first.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/order_of_integration.png" width="766" height="79" />
</p>

When you have two or more time series, and there exists a linear combination of them that has an order of integration (d) lower than that of each individual series, then the collection of these series is said to be cointegrated.

We often use Johansen test as cointegration test. It's based on the estimation of expected maximization through maximum likelihood, under various assumptions about the trend and intercepting parameters of the data. Python `statsmodels` provides built-in `coint_johansen`. 

<i>Note: The input data here is already converted to stationary from previous stationary analysis step!</i>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/cointegration_test.png" width="829" height="718" />
</p>

The conintegration test output indicates that temperature, humidity, light and CO2 are cointegrated, that is to say, we can use these variables together in a model like VAR (more details coming in multivariate time series outlier detection). It is also safe to throw away "humidity ratio" because of its high correlation with variable "humidity".

🌻 [Check detailed code for Integration Test >>][3]

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][1]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][2]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts6.md
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts4.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/yinyang/past_ts_exploration.ipynb




