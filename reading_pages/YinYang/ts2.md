### Stationary Analysis

When we say a time series is "stationary", it means the time series has constant mean, variation throughout the time. This is also means stationary time series is time independent. There are many statistical methods applied on time series assume the data is stationary, therefore we often have to convert the data to stationary before applying these statistical methods.

To check whether a sequence data is stationary, Lady H. often applies 3 methods at the same time:
* <b>Plot the rolling mean and rolling standard deviation of the time series input</b>. Ideally, if the rolling mean and rolling standard deviation appear to be constant, it means the data has constant mean and variation along the time, and highly likely to be stationary. But the visualization only provides an idea, we need to look into more details.
* <b>Augmented Dickey-Fuller (ADF) Test</b> checks differencing stationary. The idea is, the time series will be transformed to stationary through differencing. This method only checks whether the rolling mean changes.
* <b>KPSS Test</b> checks trending stationary. The idea is, by removing the trend, the time series will become stationary.




