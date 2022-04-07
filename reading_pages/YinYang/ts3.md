
Lady H. summarized a few more tips to make the data stationary 😉:
* <b>Differencing</b> is often a way to remove trend.
  * Besides 1st, 2nd, 3rd order differencing, you can also try [seasonal differencing][1].
* <b>Log or square root</b> is popular in handling the changing variance.
* <b>Moving average (rolling mean)</b> can smooth the time series by removing random noise.
  * [This example][2] includes both moving average and m*n weighted moving average. 
    * Moving average only applies `rolling()` followed by `mean()` once
    * m*n weighted moving average applies rolling mean on window `m` and then applies on window `n` again. `m` often choose the periodicity of the seasonal data. This method aims at seasonal smoothing and gives better estimate of the trend.
  * However, moving average also can reduce the variance of the dataset which might lead to model overestimation later, be cautious!


### Forecastability Analysis

The bassic idea of "forecastability" is, if a time series is more complex, then it's more unpredictable.

Now the question is, how do we define "complex"?
  
[1]:https://github.com/PacktPublishing/Practical-Time-Series-Analysis/blob/master/Chapter02/Chapter_2_Seasonal_Differencing.ipynb
[2]:https://github.com/PacktPublishing/Practical-Time-Series-Analysis/blob/master/Chapter02/Chapter_2_Moving_Averages.ipynb
