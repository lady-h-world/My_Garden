Lady H. observed that the AUC and AVP of synthetic data were consistently lower than those of real data. This prompted her to investigate whether certain features caused more incorrect predictions in synthetic data trained model. To validate her assumption, she did some SHAP analysis.

A higher positive SHAP value suggests that a feature contributes more efforts to pushing the predicted value higher, whereas a lower negative SHAP value indicates that the feature adds more efforts in pushing the predicted value lower.

Firstly, she checks the <b>positive class records</b> where the real data trained model predicted correctly while the synthetic data trained model predicted wrong.
* In <b>"Large Positive Proba Difference"</b> chart, she chose records with `real_data_predicted_probability - synthetic_data_predicted_probability >= 0.6`.
  * The left SHAP decision plot represents feature contributions from the real data. Organized right-leaning lines suggest features collectively contribute to higher probabilities, the correct class.
  * The right SHAP decision plot represents feature contributions from CTGAN's synthetic data. Organized left-leaning lines suggest features collectively contribute to lower probabilities, the incorrect class.
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/shap_decision_plot.png" width="880" height="90" />
</p>

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/pos_shaps.png" width="967" height="471" />

* In <b>"Small Positive Proba Difference"</b> chart, she chose records with `0.1 > real_data_predicted_probability - synthetic_data_predicted_probability > 0`.
  * In both SHAP decision plots, lines are gathered in the middle, there's no clear left or right leaning patterns.

The comparison between "Large Positive Proba Difference" and "Small Positive Proba Difference" indicates, for positive class records, there are some top features affect the prediction differences between real data trained model and synthetic data trained model. When such features play a bigger influence, the differences are larger, and when such features have a smaller influence, the differences are smaller.

Then how about <b>negative class records</b>? Can we find simiar patterns? Indeed, yes!

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/neg_shaps.png" width="967" height="471" />

🌻 [Check code details here >>][1] 


Next, she chose the most "suspicious" features from above analysis, to further check their distributions.

This is the distribution comparison between real data and CTGAN generated synthetic data, for <b>all positive records</b>:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/pos_dist.png" width="1001" height="559" />

And this is the distribution comparison for <b>all negative records</b>:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/neg_dist.png" width="1001" height="559" />

Comparing these 2 screenshots, did you find any interesting clues? 😉

Lady H. noticed for features like duration and age, their CTGAN generated features in negative class have lots of overlap with their positive class values, by contrast real data's values in these features are better at distinguishing the positive and negative classes. This might be part of reasons why real data trained model performed better in classification. Having this thought, she decided to use CTGAN to generate synthetic training data for positive class and negative class separately, hoping this can get more accurate feature distributions in both classes and therefore improve the synthetic data trained model's performance. 

This method is called as ASDGP, standing for <b>A</b>djusted <b>S</b>ynthetic <b>D</b>ata <b>G</b>eneration <b>P</b>rocess, a name Lady H. made up 😉!

And she made it! The performance finally jumped above 0.6.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/syn_exp_table.png" width="930" height="441" />

🌻 [Check code details here >>][1] 

Do you have any other ideas to further improve the prediction performance of synthetic trained model? Would you like to try with CastGAN? You're very welcome to share your experiments or ideas [here][2]!


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Secret Guest Home >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][3]

[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/deep_dive.ipynb
[2]:https://github.com/lady-h-world/My_Garden/discussions
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans7.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/secret_guest.md