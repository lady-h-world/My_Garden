### UMAP

UMAP (Uniform Manifold Approximation and Projection) is a dimensional reduction method that considers both local the global structures when it's trying to project the data into a lower dimensional space. To preserving the local structures, it builds a neighborhood graph by considering the varying distances between different densities, local connectivity with different levels of certainties, and the edge weights between connected points. Then when projecting the data to a lower dimensional space, it uses global euclidean distance to control the minimum spread of points, and looking for optimal edge weights that can minimize the cross entropy through stochastic gradient descent. For more details, [check here][1].

[1]:https://towardsdatascience.com/umap-dimensionality-reduction-an-incredibly-robust-machine-learning-algorithm-b5acb01de568
