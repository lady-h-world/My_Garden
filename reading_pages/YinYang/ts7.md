# Time Series Detection

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/kats_vs_greykite.png" width="234" height="263" /></p>

After data exploration, often times we want to dive deeper into the hidden patterns in time series, such as trend, seasonality, changepoints, outliers, etc. Some of these insights not only helps understand the time series better, but can help later model forecasting too.

To do these detection, Lady H. has experimented with 2 latest time series toolkits, Kats and Greykite. 

* [Kats][1] is a time series toolkit developped by Facebook Research.
* [Greykite][2] provides a framework for time series forecasting with its flagship algorithm Silverkite, it also provides exploratory analysis on time series.

Which is a better choice? Or when to use what? <b>Kats vs Greykite!</b> The competition time begins!


## Installation

### Install Kats

Kats didn't have frequent update. Lady H. was super busy with her work and life at the time, and only had no more than 1 hour each day to take care of the garden. So it took her 3 months to finish testing the superpower of the sprout in this stop. During this period, Kats stayed in v0.1, never changed. Such low updating frequency is rare among open source libraries from a giant company.

The installation of Kats was tricky, and the problems often happened in Prophet related features.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/prophet_note.png" width="766" height="79" />
</p>

To be able to use Prophet in Kats, you need to install and build it. Using conda-fordge (`conda install -c conda-forge prophet`) is a faster and safer way. However, [Kats requires installed Prophet to be a specific version][3] while conda-forge installed version can be higher. This can cause error when you try to import certain Kats functions. To resolve this issue, you would need to git clone Kats to your local environment and change its `requirements.txt` to make Prophet align with the version you have installed and built.


[1]:https://github.com/facebookresearch/Kats
[2]:https://github.com/linkedin/greykite
[3]:https://github.com/facebookresearch/Kats/blob/main/requirements.txt#L9
