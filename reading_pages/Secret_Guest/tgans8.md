Seeing both AUC and AVP kept being low (under 0.6), Lady H. started to wonder whether there are certain features in synthetic data played an important role in low performance? If so, maybe she can improve the prediction performance from those features.

To validate her assumption, she aims to investigate whether certain features influence the predicted probability towards higher or lower values. SHAP proves to be a valuable tool for this purpose. A higher positive SHAP value suggests that a feature contributes more efforts to pushing the predicted value higher, whereas a lower negative SHAP value indicates that the feature adds more efforts in pushing the predicted value lower.

In the chart below, she compares the positive difference of `real_data_predicted_probability - synthetic_data_predicted_probability`:
* On the left SHAP screenshot, she chose records with the largest differences.
  * The left SHAP plot represents feature contributions from the real data. Organized right-leaning lines suggest features collectively contribute to a positive predicted probability. Features that push the line farther from the middle grey line have a more significant role in driving a higher prediction probability. Thus, the top features in this SHAP plot exert greater influence.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/pos_shaps.png" width="967" height="471" />


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/syn_data_exps/deep_dive.ipynb