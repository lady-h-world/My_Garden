### AutoKeras

AutoKeras specializes in deep learning model selection. Whether your data involves classification or regression, it automatically builds an optimal neural network, which is pretty cool! It is built upon Keras Tuner, [the HPO tool used at Lotus Queen][1].


#### Regression with AutoKeras

Lessons learned from TPOT's 4 hours execution, when applying AutoKeras on the Sales data, Lady H. decided only to use 3 numerical features as the input feature set, in order to save time. These 3 features are "Customers_larger_than_3000", "CompetitionDistance" and "Customers".

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/ak_reg_data.png" width="991" height="461" />
</p>

Using the "Bayesian" tuning method and limiting it to just 3 epochs aimed to reduce the overall execution time. In the end, model selection took around 45 minutes but resulted in a negative R² score - an unsurprisingly poor outcome. Below is the neural network structure that was selected:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/ak_reg.png" width="1014" height="860" />
</p>

🌻 [Look into AutoKeras regression experiment details >>][2]


#### Classification with AutoKeras

Since the Leaves30 data is much smaller, using 100 epoches, the model selection can be finished within 7 minutes. 

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/ak_cla1.png" width="735" height="276" />
</p>

And the optimal neural network structure is as shown below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/ak_cla2.png" width="568" height="499" />
</p>

🌻 [Look into AutoKeras classification experiment details >>][2]

The classification performance is fine, but it is still no better than what FLAML achieved during HPO.


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<< Looking back][4]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Lotus_Queen/param_tuning_6.md#keras-tuner-hpo-in-deep-learning
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/mini_pipelines/autokeras.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline4.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline2.md
