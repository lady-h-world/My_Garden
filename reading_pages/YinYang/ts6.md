### Granger Causality

When exploring the relationship between variables in a multivariate time series, we also want to know whether one variable can forecast or influence another variable. Granger causality is used for this type of analysis.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/granger_causality_not_causality.png" width="766" height="79" />
</p>

Although granger causality is not causality, sometimes we still use it to generate "assumed causality", meaning, if variable A granger causes variable B and variable B does not granger cause variable A, then we assume variable A causes variable B.

Let's understand details through the code. 

Before applying granger causality, Lady H. suggests to do some data preprocessing:
* Remove highly correlated variables, to reduce unnecessary calculation. Because if a variable can forecast another variable or can be forecasted by another variable, then its highly correlated variable can have similar effect.
* Make the multivariate time series stationary. <i>This was already done in previous stationary analysis step.</i>

Here's the code Lady H. often uses to remove higher correlated columns.
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/gc_rm_high_corr.png" width="989" height="349" />
</p>

After data preprocessing, now let's look at the core logic of granger causality and assumed causality analysis.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/assumed_causality_code.png" width="738" height="327" />
</p>

When we are using `grangercausalitytests(df[[col1, col2]])`, the null hypothesis and alternative hypothesis are:
* H0: col2 does not granger cause col1
* H1: col2 granger cause col1

Therefore when we have found col2 granger causes col1 but col1 doesn't granger cause col2, then we assume col2 causes col1, and vice versa.

The assumed causality of our green houses' data is shown below. It aligns with common sense, also discloses why the icreasing of CO2 creates a vicious circle of worsening the global environment. 😰

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/assumed_causality_output.png" width="810" height="351" />
</p>

Besides exploring assumed causality, we can also use the output to understand the interchangable influence between variables in a multivariate time series. If we found such influence exists, then models like VAR can be a good choice to be applied to the data for forecasting, outlier detection, etc.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][1]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][2]

[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts7.md
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/YinYang/ts5.md
