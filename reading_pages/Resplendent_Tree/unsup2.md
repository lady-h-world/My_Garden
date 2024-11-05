### Finding Optimal K
There are countless data science tutorials available online, but how do you typically use them? While these tutorials often spark inspiration, Lady H. is cautious about taking them at face value. When she finds something intriguing, she delves deeper into the theory and validates it through additional experiments.

The inspiration for this experiment came from an article titled ["Are You Still Using the Elbow Method?"][1]. In the article, the author compares several k-estimation algorithms using five datasets with clusters ranging from 2 to 25. The visualizations are quite compelling, and the author concludes that the elbow method, a popular k-estimation approach, performed the worst. Since the datasets in the article consist of well-separated blobs, Lady H. wondered how these algorithms would perform on more complex datasets.

Before diving into Lady H.'s experiments, let’s first understand how each k-estimation algorithm works. To identify the optimal `k`, the goal is to achieve clusters with high between-cluster variance and low within-cluster variance.


#### Elbow Method
The elbow method examines WCSS (Within-Cluster Sum of Squares), which is the sum of the squared distances between data points within a cluster and the cluster’s centroid. A lower WCSS indicates that data points within a cluster are closer together. The optimal `k` is typically chosen at the 'elbow' of the plot, where WCSS decreases most sharply. Choosing a larger `k` with an even smaller WCSS isn’t ideal, as it would create more clusters than necessary.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/plot_has_elbow.png" width="683" height="458" />

As we can see, the elbow method doesn’t evaluate between-cluster variance. Additionally, it can sometimes be difficult to identify the optimal `k` on the plot, as shown in the example below.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/plot_no_elbow.png" width="682" height="460" />


#### Calinski Harabasz Index
The Calinski-Harabasz Index, also known as the Variance Ratio Criterion, is calculated as `Calinski-Harabasz Index = sum(between-cluster dispersion) / sum(within-cluster dispersion)`, where dispersion represents the sum of squared distances. A higher Calinski-Harabasz Index indicates better clustering, as it reflects greater between-cluster variance and smaller within-cluster variance.

This index is quick to compute and tends to provide more accurate k estimations on clusters that are convex, dense, and well-separated.

Do you know what does "convex" mean to clusters?
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/convex_cluster.png" width="766" height="79" />
</p>

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/convex_example.png" width="494" height="239" />


#### Davies-Bouldin Index
DBI (Davies-Bouldin Index) measures the average similarity between each cluster and its most similar cluster. Calculating the similarity uses the ratio of the within-cluster distance and the between-cluster distance. When there's smaller within-cluster distance and larger between-cluster distance, DBI is lower, indicating a better clustering result.

DBI is easy to calculate and interpret. However, it only considers the pairwise distances between cluster centroids and cluster members, the score can be sensitive to outliers, and ignored the data distribution or structure (such as clusters within a cluster, or non-linear relationship, etc.). It also makes false assumption that clusters share the same density and size, which is not true in many real world scenarios.


#### Silhouette Coefficient
Silhouette Coefficient is a measure of how similar an object is to its own cluster comparing to other clusters. `Silhouette Coefficient = (b-a)/max(a,b)`, `a` is the average distance between each point within a cluster, `b` is the average distance between clusters. Its value is between 1 and -1, higher the better, 0 means overlapping clusters.

[Some online tutorial][2] shared about the drawbacks of DBI, then said Silhouette Coefficient can be an alternative solution. However, if we just look at the definition of DBI, Silhouette Coefficient and Calinski Harabasz Index, they share the same drawbacks for being better in convex clusters, being sensitive to outliers and ignoring the data distribution or data structure.


#### BIC
BIC (Bayesian Information Criterion) is often used in model selection, based on the maximum likelihood of model against parameters. In the case of clustering, BIC is trying to balance the maximum likelihood of model against `k`. At the same time, BIC adds penality to reduce overfitting. Lower BIC score is better. 


#### Estimated K Comparison
Now let's apply these k-estimation algorithms to our clusters.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/6_clusters.png" width="904" height="502" />

Here's the comparison code:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_estimate_k.png" width="891" height="748" />

🌻 [Check detailed implementation of each k-estimation algorithm here >>][3]

Let's take a look at the k-estimation results. Is elbow method really the worst? Obviously not! In the plot below, the line closer to the grey diagonal has k-estimator closer to the ground truth. So, elbow method has obviously better performance than other algorithms.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/k_estimate_comparison.png" width="760" height="660" />

🌻 [Check all the code here >>][3]

If we review this tutorial ["Are You Still Using the Elbow Method?"][1], all of its data have well separated blobs and each blob is a convex cluster, but such pleasant datasets are hard to find in the real world.

So what should you do in the future when estimating k for clustering problem? Lady H. suggests:
  * Elbow method is still a simple choice to start with. 
  * If you can code with Language R, Lady H. has experimented with 4 methods, one of them applies 30 k-estimation algorithms and returns the most voted k.  
    * 🌻 [See R code here >>][4]
    * Similarly, in python, you can apply multiple k-estimation algorithms and use the most voted k.
  * You can also consider other clustering algorithms rather than k-means.


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Resplendent Tree Home >>][6]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]


[1]:https://towardsdatascience.com/are-you-still-using-the-elbow-method-5d271b3063bd
[2]:https://www.linkedin.com/advice/0/what-some-challenges-limitations-cluster-analysis
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/unsupervised/estimate_clusters_count.ipynb
[4]:https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/Outliers_and_Clustering/finding_optimal_k.R#L91-L92
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/unsup1.md
[6]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/about_resplendent_tree.md#correlation--clustering