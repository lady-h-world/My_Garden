### Association between Categorical Variables

To measure the association between categorical variables, there're 2 popular choices:
* `Pearson's Chi2 Test` is used to determine whether there is a statistically significant difference between the expected frequencies and the observed frequencies in one or more categories of a contingency table. A contigency table is a table in a matrix format that displays the frequency distribution of variables, [for example][1].
* `Cramer's V` measures the associations between 2 categorical variables, based on Pearson's Chi2 Test.

You can consider they are the same method 😊. 

But in python implementation, there're some differences. The code below allows to choose either Chi2 or Cramer's V. 
The output of Chi2 is mainly using p value to decide the association. It needs a threshold (namely, significant level, 
often 
choose 0.05) and when p value is lower than this thereshold, we can consider there's an association. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/chi2_cramer_code_v2.png" width="829" height="409" />

By contrast, Cramer's V is more straightforward. It outputs a value that represents the association degree. Higher 
value 
indicates higher association. So its output is easier to interpret. Look at this output:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/chi2_cramer_out_v2.png" width="321" height="204" />

🌻 [Look into code details here >>][2] 


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][3]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][4]
 



[1]:https://en.wikipedia.org/wiki/Contingency_table
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/var_relationships/association.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/rel3.md
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/rel1.md
