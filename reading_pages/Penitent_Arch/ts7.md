# Time Series Detection

<p>
<img align="right" src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/kats_vs_greykite.png" width="234" height="263" /></p>

After exploring the data, we often dive deeper into time series patterns like trend, seasonality, changepoints, and outliers. These insights not only improve understanding but also enhance forecasting models.

To do these detections, Lady H. has experimented with 2 latest popular time series toolkits, Kats and Greykite. 

* [Kats][1] is an open-source time series toolkit from Facebook Research.
* [Greykite][2] is a framework for forecasting with its flagship Silverkite algorithm, also supporting exploratory analysis.

Which is the better choice? Let the <b>Kats vs. Greykite</b> competition begin!


## Installation

### Install Kats
Kats doesn't update as frequent as many other popular open source libraries. [Check its release history][7] 😉.

The installation of Kats was tricky, and the problems often happened in Prophet related features.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/prophet_note.png" width="766" height="79" />
</p>

A better way to install Kats is to git clone its repo to your local environment and manually install it, here's how:
1. Open your local environment terminal and go to the directory where you want to install Kats
2. Type `git clone https://github.com/facebookresearch/Kats.git` to download Kats library to your local environment
3. Enter into `Kats` folder and type `python setup.py install` to manually install Kats
* If you are using python virtual environment, then find its python path to replace "python" in this command. For example, Lady H. was using conda virtual env called "yinyang", so her command was `C:\ladyh\anaconda3\envs\yinyang\python setup.py install`

Wondering why better to manually install this library? Lady H. has multiple reasons after trails and errors! 🧐

First of all, conflicting library versions can cause problems. For example, as we can see [Kats requires the installed Prophet to be a specific version][3], but in order to use Prophet, you need to successfully build it first. What happened to Lady H. was, the Prophet version she could built had to be higher than the version required by Kats. So, in order to install Kats, she had to change Kats' `requirements.txt` to make Prophet's version align with her built version. However, the risk of doing this is, you might face problems when calling certain Kats' functions later...

Another benefit of installing Kats manually is, you might need to fix some bugs in Kats yourself in order to keep using a function... [See what happened to Lady H.][4], she finally implemented the function herself.

Moreover, here're a few more installation you might need in order to use Kats:
* `pip install attr`, adding "attr" in Kats' requirememts.txt may not work...
* `pip install deprecated`
* `pip install ax-platform`
* Make sure `statsmodels==0.12.2`, higher version will get errors when using Kats' VAR model

After experienced all these troubles, Lady H. figured out that, manually install Kats provides more flexibility.

### Install Greykite

Make sure pandas version is no more than "1.3.0", then just type `pip install greykite`.

## Data Input

When you are using Kats, the time series data input has to be converted to `TimeSeriesData`. Meanwhile, as shown below, the time index has to be named as "time". After the conversion, there's no easy way to print out the data sample.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/kats_input.png" width="692" height="397" />
</p>

By comparison, Greykite is more flexible. You can keep the data input as pandas and only need to tell Greykite which column is the time index and which column is the time series column, this also allows you to look into each variable of a multivariate time series data. Besides, as shown below, you can print out the data sample easily.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/detection/greykite_input.png" width="806" height="364" />
</p>

Greykite has obviously better user experience, the problem in Kats is caused by product design or software design? Lady H. thinks it's both. Does this mean Greykite is better than Kats on everything? Let's see! 😉

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
[3]:https://github.com/facebookresearch/Kats/blob/fix_plots/requirements.txt#L9
[4]:https://github.com/facebookresearch/Kats/issues/194
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts8.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts6.md
[7]:https://github.com/facebookresearch/Kats/releases
