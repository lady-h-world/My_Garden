## Changepoint Detection

As we saw in trend detection, time points were detected. Similarly, changepoint detection is also a method to detect time points, but instead of detection the trend changing points, it's trying to find time points where the probability distribution of a time series changes.

### Kats Changepoint Detection Methods

The experiments for Kats changepoint detection are shown with humidity and temperature time series data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/input_humidity.png" width="1075" height="155" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/temperature_input.png" width="1074" height="158" />
</p>

Wondering why sales data is not shown here? Because Kats changepoint detection didn't work well on the sales data, the output was too bad to be used in the demo... 😅

#### CUSUM Detector
