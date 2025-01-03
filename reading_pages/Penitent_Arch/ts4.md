## Explore Multivariate Time Series

Comparing with univariate time series, multivariate time series has more than 1 time dependent variables.


### About the Data

<p>
<img align="left" src="https://github.com/lady-h-world/My_Garden/blob/main/images/lady_heart_manga/grow_sprouts.png" width="204" height="329" />

Our garden features a massive green warehouse housing hundreds of smaller greenhouses, each dedicated to cultivating sprouts of various species. To ensure a healthy growing environment, every greenhouse is continuously monitored. One key metric we track is "occupancy". By analyzing factors such as temperature, humidity, light, CO₂ levels, and humidity ratios, we can accurately predict whether a greenhouse has enough space to accommodate new sprouts.
</p>

Here's the data sample of a greenhouse's data:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multi_ts_sample.png" width="590" height="163" />
</p>

The 5 variables are recorded nearly every minute. When we examine each variable over time, they display distinct trends and seasonal patterns, except for humidity and humidity ratio, which exhibit almost identical curve shapes.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multi_ts_plot1.png" width="1062" height="921" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_ts_plot2.png" width="1069" height="621" />
</p>

Meanwhile, below is the plot of the forecasting target, "Occupancy":

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multi_ts_plot3.png" width="1062" height="310" />
</p>

🌻 [To get multivariate time series data >>][1]



### Stationary Analysis on Multivariate Analysis
Some statistical models require each variable in a multivariate time series to be stationary.

If we do a stationary analysis on our green houses' data, we can see neither humidity nor humidity ratio is differencing stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_ts_stationary_before.png" width="517" height="239" />
</p>

If we apply 1st order differencing here, both humidity and humidity ratio will become stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mults_stationary_after.png" width="685" height="437" />
</p>

🌻 [Check detailed code of Stationary Analysis on Multivariate Time Series >>][2]

Comparing with univariate time series, there is more fun we can explore in multivariate time series, such as exploring the relationships between its variables. Let's go to see more! 😉


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
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/penitent_arch/past_ts_exploration.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts5.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts3.md
