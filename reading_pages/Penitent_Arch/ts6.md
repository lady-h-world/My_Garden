### Granger Causality
When exploring the relationship between variables in a multivariate time series, we also want to know <b>whether one variable can forecast or influence another variable</b>. Granger causality is used for this type of analysis.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/notes/granger_causality_not_causality.png" width="766" height="79" />
</p>

Although <b>Granger Causality does NOT imply true causation</b>, it is often used to infer "the influence". For example, if variable A granger causes variable B, but variable B does not granger cause variable A, we can assume that variable A influences variable B.

Let's understand details through the code. 

Before applying granger causality, Lady H. suggests to do some data preprocessing:
* <b>Remove highly correlated variables</b> to minimize unnecessary calculations. If one variable can forecast another or be forecasted by it, then any highly correlated variables are likely to have similar effects.
* <b>Ensure the multivariate time series is stationary.</b> <i>This was already done in previous stationary analysis step.</i>

Here's the code Lady H. often uses to remove higher correlated columns.
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/gc_rm_high_corr.png" width="989" height="349" />
</p>

After data preprocessing, now let's look at the core logic of granger causality and the influence analysis.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/granger_causality_code.png" width="738" height="327" />
</p>

When we are using `grangercausalitytests(df[[col1, col2]])`, the null hypothesis and alternative hypothesis are:
* H0 (null hypothesis): col2 does not granger cause col1
* H1 (alternative hypothesis): col2 granger causes col1

Therefore when we have found col2 granger causes col1 but col1 doesn't granger cause col2, then we assume col2 can influence col1, and vice versa.

The mutual influence of our greenhouses' data is shown below. It aligns with common sense, also discloses why the icreasing of CO2 creates a vicious circle of worsening the global environment. 😰

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Totem_images/data_exploration/granger_causality_output.png" width="810" height="351" />
</p>

🌻 [Check detailed code for Granger Causality][3]


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][1]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][2]

[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts7.md
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Penitent_Arch/ts5.md
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/penitent_arch/past_ts_exploration.ipynb
