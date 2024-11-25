## Changepoint Detection
As we saw in trend detection, the detected output are time points where the trend changes. Changepoint detection is also a method to detect time points, but the point indicates where the probability distribution of a time series changes. In some libraries such as Greykite, trend detection is included in its changepoint detection. In Kats, they are seperated. Let's take a look at Kats changepoint detection first.


### Kats Changepoint Detection
The experiments for Kats changepoint detection are shown with humidity and temperature time series data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/input_humidity.png" width="1075" height="155" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/temperature_input.png" width="1074" height="158" />
</p>


#### Kats' CUSUM Detector
CUSUM Detector detects the up or down shift of means in the time series. Starting from an initial point, it calculates the CUSUM of means iteratively, and locates a changepoint where its previous CUSUM is maximized or minimized. 

The null hypothesis is `H0: There is no change in the mean`. We can decide to detect a single changepoint or multiple changepoints. Let's start from single changepoint detection!

##### Single Changepoint Detection
To use CUSUM Detector in Kats, we need to initialize the detector with a time series input as shown in Step 1, then we can write a function in Step 2 to load detector's parameters and plot the changepoint, finally Step 3 shows the output of increasing changepoint detection for both humidity and temperature data. The parameter `threshold` is the significance level for null hypothesis. As we can see, in temperature data, there is no significant increasing changepoint detected, given 0.05 significance level.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_single_code.png" width="998" height="740" />
</p>

Similarly, we can detect decreasing changepoint for the time series as shown below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_single_decrease.png" width="926" height="598" />
</p>

What's more, sometimes we only want to do the detection within part of the time series, so we can specify an interest window and the changepoint detection will only happen within the window. Of course, the detected result is only valid locally in the window but may not be valid in the whole time series.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_single_interest_window.png" width="1081" height="324" />
</p>

🌻 [Check detailed code in Kats Changepoint Detection >>][3]

##### Multiple Changepoints Detection

The secret to enable multiple changepoints detection with CUSUM Detector is to add a sliding window. When the window slide forward in a fixed step size, the detector will detect the changepoint within the window.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_multi_code.png" width="933" height="331" />
</p>

In this example, we are using window size as 2000 (meaning, there're 2000 records in the window) and step size as 800 to detect the increasing changepoints, the results are markded in red lines. As you can see below, some red lines are close together, if you want to avoid this happen, you can set a larger step size, so that there is less overlap between windows.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_multi_up.png" width="999" height="569" />
</p>

Similarly, here're the detected decreasing changepoints:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/cusum_multi_down.png" width="995" height="576" />
</p>

🌻 [Check detailed code in Kats Changepoint Detection >>][3]


#### Kats' RobustStat Detector

If to detect multiple changepoints with CUSUM Detector needs self-implemented rolling window function, then RobustStat Detector can do this for you in one run. Similar to CUSUM Detector, it detects changepoints by checking mean shifts. It will start with smoothing out the time series using moving average, then compare the differences between a window of data points with its previous windows (window size is fixed, called as `comparison_window`). Finally it calculates the z-score, p-values of those differences, and mark those points with p-value smaller than the threshold as changepoints.

To detect a single changepoint, it looks like this:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/robuststat_single.png" width="1085" height="876" />
</p>

However, as we can see, we can't specify the changepoint to be the "increasing" or the "decreasing" one. [Kats documentation][4] is too poor, you simply don't know how to properly set parameter values in the function... And here's how to generate multiple changepoints detection, it seems that the trick is to use a smaller comparison window.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/robuststat_mul.png" width="617" height="781" />
</p>

You might have noticed the small size of the visualization, in fact, Lady H. can't find a way to adjust the plot size... Either because Kats is an incomplete library or because of its embarassing software design...

🌻 [Check detailed code in Kats Changepoint Detection >>][3]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][1]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][2]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts10.md
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts8.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/penitent_arch/kats_experiments/kats_detect_changepoints.ipynb
[4]:https://facebookresearch.github.io/Kats/api/kats.detectors.robust_stat_detection.html
