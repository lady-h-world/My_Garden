# Time Series Data Exploration
Unlike traditional datasets, time series data contains hidden temporal patterns, offering a unique and engaging experience during data exploration. Let’s explore some popular and practical methods!


## Explore Univariate Time Series

### About the Data

Our perfume sales data is a classic example of time series data. Specifically, it is a univariate time series, meaning there is only one time-dependent variable (in this case, `Daily_Sales`). Take a look at the example below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_sales_exp.png" width="170" height="184" />
</p>

Here’s the sales plot. As you can see, the data shows a clear, recurring pattern of ups and downs:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/daily_sales_plot.png" width="1092" height="293" />
</p>

🌻 [To get sales time series data >>][1]


### Time Series Components

A time series sequence has multiple components:
* <b>Trend</b>: It indicates the overall direction of the time series sequence, such as upward, downward or no trend.
* <b>Seasonality</b>: It refers to the tendency of going up and down in a consistent frequency. It's repetitive and calendar related.
* <b>Cycle</b>: Similar to seasonality, it's also recurring but with inconsistent frequencies. It's less frequent than seasonality fluctuations, and the time span of a cyclical change can be longer than a seasonal change.
  * Cycle is not time dependent and can only be explained by exogenous variables.
* <b>Residuals</b>: It's the error component, random and doesn't systematicaly depend on the time. It's caused by the lack of info, or caused by random noise, and it's inrreducible.

To explore a time series sequence, we often start with <b>decomposition</b>, which is a process of decomposing the sequence to trend, seasonlity and residuals. There are 2 categories of decomposition:

* Additive Method `Y[t] = T[t] + S[t] + E[t]`
  * It assumes the time series value at time `t` is the sum of trend (`T`), seasonality (`S`) and residuals (`E`) at time `t`.
  * This model is usually applied when there is a time-dependent trend component but constant seasonality that has the same amplitude and frequency over time.
* Multiplicative Method `Y[t] = T[t] * S[t] * E[t]`
  * This model often used when there is non-constant seasonality.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/trend_cycle.png" width="766" height="79" />
</p>

Let's look at the decomposition of our sales data. This is the additive decomposition:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/additive_dep.png" width="1116" height="500" />
</p>

And this is the multiplicative decomposition, looks almost the same as additive method's output, right? But as marked below, the data scale in seasonality and residuals are different:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multiplicative_decomp.png" width="1116" height="500" />
</p>

🌻 [Check detailed code in Time Series Decomposition >>][2]

<b>Observations</b>:
* The seasonality repeats almost every 7.5 days, that's around 1 week.
* Since the seasonality is not constant along the time, this time series might be more suitable to use multiplication decomposition.
* The residuals tend to have larger fluctuations between April and July, or at the beginning of a new year or at the beginning of October, this insight might be useful in later feature enggineering for model forecasting.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][4]
 
[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_sales.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/yinyang/past_ts_exploration.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts2.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/garden_totem.md
