# Time Series Data Exploration

Comparing with traditional dataset, time series data has hidden time patterns, which creates a different fun experience in data exploration! Let's looks at some popular and practical methods.

## Explore Univariate Time Series

### About the Data

Our Garden Market's perfume sales data is a typical timeseries data. See the example below, it's also a univariate time series data, meaning there is only 1 time sequence column ("Daily_Sales" in this example) to explore. Its index is in time order.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/ts_sales_exp.png" width="170" height="184" />
</p>

🌻 [To get sales time series data >>][1]


### Time Series Components

A time series sequence has multiple components:
* Trend: It indicates the overall direction of the time series sequence, such as upward or downward.
  * Sometimes, we need to look into each subset of the sequence to discover the trending.
* Seasonality: It's a repeative and calendar related (has fixed period of variations) pattern.
* Cyclical (Optional): Similar to seasonlity, it's also repeative but doesn't have fixed period of variations. It's less frequent than seasonality fluctuations, and the timespan of a cyclical change can be longer than a seasonal change.
  * We don't try to remove cyclical in time series stationary work, since when we check stationary, exogenous variables are not considered, but cyclical is not time dependent and can only be explained by exogenous variables. For "stationary", you will see more details soon!
* Residuals: It's the irreducible error component, random and doesn't systematic dependent on the time. It's caused by the lack of info, or caused by random noise.

To explore a time series sequence, we often start with <b>decomposition</b>, which is a process to decompose the sequence to trend, seasonlity and residuals.


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/generate_sales.ipynb

