### Finding Optimal K

There are many online data science tutorials in your world, how do you often use them? These tutorials do create lots of inspirations but Lady H. never fully trust them, so when she found something interesting, she will dive deeper into the theories behind and validate with more experiments. 

The idea of this experiment started from an article called ["Are You Still Using the Elbow Method?"][1]. In this article, the author compared several k-estimation algorithms with 5 datasets containing clusters ranging from 2 to 25. The visualization is very persuasive, and he concluded that elbow method, a popular k-estimation algorithm performed the worst. The datasets in this article are all well separated blobs, therefore Lady H. thought, what if the datasets are more complicated, how would these algorithms perform?

Before looking at Lady H.'s experiments, let's understand how does each k-estimation algorithm work. To find the optimal k, the ideal result is, the generated clusters have larger between-cluster variance and smaller within-cluster variance.


#### Elbow Method

Elbow method checks WCSS (Within-Cluster Sum of Square), the sum of the squared distance between data points in a cluster and the cluster centroid. We often choose the k at the elbow of its plot, meaning WCSS dropped most significantly at that point. We don't choose larger k with even smaller WCSS value is because that will create more clusters, which may not be necessary. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/plot_has_elbow.png" width="683" height="458" />

As we can see, elbow method doesn't measure between-cluster performance. Meanwhile, sometimes it can be challenging to find the right k on the plot, like the example below.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/plot_no_elbow.png" width="682" height="460" />


#### Calinski Harabasz Index

Calinski Harabasz Index is also known as Variance Ratio Criterion. `Calinski Harabasz Index = sum(between_cluster dispersion) / sum(within_cluster dispersion)`, dispersion is the sum of squared distances. Higher value indicates better clustering, since that requires larger between-cluster variance and smaller within-cluster variance.

Calinski Harabasz Index is fast to compute. It tends to have better k estimation on convexed, dense and well separated clusters. 

Do you know what does "convex" mean to clusters?
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/notes/convex_cluster.png" width="766" height="79" />
</p>

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/convex_example.png" width="494" height="239" />


#### Davies-Bouldin Index

DBI (Davies-Bouldin Index) measures the average similarity between each cluster and its most similar cluster. Calculating the similarity uses the ratio of the within-cluster distance and the between-cluster distance. Therefore, when there's smaller within-cluster distance and larger between-cluster distance, DBI is lower, indicating a better clustering result.

DBI is easy to calculate and interpret. However, it only considers the pairwise distances between cluster centroids and cluster members, the score can be sensitive to outliers, and ignored the data distribution or structure (such as clusters within a cluster, or non-linear relationship, etc.). It also makes false assumption that clusters share the same density and size, which is not true in many real world scenarios.


#### Silhouette Coefficient

Silhouette Coefficient is a measure of how similar an object is to its own cluster comparing to other clusters. `Silhouette Coefficient = (b-a)/max(a,b)`, `a` is the average distance between each point within a cluster, `b` is the average distance between clusters. Its value is between 1 and -1, higher the better, 0 means overlapping clusters.

[Some online tutorial][2] shared about the drawbacks of DBI, then said Silhouette Coefficient can be an alternative solution. However, if we just look at the definition of DBI, Silhouette Coefficient and Calinski Harabasz Index, they share the same drawbacks for being better in convex clusters, being sensitive to outliers and ignoring the data distribution or data structure.


#### BIC

BIC (Bayesian Information Criterion) is often used in model selection, based on the maximum likelihood of model against parameters. In the case of clustering, BIC is trying to balance the maximum likelihood of model against `k`. At the same time, BIC adds penality to relief overfitting. Lower BIC score is better. 


#### Estimated K Comparison

Now let's apply all the k-estimation algorithms mentioned above to our clusters.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/6clusters.png" width="911" height="514" />

Here's the comparison code:
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/estimate_k_code.png" width="895" height="759" />

🌻 [Check detailed implementation of each k-estimation algorithm here >>][3]

Let's take a look at the k-estimation results. Is elbow method really the worst like some online tutorial said? Obviously not! The line closer to the grey diagonal has k-estimator closer to the ground truth. Elbow method has obvious better performance than other algorithms.
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/k_estimate_comparison.png" width="760" height="660" />

If we review this tutorial ["Are You Still Using the Elbow Method?"][1], all of its data have well separated blobs and each blob is a convex cluster. Such cases are ideal for other algorithms work well, but in reality, it's hard to find such pleasant datasets. In more complex situations, such as the circles, moons datasets, other algorithms worked much worse than elbow method.

So what should you do in the future when estimating k for clustering problem? Lady H. suggests:
  * Elbow method is still a safe choice to start with. 
  * If you're coding with Language R, Lady H. has experimented with 4 methods, one of them applied 30 k-estimation algorithms and returned the most voted k.  
    * 🌻 [See code here >>][4]
  * You can also consider other clustering algorithms, cuz the problem might be on k-means.


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