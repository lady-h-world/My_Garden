### Finding Optimal K

There are many online data science tutorials in your world, how do you use them in your work? These tutorials do create lots of inspirations but Lady H. never fully trust them, so when she found something interesting, she will dive deeper into the theories behind and do experiment using different datasets. 

The idea of this experiment started from an article called ["Are You Still Using the Elbow Method?"][1]. In this article, the author compared several k-finding methods with 5 datasets containing clusters ranging from 2 to 25. The visualization is very persuasive, and he concluded that elbow method, a popular k-finding method performed worst. The datasets in this article are all well separated blobs, therefore Lady H. thought, what if the datasets are more complicated to find clusters, how would these methods perform?

Before looking at Lady H.'s experiments, let's understand how does each k-finding method work. To find the optimal k, the ideal result is, generated clusters have larger between-cluster variance and smaller within-cluster variance.


#### Elbow Method

Elbow method checks WCSS (Within-Cluster Sum of Square), the sum of the squared distance between data points in a cluster and the cluster centroid. We often choose the k at the elbow of its plot, meaning WCSS dropped most significantly at that point. We don't choose larger k with even smaller WCSS value is because that will create more clusters, which may not be necessary. 

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/plot_has_elbow.png" width="683" height="458" />

As we can see, elbow method doesn't measure between-cluster performance. Meanwhile, sometimes it can be challenging to find the right k on the plot.

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

DBI (Davies-Bouldin Index) measures the average similarity between each cluster and its most similar cluster. Calculating the similarity is to use the ratio of the within-cluster distance and the between-cluster distance. Therefore, when there's within-cluster distance and larger between-cluster distance, DBI is lower, indicating the better clustering result.

DBI is easy to calculate and interpret. However, it only considers the pairwise distances between cluster centroids and cluster members, the score can be sensitive to outliers, and ignored the data distribution or structure (such as clusters within a cluster, or non-linear relationship, etc.). It also makes false assumption that clusters share the same density and size, which is not true in many real world scenarios.

[1]:https://towardsdatascience.com/are-you-still-using-the-elbow-method-5d271b3063bd
