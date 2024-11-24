## Trend Detection
Trend detection aims to identify the data points where an increasing or decreasing trend begins. This functionality is available in Kats but is not offered in Greykite.

Kats mainly uses the Mann-Kendall (M-K) Test for trend detection. The M-K test evaluates trends in a time series by calculating the differences between each pair of time points `y_t` and `y_i` (t>i) within the time window. It sums up the signs of these differences to compute the S-statistic. A large positive S indicates an increasing trend, while a large negative S indicates a decreasing trend. The Mann-Kendall test identifies whether a monotonic trend exists in the time series but does not determine the specific time points where trends increase or decrease.

Additionally, Kats offers a Seasonal Mann-Kendall (M-K) Test for detecting seasonal trends. This test applies the M-K method separately within each season. For instance, in the case of monthly seasonality, the signs of differences for January observations are compared only with other January observations, with no comparisons made across different months.

Let's look at how to apply these tests in practice!

With the code below, we can do M-K test and plot all the detected trend points.
* `direction` can be "up", "down" and "both" for increasing, decreasing or both trends detection.
* `window_size` specifies the size of the moving window.
* `freq` indicates the seasonality ("weekly", "monthly" or "yearly"), when there is such seasonality in the time series, Kats will apply rolling average with relevant frequency (weekly/monthly/yearly) to smooth out the time series data.
* `threshold` indicates the intensity of detected trend, it's a value between [0, 1], higher threshold returns more detected points, if you set the value as 0, it will use p-value with default alpha=0.05 for the detection.
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/mk_trend_detection.png" width="905" height="145" />
</p>

Here's the increasing trend points detection. As we found in previous data exploration stage, the seasoanlity has 7.5 days frequency, therefore Lady H. set `freq=weekly` here, and all the detected points are marked with a red line in the plot below.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/up_mk.png" width="1084" height="530" />
</p>

At the same time, you might have noticed the warning saying "No trend detected!"...😓 This is just an annoying bug in Kats' output... it happens in almost every output, so just ignore it.

Similarly, here's the plot of decreasing trend detection:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/mk_down.png" width="1090" height="524" />
</p>

Do you feel the above plots are too intense? If you want to get less points detected, there're a few ways to try:
* Reduce `threshold` value to reduce the detection intensity.
* Increase the `window_size`.
* Keep `freq=None` as shown below, so that there is no rolling average smoothing and the detected trend points might become lower, since small fluctuations had been smoothed out.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/mk_no_freq.png" width="1084" height="522" />
</p>

The code of seasonal trend detection is similar. Kats provides built-in Seasonal M-K test as shown below, and of course, the `freq` value of the detector is no longer needed.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/smk_trend_detection.png" width="909" height="147" />
</p>

Seasonal M-K test is often considered as a robust and powerful trend detection method, and here's the detection results:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/smk_output.png" width="1088" height="759" />
</p>

🌻 [Check detailed code in Kats Trend Detection >>][1]

Besides getting these detection output, we can also add this piece of info in feature engineering step, especially when we are using classical machine learning models. For example, we can create a new feature called "is_up_trend" and mark detected increasing trend time point as 1 while having other records as 0. The added feature provides more info to the model and might improve model forecasting accuracy.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][2]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/penitent_arch/kats_experiments/kats_detect_trend.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts9.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts7.md
