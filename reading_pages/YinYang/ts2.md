### Stationary Analysis

When we say a time series is "stationary", it means the time series has constant mean, variation throughout the time. This is also means stationary time series is time independent. There are many statistical methods applied on time series assume the data is stationary, therefore we often have to convert the data to stationary before applying these statistical methods.

To check whether a sequence data is stationary, Lady H. often applies 3 methods at the same time:
* <b>Plot the rolling mean and rolling standard deviation of the time series input</b>. Ideally, if the rolling mean and rolling standard deviation appear to be constant, it means the data has constant mean and variation along the time, and highly likely to be stationary. But the visualization only provides an idea, we need to look into more details.
* <b>Augmented Dickey-Fuller (ADF) Test</b> checks differencing stationary. The idea is, the time series will be transformed to stationary through differencing. This method only checks whether the rolling mean changes.
* <b>KPSS Test</b> checks trending stationary. The idea is, by removing the trend, the time series will become stationary.

Here's the code to do these tests:
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/stationary_tests.png" width="1000" height="800" />
</p>

We often start to check the stationary of the original time series. Let's take a look at the stationary analysis on our sales data.
* Looking at the rolling mean and rolling standard deviation, we can't say they are constant, this is why the visualization only provides an idea and we need to look into more statistical details.
* Looking at ADF test's output, we often compare the "Test Statistic" value with the critical values. When the absolutive test statistic value is larger the data is more likely to be stationary. In this case, we can see, the absolute test statistics is 4.387308 and it's larger than the absolute critical value 1%, so this time series has 99% confidence to be differencing stationary.
* Same idea apply to KPSS test's output. The absolute test statistic value is 0.380510, it's larger than the absolute critical value 10% but smaller than the absolute critical value 5%, so this time series has 90% confidence to be trending stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/original_ts_stationary_tests.png" width="1000" height="800" />
</p>

🌻 [Check all the code and details here >>][1]

Our sales data is stationary, we don't need to do more work to make it stationary. However, there are many real world time series data needs some extra work. If you will see the time series is not differencing stationary (failed ADF test), then you can try 1st order differencing and even 2nd order differencing on the time series data.

* `1st order differencing = y_i - y_i-1`, and the code can be written as:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_1st_order_diff.png" width="887" height="64" />
</p>

* `2nd order dofferencing = (y_i - y_i-1) - (y_i-1 - y_i-2) = y_i - 2*y_i-1 + y_i-2`, and the code can be written as:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_2nd_order_diff.png" width="881" height="72" />
</p>

Often times, do the differencing till 2nd or 3rd is enough, if you still can't get a stationary output, then it means differencing is not a preferred method. Then what to do? Here comes another method, which is to check residuals' stationary, since it has removed trend and saesoanlity and it's supposed to be time independent. If the residuals is stationary, in some applications, we can simply use residuals as the input of those statistical models.

Let's look at the stationary analysis on the residuals came from the additive decomposition, it's differencing stationary but not trending stationary. 
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/add_res_stationary_test.png" width="1000" height="800" />
</p>

As mentioned before, our sales data is better for multiplicative decomposition. If we do tationary analysis on the multiplicative decomposition residuals, we will see it's both differencing stationary and trending stationary.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/mul_res_stationary_tests.png" width="1000" height="800" />
</p>

🌻 [Check all the code and details here >>][1]

[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/yinyang/past_ts_exploration.ipynb
