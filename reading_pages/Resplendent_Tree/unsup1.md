## Clustering - Finding Optimal K

As most of you know, clustering is an unsupervised machine learning technique, it groups data without any data label. A popular topic in clustering is to decide `k`, the number of clusters. Now we are going to explore different methods that helps decide the optimal value of k.


### About the Data

So far, all the data you have seen were delivered by [Crystal Ball][1] through searches in the universe 😉. It can also generate data from its own to mimic real world scenarios, and we call this process as "data simulation". With data simulation, we can experiment on more kinds of data conditions. The clustering data here is simulated data.

Python sklearn provides built-in methods to simulate different types of clusters. For example, see the code below, we can create clusters in the shape of circles, moons and blobs. For circles and moons, it only supports 2 clusters, but for blobs, there is more flexibility to specify the number of clusters and the density of each cluster.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_clusters_simulate.png" width="1268" height="931" />

🌻 [Check clusters simulation code here >>][2]

Now let's see different clusters Lady H. simulated. The main differences are in created blobs. In the 3rd, 4th, 6th plots, clusters share similar standard deviation and they are more separated from each other, but in the 5th plot, clusters are more mixed together. The circles and the moons are special shapes, even though from the plot, we can see the separation of clusters clearly, they are challenging for some popular clustering algorithms to differentiate, such as distance based algorithms like k-means.

<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Resplendent_Tree_images/code_clusters.png" width="1260" height="853" />

🌻 [Check purposeful clusters simulation code here >>][3]

With these purposefully simulated clusters, let's explore more on finding the optimal number of clusters `k`.


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Keep going >>][4]

<p align="right">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/going_back.png" width="60" height="44" />
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<< Looking back][5]
 



[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Crystal_Ball/about_crystal_ball.md
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/crystal_ball/data_collector/simulate_clusters.ipynb
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/resplendent_tree/unsupervised/estimate_clusters_count.ipynb
[4]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/unsup2.md
[5]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Resplendent_Tree/about_resplendent_tree.md