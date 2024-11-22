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
A time series sequence consists of several key components:

* <b>Trend</b>: Represents the overall direction of the time series, such as upward, downward, or stable with no trend.
* <b>Seasonality</b>: Refers to consistent, repetitive fluctuations occurring at regular intervals, often linked to the calendar.
* <b>Cycle</b>: Similar to seasonality but with irregular frequencies. Cycles are less frequent and may span longer periods than seasonal changes. Unlike seasonality, cycles are not time-dependent and are typically influenced by external factors.
* <b>Residuals</b>: The random error component, which does not systematically depend on time. Residuals arise from missing information or random noise and are irreducible.

To analyze a time series sequence, we often begin with <b>decomposition</b>, a process that separates the sequence into its trend, seasonality, and residual components. There are two types of decomposition methods:

* <b>Additive Method</b>:
  * Formula: `Y[t] = T[t] + S[t] + E[t]`
  * Assumes the time series value at time `t` is the sum of the trend (`T`), seasonality (`S`), and residuals (`E`) at time `t`. Typically used when the trend component is time-dependent but seasonality remains constant in amplitude and frequency over time.

* <b>Multiplicative Method</b>:
  * Formula: `Y[t] = T[t] * S[t] * E[t]`
  * Generally applied when the seasonality varies in amplitude over time.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/trend_cycle.png" width="766" height="79" />
</p>

Let's look at the decomposition of our sales data. This is the <b>additive decomposition</b>:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/additive_dep.png" width="1116" height="500" />
</p>

This is the result of the <b>multiplicative decomposition</b>. At first glance, it looks almost identical to the output from the additive method, right? However, as highlighted below, the scale of the data in the seasonality and residual components is noticeably different.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/multiplicative_decomp.png" width="1116" height="500" />
</p>

🌻 [Check detailed code in Time Series Decomposition >>][2]

<b>Observations</b>:
* The seasonality repeats almost every 7.5 days, that's around 1 week.
* The seasonality is constant.
* The residuals tend to have larger fluctuations between April and July, or at the beginning of a new year or at the beginning of October, this insight might be useful in later feature engineering for model forecasting.


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
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/penitent_arch/past_ts_exploration.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts2.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/penitent_arch.md
