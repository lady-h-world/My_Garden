## Explore Multivariate Time Series

Comparing with univariate time series, multivariate time series has more than 1 time dependent variables.

### About the Data

Have you ever wonder where do we store so many sprouts for garden visitors? We have a giant green warehouse, which contains thousands of green rooms to grow sprouts! In order to maintain a healthy growing environment, every green room is monitored all the time. One of the monitoring metric is "occupancy", by checking the temperature, humidity, light, CO2 and humidity ratio, we can forecast whether a room has enough occupacy for new sprouts.

Here's the data sample of 1 green room's data:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multi_ts_sample.png" width="590" height="163" />
</p>

The 5 variables are recorded almost every 1 minute. If we take a look at each variable throughout the time, different variables present different trend and seasonality patterns, while humidity and humidity ratio are having almost the same curve shapes.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multi_ts_plot1.png" width="1062" height="921" />
</p>

Occupancy is not the variable we will dive into, but let's still take a peek at its overall appearance:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_ts_plot2.png" width="1069" height="621" />
</p>

🌻 [To get multivariate time series data >>][1]



### Stationary Analysis on Multivariate Analysis

Some statistical models require each variable in a multivariate time series to be stationary.

If we do a stationary analysis on our green room's data, we can see both humidity and humidity ratio are not differencing stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_ts_stationary_before.png" width="517" height="239" />
</p>

To make the 2 variables to be differencing stationary, we often start with 1st order differencing on the variables, and luckily, now we get every variable to be stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mults_stationary_after.png" width="685" height="437" />
</p>

🌻 [Check detailed code in Stationary Analysis on Multivariate Time Series >>][2]

Comparing with univariate time series, there is more fun we can explore in multivariate time series, that is the relationships between its variables. Keep following Chansey Butterflies to see how can we disclose these relationships! 😉


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
