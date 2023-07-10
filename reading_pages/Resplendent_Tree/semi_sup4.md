#### Performance with Different Mask Rate

Lady H. applied both DIY solution and built-in `ElkanotoPuClassifier` solution on datasets with 95%, 80%, 50%, 30% mask rates. It turned out DIY solution is still a better option. Let's look into details.

This is the performance comparison on 95% masked data. At the best threshold, both solution have `pred_pos_perct` close to `real_pos_perct`, but DIY solution has higher `known_recall`.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_0.95.png" width="1153" height="946" />

For 80%, 50% and 30% masked data, the performance difference at the best threshold is minor, but DIY solution still has slightly better `known_recall`.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_0.8.png" width="1109" height="917" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_0.5.png" width="1131" height="930" />

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/pu_0.3.png" width="1132" height="945" />

* 🌻 [Check DIY PU Learning code >>][1]
* 🌻 [Check Built-in PU Learning code >>][2]

😁 So the DIY solution won!


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Resplendent Tree Home >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][4]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/try_diy_pu_learning.ipynb
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/semi_supervised/try_pulearn.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/about_resplendent_tree.md#correlation--clustering
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/semi_sup3.md