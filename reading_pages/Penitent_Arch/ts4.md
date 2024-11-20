## Explore Multivariate Time Series

Comparing with univariate time series, multivariate time series has more than 1 time dependent variables.

### About the Data

<p>
<img align="left" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/grow_sprouts.png" width="204" height="329" />

Have you ever wonder where do we store so many sprouts for garden visitors? We have a giant green warehouse, which contains hundreds of green houses to grow sprouts! In order to maintain a healthy growing environment, every green house is monitored all the time. One of the monitoring metrics is "occupancy", by checking the temperature, humidity, light, CO2 and humidity ratio, we can forecast whether a green house has enough space for new sprouts.
</p>

Here's the data sample of 1 green house's data:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multi_ts_sample.png" width="590" height="163" />
</p>

The 5 variables are recorded almost every 1 minute. If we take a look at each variable throughout the time, different variables present different trend and seasonality patterns, except humidity and humidity ratio are having almost the same curve shapes.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multi_ts_plot1.png" width="1062" height="921" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_ts_plot2.png" width="1069" height="621" />
</p>

We won't dive into the forecasting target "Occupancy", but let's still take a peek at its overall appearance:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multi_ts_plot3.png" width="1062" height="310" />
</p>

🌻 [To get multivariate time series data >>][1]



### Stationary Analysis on Multivariate Analysis

Some statistical models require each variable in a multivariate time series to be stationary.

If we do a stationary analysis on our green houses' data, we can see both humidity and humidity ratio are not differencing stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_ts_stationary_before.png" width="517" height="239" />
</p>

To make the 2 variables to be differencing stationary, we often start with 1st order differencing on the variables, and luckily, now we get every variable stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mults_stationary_after.png" width="685" height="437" />
</p>

🌻 [Check detailed code in Stationary Analysis on Multivariate Time Series >>][2]

Comparing with univariate time series, there is more fun we can explore in multivariate time series, such as exploring the relationships between its variables. Keep following Chansey Butterflies to see how can we disclose these relationships! 😉


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][4]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_multivariate_ts.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/yinyang/past_ts_exploration.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts5.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts3.md
