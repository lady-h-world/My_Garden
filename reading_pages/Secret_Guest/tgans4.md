First of all, CTABGAN+ added an extra estimator to predict each variable in tabular data. For discrete variable, it predicts the probability of each category, for continuous variable, it predicts the regression value. The assumption behind is the same as [ACGAN mentioned before][1], by introducing this auxiliary estimator, the quality of the output can be enhanced.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Secret_Guest_images/ctabgan+_auxiliary.png" width="961" height="330" />


[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Secret_Guest/tgans2.md