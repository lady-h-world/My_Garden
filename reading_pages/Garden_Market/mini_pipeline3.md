### AutoKeras

AutoKeras is used for deep learning model selection specifically. No matter your data is a classification or a regression problem, it will try to build an optimal neural network for you, which is cool! It is built upon Keras Tuner, [the HPO tool used at Queen Lotus' site][1], therefore it accepts parameters used in Keras Tuner.

#### Regression with AutoKeras

Lessons learned from TPOT's 4 hours execution, when applying AutoKeras on the Sales data, Lady H. decided only to use 3 numerical features as the input feature set, in order to save time. These 3 features are "Customers_larger_than_3000", "CompetitionDistance" and "Customers".

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/mini_pipeline/ak_reg_data.png" width="991" height="461" />
</p>

Using "bayesian" tuning method and only apply 3 epochs was also trying to reduce the overall execution time. Finally the model selection took around 45 minutes but only got a negative R2 score, an unsurprisingly bad result. But without such a terrible performance, how can we realize the benefits of using MLJar later 😉. Below, you can also see the selected neural network structure:

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

The classification performance is fine, but it is still no better than what FLAML achieved during HPO. Time to show MLJar, it gets more satisfying output.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [<< Looking back][4]
 


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/param_tuning_6.md#keras-tuner-hpo-in-deep-learning
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/mini_pipelines/autokeras.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline4.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Garden_Market/mini_pipeline2.md
