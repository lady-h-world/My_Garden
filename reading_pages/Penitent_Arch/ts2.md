### Stationary Analysis on Univariate Time Series
In the field of time series analysis, certain statistical methods, such as ARIMA, assume that the data is stationary. Therefore, it is often necessary to transform the data into a stationary form before applying these methods. A time series is considered "stationary" if it has a constant mean and variance over time. In other words, a stationary time series is not influenced by time but exhibits consistent statistical properties throughout."

To determine whether a time series is stationary, Lady H. typically uses three methods together:

1. <b>Plotting the rolling mean and rolling standard deviation</b>: This involves visualizing the rolling mean and standard deviation over time. If they appear constant, it suggests that the time series has a stable mean and variance, making it likely stationary. 
  * A "rolling" value is calculated using a smaller time window, which is moved along the time series to produce a series of values. This smaller window is referred to as the "rolling window."
  * However, visual judgment of constancy can be subjective. To confirm, more rigorous tests like the ADF and KPSS tests should also be applied.
2. <b>Augmented Dickey-Fuller (ADF) Test</b>: This statistical test checks for differencing stationary by focusing on whether the data is stationary after differencing. 
3. <b>KPSS Test</b>: This test examines whether the time series is stationary around a deterministic trend (trend stationary).

By combining these methods, a more reliable assessment of stationarity can be made.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/stationary_2.png" width="1000" height="110" />
</p>

Here's the code to do these tests:
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/stationary_tests.png" width="1000" height="800" />
</p>

We often start to check the stationary of the original time series. Let's take a look at the stationary analysis on our sales data.
* Looking at the rolling mean and rolling standard deviation, some people might think it looks constant while others won't, this is why the visualization only provides an idea and we need to look into more statistical details.
* Looking at ADF test's output, we often compare the "test statistic" value with the critical values. When the absolutive "test statistic" value is larger, the data is more likely to be stationary. In this case, we can see, the absolute "test statistic" is 4.387308 and it's larger than 3.438893, the absolute "critical value 1%", so this time series has 99% confidence to be differencing stationary.
* Same idea applies to KPSS test's output. The absolute "test statistic" value is 0.380510, it's larger than the absolute "critical value 10%" but smaller than the "absolute critical value 5%", so this time series has 90% confidence to be trending stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/original_ts_stationary_tests.png" width="1000" height="800" />
</p>

🌻 [Check detailed code in Stationary Analysis on Univariate Time Series >>][1]

The above results indicate that our sales data is already stationary, so we don't need to do any extra work. However, there are many real world time series data needs more effort. If you will see the time series is not differencing stationary (failed ADF test), then you can try 1st order differencing on the time series data.

* `1st order differencing = y_i - y_i-1`, and the code can be written as:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_1st_order_diff.png" width="887" height="64" />
</p>

If ADF test still failed after 1st order differencing, you can try 2nd order differencing.
* `2nd order dofferencing = (y_i - y_i-1) - (y_i-1 - y_i-2) = y_i - 2*y_i-1 + y_i-2`, and the code can be written as:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_2nd_order_diff.png" width="881" height="72" />
</p>

Often times, do the differencing till 2nd or 3rd order is enough, if you still can't get a stationary output, it means differencing is not a preferred method. But what to do then?

Here comes another method, which is to check residuals' stationary, since residuals is supposed to be time independent. If the residuals is stationary, in some applications, we can simply use residuals as the input of those statistical models.

Let's look at the stationary analysis on the additive decomposition residuals first. It appears to be differencing stationary but not trending stationary. 
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/add_res_stationary_test.png" width="1000" height="800" />
</p>

Now let's do stationary analysis on the multiplicative decomposition residuals, it appears to be both differencing stationary and trending stationary. This has further proved what mentioned before, this time series is better to use multiplicative decomposition. This insight is helpful in deciding the model type should be "additive" or "multiplicative" when using forecasting tools such as Prophet. You will see more details in "Time Series Forecasting" section.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_res_stationary_tests.png" width="1000" height="800" />
</p>

🌻 [Check detailed code in Stationary Analysis >>][1]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][2]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]

[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/penitent_arch/past_ts_exploration.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts3.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts1.md
