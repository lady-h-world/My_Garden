
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

The basic idea of "forecastability" is, when a time series has higher chance of having repetitive patterns, then it's more predictable. We use Approximate Entropy or Sample Entropy to measure this forecastability.

* [Approximate Entropy][3] reflects the likelihood that, similar patterns of observations will not be followed by additional similar observations. Therefore when Approximate Entropy is lower, this likelihood is lower and the time series tend to have more repetitive patterns and be more predictable.
* [Sample Entropy][4] is a modification of Approximate Entropy, it is data length independence and easier to implement. Meanwhile, Approximate Entropy tends to overestimate the regularity of a time series because of "self-matches", Sample Entropy doesn't have self-matches.
  
[1]:https://github.com/PacktPublishing/Practical-Time-Series-Analysis/blob/master/Chapter02/Chapter_2_Seasonal_Differencing.ipynb
[2]:https://github.com/PacktPublishing/Practical-Time-Series-Analysis/blob/master/Chapter02/Chapter_2_Moving_Averages.ipynb
[3]:https://en.wikipedia.org/wiki/Approximate_entropy
[4]:https://en.wikipedia.org/wiki/Sample_entropy
