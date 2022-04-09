### Stationary Analysis

When we say a time series is "stationary", it means the time series has constant mean, variation throughout the time. This also means stationary time series is time independent. There are many statistical methods (such as ARIMA) assume the data is stationary, and we often need to convert the data to stationary before applying these statistical methods on the data.

To check whether a time series sequence is stationary, Lady H. often applies 3 methods together:
* <b>Plot the rolling mean and rolling standard deviation of the time series</b>. Ideally, if the rolling mean and rolling standard deviation appear to be constant, it means the data has constant mean and variation along the time, and highly likely to be stationary. But our judgement on being "constant" through visualization can be biased, we need to look into more details.
  * To get a "rolling" value, we often calculate the value within a smaller time window, then moving this window along the time series so that we will get a list of values, such as the rolling mean. This smaller window is known as the "rolling window". 
* <b>Augmented Dickey-Fuller (ADF) Test</b> checks differencing stationary. 
* <b>KPSS Test</b> checks trending stationary. 

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/stationary_2.png" width="1000" height="110" />
</p>

Here's the code to do these tests:
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/stationary_tests.png" width="1000" height="800" />
</p>

We often start to check the stationary of the original time series. Let's take a look at the stationary analysis on our sales data.
* Looking at the rolling mean and rolling standard deviation, some people might think it looks constant while other won't, this is why the visualization only provides an idea and we need to look into more statistical details.
* Looking at ADF test's output, we often compare the "Test Statistic" value with the critical values. When the absolutive "test statistic" value is larger, the data is more likely to be stationary. In this case, we can see, the absolute "test statistic" is 4.387308 and it's larger than the absolute "critical value 1%", so this time series has 99% confidence to be differencing stationary.
* Same idea applies to KPSS test's output. The absolute "test statistic" value is 0.380510, it's larger than the absolute "critical value 10%" but smaller than the "absolute critical value 5%", so this time series has 90% confidence to be trending stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/original_ts_stationary_tests.png" width="1000" height="800" />
</p>

🌻 [Check all the code and details here >>][1]

The above results indicate that our sales data is already stationary, so we don't need to do any extra work. However, there are many real world time series data needs more effort. If you will see the time series is not differencing stationary (failed ADF test), then you can try 1st order differencing and 2nd order differencing on the time series data.

* `1st order differencing = y_i - y_i-1`, and the code can be written as:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_1st_order_diff.png" width="887" height="64" />
</p>

If ADF test still failed after 1st order differencing, you can try 2nd order differencing.
* `2nd order dofferencing = (y_i - y_i-1) - (y_i-1 - y_i-2) = y_i - 2*y_i-1 + y_i-2`, and the code can be written as:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_2nd_order_diff.png" width="881" height="72" />
</p>

Often times, do the differencing till 2nd or 3rd order is enough, if you still can't get a stationary output, then it means differencing is not a preferred method. 

Then what to do? Here comes another method, which is to check residuals' stationary, since residuals is supposed to be time independent. If the residuals is stationary, in some applications, we can simply use residuals as the input of those statistical models.

Let's look at the stationary analysis on the additive decomposition residuals first. It appears to be differencing stationary but not trending stationary. 
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/add_res_stationary_test.png" width="1000" height="800" />
</p>

Now let's do stationary analysis on the multiplicative decomposition residuals, it appears to be both differencing stationary and trending stationary. This has further proved what mentioned before, this time series is better to use multiplicative decomposition. This insight is helpful in deciding the model type should be "additive" or "multiplicative" in forecasting tools such as Prophet. You will see more details in "Time Series Forecasting" section.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_res_stationary_tests.png" width="1000" height="800" />
</p>

🌻 [Check all the code and details here >>][1]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][2]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]

[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/yinyang/past_ts_exploration.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts3.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts1.md
