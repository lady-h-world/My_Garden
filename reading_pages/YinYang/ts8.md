## Trend Detection

Trend detection is to find data points where an increasing or decreasing trend started. This detection feature is provided in Kats but not in Greykite.

Kats mainly uses M-K (Mann Kendall) Test for trend detection. It calculates all the differences between `y_t` and all its previous `y_i` within the time window, then sum up the signs of these differences. The time point that gets the largest positive value is the trend increasing point, and the one gets the lowest negative value is the trend decreasing point.

Besides, Kats also provides Seasonal M-K Test for seasonal trend detection, which performs M-K test within the same season. For example, for monthly seasons, the summed up signs for January observations is only compared with other January observations, there is no cross-season comparison.

Let's look at how to apply these tests in practice!

With the code below, we can do M-K test and plot all the detected trend points.
* `direction` can be "up", "down" and "both" for increasing, decreasing or both trends detection.
* `window_size` specifies the size of the moving window.
* `freq` indicates the seasonality ("weekly", "monthly" or "yearly"), when there is such seasonality in the time series, Kats will apply rolling average with relevant frequency (weekly/monthly/yearly) to smooth out the time series data.
* `threshold` indicates the intensity of detected trend, it's a value between [0, 1], higher threshold returns more detected points, if you set the value as 0, it will use p-value with default alpha=0.05 for the detection.
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/mk_trend_detection.png" width="905" height="145" />
</p>

Here's the increasing trend points detection. As we found in previous data exploration stage, the seasoanlity has 7.5 days frequency, therefore Lady H. set `freq=weekly` here, and all the detected points are marked with a read line in the plot below.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/up_mk.png" width="1084" height="530" />
</p>
At the same time, you might have noticed the warning saying "No trend detected!"...😓 This is just an annoying bug in Kats' output... it happens in almost every detection output, so just ignore it.

Similarly, here's the plot of decreasing trend detection:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/mk_down.png" width="1090" height="524" />
</p>

Do you feel the above plots are too intense? If you want to get less points detected, there're a few ways to try:
* Reduce `threshold` value to reduce the detection intensity
* Increase the `window_size`
* Keep `freq=None` as shown below, so that there is no rolling average smoothing and the detected trend points can be lower

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

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][2]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/yinyang/kats_experiments/kats_detect_trend.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts9.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts7.md
