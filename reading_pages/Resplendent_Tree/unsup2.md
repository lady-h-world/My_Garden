### Finding Optimal K

There are many online data science tutorials in your world, how do you use them in your work? These tutorials do create lots of inspirations but Lady H. never fully trust them, so when she found something interesting, she will dive deeper into the theories behind and do experiment using different datasets. 

The idea of this experiment started from an article called ["Are You Still Using the Elbow Method?"][1]. In this article, the author compared several k-finding methods with 5 datasets containing clusters ranging from 2 to 25. The visualization is very persuasive, and he concluded that elbow method, a popular k-finding method performed worst. The datasets in this article are all well separated blobs, therefore Lady H. thought, what if the datasets are more complicated to find clusters, how would these methods perform?

Before looking at Lady H.'s experiments, let's understand how does each k-finding method work. To find the optimal k, the ideal result is, generated clusters have smaller within-cluster point distances and larger between-cluster point distances.

#### Elbow Method

Elbow method checks WCSS (Within-Cluster Sum of Square), the sum of the squared distance between data points in a cluster and the cluster centroid. We often choose the k at the elbow of its plot, meaning WCSS dropped most significantly at that point.


[1]:https://towardsdatascience.com/are-you-still-using-the-elbow-method-5d271b3063bd
