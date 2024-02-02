Lady H. observed that the AUC and AVP of synthetic data were consistently lower than those of real data. This prompted her to investigate whether certain features caused more incorrect predictions in synthetic data trained model.

To validate her assumption, she did some SHAP analysis. A higher positive SHAP value suggests that a feature contributes more efforts to pushing the predicted value higher, whereas a lower negative SHAP value indicates that the feature adds more efforts in pushing the predicted value lower.

Firstly, she checks the <b>positive class records</b> where the real data trained model predicted as positive while the synthetic data trained model predicted wrong.
* On the left SHAP screenshot, <b>"Large Positive Proba Difference"</b>, she chose records with `real_data_predicted_probability - synthetic_data_predicted_probability >= 0.6`.
  * The left SHAP decision plot represents feature contributions from the real data. Organized right-leaning lines suggest features collectively contribute to higher probabilities.
  * The right SHAP decision plot represents feature contributions from CTGAN's synthetic data. Organized left-leaning lines suggest features collectively contribute to lower probabilities.
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/shap_decision_plot.png" width="880" height="90" />
</p>

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/pos_shaps.png" width="967" height="471" />

* On the right SHAP screenshot, <b>"Small Positive Proba Difference"</b>, she chose records with `0.1 > real_data_predicted_probability - synthetic_data_predicted_probability > 0`.
  * In both SHAP decision plots, lines are gathered in the middle, there's no clear left or right leaning patterns.

The comparison between "Large Positive Proba Difference" and "Small Positive Proba Difference" indicates, for positive class records, there are some top features affect the prediction differences between real data trained model and synthetic data trained model. When such features play a bigger influence, the differences are larger, and when such features have a smaller influence, the differences are smaller.

Then how about <b>negative class records</b>? Can we find simiar patterns? Indeed, yes!

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/neg_shaps.png" width="967" height="471" />

🌻 [Check code details here >>][1] 

[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/deep_dive.ipynb
