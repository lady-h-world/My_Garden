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
The Davies-Bouldin Index (DBI) measures the average similarity between each cluster and the cluster that is most similar to it. Similarity is calculated using the ratio of within-cluster distance to between-cluster distance. A lower DBI indicates better clustering, as it reflects smaller within-cluster distances and larger between-cluster distances.

DBI is straightforward to calculate and interpret. However, it only considers pairwise distances between cluster centroids and their members, making it sensitive to outliers and neglectful of data distribution or structure (e.g., nested clusters or non-linear relationships). Additionally, it assumes clusters have similar density and size, which is often not the case in real-world scenarios.


#### Silhouette Coefficient
Silhouette Coefficient is a measure of how similar an object is to its own cluster comparing to other clusters. `Silhouette Coefficient = (b-a)/max(a,b)`, `a` is the average distance between each point within a cluster, `b` is the average distance between clusters. The coefficient ranges from -1 to 1, with higher values indicating better clustering and 0 suggesting overlapping clusters.

[Some online tutorial][2] shared about the drawbacks of DBI, then said Silhouette Coefficient can be an alternative solution. However, if we just look at the definition of DBI, Silhouette Coefficient and Calinski Harabasz Index, they share the same drawbacks for being better in convex clusters, being sensitive to outliers and ignoring the data distribution or data structure.


#### BIC
The Bayesian Information Criterion (BIC) is commonly used for model selection and is based on the maximum likelihood of a model given its parameters. In clustering, BIC seeks to balance the model’s maximum likelihood with the number of clusters, `k`, while applying a penalty to prevent overfitting. A lower BIC score indicates a better model fit.


#### Estimated K Comparison
Now let's apply these k-estimation algorithms to our clusters.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/6_clusters.png" width="904" height="502" />

Here's the comparison code:

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_estimate_k.png" width="891" height="748" />

🌻 [Check detailed implementation of each k-estimation algorithm here >>][3]

Let's take a look at the k-estimation results. Is elbow method really the worst? Obviously not! In the plot below, the line closer to the grey diagonal has k-estimator closer to the ground truth. So, elbow method has obviously better performance than other algorithms.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/k_estimate_comparison.png" width="760" height="660" />

🌻 [Check all the code here >>][3]

In reviewing the tutorial ["Are You Still Using the Elbow Method?"][1], all the datasets it uses contain well-separated blobs, with each blob forming a convex cluster. However, such ideal datasets are rare in real-world applications.

So what should you consider when estimating `k` for clustering problems in the future? Lady H. suggests:
    * The elbow method remains a simple and effective starting point.
    * The elbow method remains a simple and effective starting point.
    * If you’re familiar with coding in R, Lady H. has experimented with four methods—one of which applies 30 k-estimation algorithms and returns the most frequently selected `k`.
        * 🌻 [See R code here >>][4]
    * Similarly, in Python, you can apply multiple k-estimation algorithms and select the most frequently recommended `k`.
    * Additionally, consider exploring clustering algorithms beyond k-means.


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