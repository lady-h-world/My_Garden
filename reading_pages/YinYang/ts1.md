# Time Series Data Exploration

Comparing with traditional datasets, time series data has hidden time patterns, which creates a different fun experience in data exploration! Let's looks at some popular and practical methods.

## Explore Univariate Time Series

### About the Data

Our Garden Market's perfume sales data has seasonality patterns, which is a typical timeseries data. See the example below, it's also a univariate time series data, meaning there is only 1 time dependent variable ("Daily_Sales" in this example) to explore. Its index is in time order.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_sales_exp.png" width="170" height="184" />
</p>

🌻 [To get sales time series data >>][1]


### Time Series Components

A time series sequence has multiple components:
* Trend: It indicates the overall direction of the time series sequence, such as upward, downward or no trend.
* Seasonality: It refers to the tendency of going up and down in a consistent frequency. It's repeative and is calendar related.
* Cycle: Similar to seasonlity, it's also repeative but with inconsistent frequencies. It's less frequent than seasonality fluctuations, and the timespan of a cyclical change can be longer than a seasonal change.
  * We don't try to remove cycle in time series stationary work, since when we check stationary, exogenous variables are not considered, but cycle is not time dependent and can only be explained by exogenous variables. For "stationary", you will see more details soon!
* Residuals: It's the irreducible error component, random and doesn't systematicly dependent on the time. It's caused by the lack of info, or caused by random noise.

To explore a time series sequence, we often start with <b>decomposition</b>, which is a process to decompose the sequence to trend, seasonlity and residuals. There are 2 categories of decomposition:

* Additive Method `Y[t] = T[t] + S[t] + E[t]`
  * It assumes the time series value at time `t` is the sum of trend (`T`), seasonality (`S`) and residuals (`E`) at time `t`
  * This model is usually applied when there is a time-dependent trend component but constant seasonality that has the same amplitude and frequency over time
* Multiplicative Method `Y[t] = T[t] * S[t] * E[t]`
  * This model often used when there is non-constant seasonality

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/trend_cycle.png" width="766" height="79" />
</p>

Let's look at the decomposition of our sales data. This is the additive decomposition:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/additive_dep.png" width="1116" height="500" />
</p>

And this is the multiplicative decomposition, looks almost the same as additive method's output, right? But as marked below, the data scale in seasonality and residuals is different:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multiplicative_decomp.png" width="1116" height="500" />
</p>

🌻 [Check detailed code in Time Series Decomposition >>][2]

<b>Obseravtions</b>:
* The seasoanlity repeats almost every 7.5 days, that's around 1 week.
* Since the seasonality is not constant along the time, this time series might be better to use multiplication decomposition.
* The residuals tend to have larger fluctuations between April and July, or at the beginning of a new year or at the beginning of October.

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
