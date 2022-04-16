# Time Series Detection

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/kats_vs_greykite.png" width="234" height="263" /></p>

After data exploration, often times we want to dive deeper into the hidden patterns in time series, such as trend, seasonality, changepoints, outliers, etc. Some of these insights not only helps understand the time series better, but can help later model forecasting too.

To do these detections, Lady H. has experimented with 2 latest popular time series toolkits, Kats and Greykite. 

* [Kats][1] is an open source time series toolkit developped by Facebook Research.
* [Greykite][2] provides a framework for time series forecasting with its flagship algorithm Silverkite, it also provides exploratory analysis on time series.

Which is a better choice? Or when to use what? <b>Kats vs Greykite!</b> The competition begins!


## Installation

### Install Kats

Kats doesn't update as frequent as as many other popular open source libraries. 

Lady H. was super busy with her work and life at the time, and only had around 1 hour each day to take care of the garden. So it took her 3 months to finish testing the superpower of the sprout in this stop. During this period, Kats stayed in version 0.1.0, never changed. Such low code updating frequency is rare among giant companies' products.

The installation of Kats was tricky, and the problems often happened in Prophet related features.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/prophet_note.png" width="766" height="79" />
</p>

A better way to install Kats is to git clone its repo to your local environment and manually install it, here's how:
1. Open your local environment terminal and go to the directionary where you want to install Kats
2. Type `git clone https://github.com/facebookresearch/Kats.git` to download Kats library to your local environment
3. Enter into `Kats` fodler and type `python setup.py install` to manually install Kats
* If you are using python virtual environment, then find its python path to replace "python" in this command. For example, Lady H. was using conda virtual env called "yinyang", so her command was `C:\ladyh\anaconda3\envs\yinyang\python setup.py install`

Wondering why better to manually install this library? Lady H. does gathered multiple reasons after trails and errors! 🧐

First of all, conflicting library versions can cause problems. For example, as we can see [Kats requires the installed Prophet to be a specific version][3], but in order to use Prophet, you need to successfully build it first. What happened to Lady H. was, the Prophet version she could built had to be higher than the version required by Kats. So, in order to install Kats, she had to change Kats' `requirements.txt` to make Prophet's version align with her built version. However, the risk of doing this is, you might face problems when calling certain Kats' functions later...

Another benefit of installing Kats manually is, you might need to fix some bugs in Kats yourself in order to keep using a function... [See what happened to Lady H.][4]

Moreover, here're a few more installation you might need in order to use Kats:
* `pip install attr`, adding "attr" in Kats' requirememts.txt may not work...
* `pip install deprecated`
* `pip install ax-platform`
* Make sure `statsmodels==0.12.2`, higher version will get errors about when using Kats' VAR

After experienced all these troubles, Lady H. figured out that, the suggested installation process above provided her more flexibility.

### Install Greykite

Make sure pandas version is not higher than "1.3.0", then just type `pip install greykite`

## Data Input

When you are using Kats, the time series data input has to be converted to `TimeSeriesData`, a Kats built-in class. Meanwhile, as shown below, the time index has to be a column called "time". After the conversion, at least with Kats v0.1.0, there's no easy way to print out the data sample.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/kats_input.png" width="692" height="397" />
</p>

By comparison, Greykite is more flexible. You can keep the data input as pandas and only need to tell Greykite which column is the time index and which column is the time series column, this also allows you to look into each variable of a multivariate time series data. As shown below, you can also print out the data sample easily.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/greykite_input.png" width="806" height="364" />
</p>

The difference between Kats and Greykite here is also showing software design differences in data science projects. When building a data science library, code owners might think using OO (Object Oriented) design is the best choice but they might be lack of mature OO design skills to provide flexible user experience, therefore as you can see, we even can't print out the data sample after converting data to `TimeSeriesData` in Kats. By comparison, Greykite is doing a better job here. It keeps the solution simple by keep pandas input as it is.

Does this mean Greykite is better than Kats on everything? Let's see! 😉

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][5]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][6]


[1]:https://github.com/facebookresearch/Kats
[2]:https://github.com/linkedin/greykite
[3]:https://github.com/facebookresearch/Kats/blob/main/requirements.txt#L9
[4]:https://github.com/facebookresearch/Kats/issues/194
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts8.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts6.md
