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

CUSUM Detector detects the up or down shifts of means in the time series. Starting from an initial point, it calculates the CUSUM of means iteratively, and locate a changepoint where its previous CUSUM is maximized or minimized. 

The null hypothesis is `H0: There is no change in the mean`. We can decide to detect a single changepoint or multiple changepoints. Let's look at single changepoint detection first!

##### Single Changepoint Detection

To use CUSUM Detector in Kats, we need to initialize the detector with a time series input as shown in Step 1, then we can write a function like Step 2 to load detector's parameters and plot the changepoint, finally Step 3 is showing the output of increasing changepoint detection for both humidity and temperature data. The parameter `threshold` is the significance level for the null hypothesis. As we can see, in temperature data, there is no significant change detected given 0.05 significance level.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_single_code.png" width="998" height="740" />
</p>

Similarly, we can detect decreasing changepoint for the time series as shown below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_single_decrease.png" width="926" height="598" />
</p>

What's more, sometimes we only want to do the detection within part of the time series, so we can specify a interest window and the changepoint detection will only happen within the window. Of course, the detected results is only valid locally in the window but may not be valid in the whole time series.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_single_interest_window.png" width="1081" height="324" />
</p>

##### Multiple Changepoints Detection


