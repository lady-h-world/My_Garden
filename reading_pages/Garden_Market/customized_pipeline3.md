#### Task Data Preprocessing

This is the step where you can do whatever data operation in order to make sure the data set can be directly used for later model training. 

In Lady H.'s use case, she just wanted to convert some features into "category" type. Because for models such as LGBM (LightGBM), categorical features can be handled automatically if they are specified as "category" type.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Garden_Market_images/customized_pipeline/data_preprocessing_code.png" width="812" height="291" />
</p>

