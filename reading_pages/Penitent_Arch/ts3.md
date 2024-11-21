
Lady H. summarized a few more tips to make the data stationary 😉:
* <b>Differencing</b> is often a way to remove trend.
  * Besides 1st, 2nd, 3rd order differencing, you can also try [seasonal differencing][1].
* <b>Log or square root</b> is popular to handle the changing variance.
* <b>Moving average (rolling mean)</b> can smooth the time series by removing random noise.
  * [This example][2] includes both moving average and m*n weighted moving average. 
    * Moving average only applies `rolling()` followed by `mean()` once
    * m*n weighted moving average applies rolling mean on window `m` and then applies on window `n` again. `m` often chooses the periodicity of the seasonal data. This method aims at seasonal smoothing and gives better estimate of the trend.
  * However, moving average can also reduce the variance of the dataset and lead to model overestimation later, be cautious❣️


### Forecastability Analysis

The basic idea of "forecastability" is, <b>when a time series has higher chance of having repetitive patterns, then it's more predictable</b>. We use Approximate Entropy or Sample Entropy to measure this forecastability.

* [Approximate Entropy][3] reflects the likelihood that, similar patterns of observations will NOT be followed by additional similar observations. 😵‍💫 Therefore when Approximate Entropy is lower, this likelihood is lower, indicating the time series tends to have more repetitive patterns and be more predictable.
* [Sample Entropy][4] is a modification of Approximate Entropy, it is data length independent and easier to implement. Meanwhile, Approximate Entropy tends to overestimate the regularity of a time series because of "self-matches", Sample Entropy doesn't have self-matches.

We often use sample entropy rather than approximate entropy in the work.

From previous stationary analysis, we have seen that the original sales data and its multiplicative residuals are both stationary, and in the comparison below, the original time series has lower entropy values and therefore appear to be more forecastable. 

Does this mean, when a time series and its residuals are both stationary, the original time series should be more predictable because it didn't remove those repetitive patterns (such as seasonality)? You are very welcome to discuss your opinions [here][5].

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/forecastability_output.png" width="1000" height="250" />
</p>

🌻 [Check detailed code in Forecastability Analysis][6]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][7]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][8]



  
[1]:https://github.com/PacktPublishing/Practical-Time-Series-Analysis/blob/master/Chapter02/Chapter_2_Seasonal_Differencing.ipynb
[2]:https://github.com/PacktPublishing/Practical-Time-Series-Analysis/blob/master/Chapter02/Chapter_2_Moving_Averages.ipynb
[3]:https://en.wikipedia.org/wiki/Approximate_entropy
[4]:https://en.wikipedia.org/wiki/Sample_entropy
[5]:https://github.com/lady-h-world/My_Garden/discussions/categories/ideas
[6]:https://github.com/lady-h-world/My_Garden/blob/main/code/penitent_arch/past_ts_exploration.ipynb
[7]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts4.md
[8]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts2.md
