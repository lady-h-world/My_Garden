#### Task Data Preprocessing

This is the step where you can do whatever data operation in order to make sure the data set can be directly used for later model training. 

In Lady H.'s use case, she just wanted to convert some features into "category" type. Because for models such as LGBM (LightGBM), categorical features can be handled automatically if they are specified as "category" type. 

* `le_col` represents a feature that originally has a mix of numerical and string values, models won't be able to undrstand the data type and will report errors. So Lady H. converted them into integer format with label encoding first, then convert to "category" type.
* `int_cat_col` represents a categorical feature that originally appears to be integer format, they can be converted to "category" directly.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/data_preprocessing_code.png" width="812" height="291" />
</p>

🌻 [Check data preprocessing config >>][1]

🌻 [Check data_preprocessing.py code >>][2]


[1]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/config.yaml#L39
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/garden_market/luigi_pipeline/data_preprocessing.py

