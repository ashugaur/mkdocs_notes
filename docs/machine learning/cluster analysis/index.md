---
title: Cluster analysis
hide:
    # - navigation
    # - toc
    - footer
---


## Overview

!!! segment ""

    Clustering is the process of breaking down data into groups consisting of similar data points or elements.


## Assumptions

!!! segment ""

    - The variables in cluster analysis are typically continuous in nature.
    - The best cluster analysis can do is identify clusters numerically. It cannot identify them substantively. What this means is that cluster analysis can only tell you of possible groups that may exist in your data, but cannot on its own tell you why these groups might exist or their underlying etiology.


## Models

### Affinity Propagation

!!! segment ""

    Affinity propagation uses graph distance.

### Centroid based

#### Agglomerative

!!! segment ""

    Hierarchical clustering algorithms can be either bottom-up or top-down.

    - In bottom-up algorithms or `agglomerative clustering`, each datapoint is treated as a separate cluster with a single object. These clusters are then successively merged until all the clusters are merged into a single giant cluster.
    - On the other hand, top-down algorithms start with a giant cluster and successively split these clusters until individual datapoints are reached.
    - Distance between cluster and a point is done by using linkages (dissimilarity matrix). Ward linkage is one of the methods to do so.
    - The visual representation of combination of these clusters is known as a dendogram.

#### BIRCH

!!! segment ""

    - Uses Euclidian distance to know which point belongs to a particular cluster.
    - Good for detecting outlies in the dataset.
    - Incrementally process incoming data and update clusters.
    - Does not scale will to high dimensional (every record with large number of features) data.

#### Hierarchical

!!! segment ""

    Connectivity based clustering based on the core idea that points are connected to points close by rather than further away. There is no central mean or reference vector to which distances are calculated.

    Algorithms do not partition the dataset but instead ../construct a tree of points which are typically merged together to form clusters. This tree diagram used to illustrate arrangement of clusters produced by hierarchical clustering is called a dendrogram. Work well with large datasets.

    1. Start with t clusters each with 1 point i.e. each point is its own cluster
    2. Algorithm goes ahead and merges 2 clusters i.e. points closest to each other to form 1 cluster. This process is repeated over and over again. As the process continues the number of clusters keeps reducing.
    3. Agglomerative is starting with many one point clusters and end up with a big cluster. Divisive is start with 1 big cluster and end with many 1 point clusters.



#### K Means clustering

!!! segment ""

    K-Means is a clustering approach in which the data is grouped into K distinct non-overlapping clusters based on their distances from the K centers. K refers to the number of clusters that you want your data to be grouped into. The value of K needs to be specified first and then the algorithm assigns the points to exactly one cluster.

    - Points in the same group are similar as possible.
    - Points in different groups are as dissimilar as possible.
    - Data/variables used to build K-means models should always be
        - Numeric (convert categorical data to numeric, use one hot encoding)
        - On the same scale, e.g. Z transform

    1. Randomly assign centroid values for each cluster. k-means++ which selects the initial centroids so that they are statistically close to the final ones.
    2. Calculate the distance (Euclidean or Manhattan) between each data point and centroid values of all the clusters.
    3. Assign the data point to the cluster of the centroid with the shortest distance.
    4. Calculate and update centroid values based on the mean values of the coordinates of all the data points of the corresponding cluster.
    5. Repeat steps 2-4 until new centroid values for all the clusters are different from the previous centroid values. `Stable solution`, a solution where after successive iterations, no point changes its class membership or cluster membership.


    ##### Value of K

    How to find optimum number of clusters? Calculate some measure of average cluster compactness for a series of values of clusters.

    WSS or Within Sum of Squares measure the compactness of the cluster. Computing the total squared distance of each point of this cluster from its cluster centre.

    Scree plot or elbow plot helps estimate total within SS (sum of square measure) for each value of K through a plot to get an idea on the optimum number of clusters. E.g. Decrease in WSS is not substantial after around 8 clusters.


### Density based

#### DBSCAN

!!! segment ""

    DBSCAN or Density-Based Spatial Clustering of applications with noise is a powerful algorithm that can easily solve non-convex problems where k-means fails. The idea is simple: A cluster is a high-density area (there are no restrictions on its shape) surrounded by a low-density one. This statement is generally true, and doesn’t need an initial declaration about the number of expected clusters. The procedure starts by analysing a small area (formally, a point surrounded by a minimum number of other samples). If the density is enough, it is considered part of a cluster. At this point, the neighbours are considered. If they also have a high density, they are merged with the first area; otherwise, they determine a topological separation. When all the areas have been scanned, the clusters have also been determined because they are islands surrounded by empty space.



#### Mean shift

!!! segment ""

    Mean shift clustering considers the distribution of datapoints as a probability-density function and tries to find the modes in the feature space. These modes are basically points corresponding to local maxima. The main advantage of mean shift algorithm is that we are not required to know the number of clusters beforehand.

    - Uses pair-wise distances between points to form clusters.
    - Computationally intensive and not very scalable.
    - Good for small datasets where we want to have large number of clusters.


### Distribution based

!!! segment ""

    Built on statistical distribution models.

#### Gaussian Mixture Models


### Spectral clustering

!!! segment ""

    Spectral clustering is a more sophisticated approach based on a symmetric affinity matrix.


## Model Validation

!!! segment ""

    These scores tell us about actual and predicted values & help choose number of clusters. Homogeneity, Completeness & V-measure are closely related.


    ### Homogeneity

    !!! segment ""
    
        Every cluster should contain members that belong to the same class. A value of 0.8 means that there's a residual uncertainty of about 20% because one or more clusters contain some points belonging to a secondary class.


    ### Completeness

    !!! segment ""

        All members of a class should lie in the same cluster. A high value means that the majority of samples belonging to a class have been assigned to the same cluster.

    ### V-measure score

    !!! segment ""

        v-measure is the harmonic mean of homogeneity and completeness. Harmonic mean is closer to lower of the two metrics. Harmonic mean favours even weightage to both metrics.

        v-measure = 2 * ((homogeneity*completeness) / (homogeneity*completeness))

        Homogeneity, Completeness and v-measure are bounded scores between 0 & 1. Higher values are better. -ive values require labelled data.

        Homogeneity & Completeness are inversely related. They are similar to precision and recall. They need a metric to optimize trade off, this is the v-measure score.

    ### Adjusted Rand Index (ARI)

    !!! segment ""

        * Measures similarity between labels and assigned clusters.
        * Adjusted for probability of correct labelling by chance.
        * Value between -1 and 1.
            * 1 means actual and predicted clusters are identical.
            * 0 indicates that data was randomly labelled.
        * Needs labelled data.
        * As the adjusted rand score is bounded between -1.0 and 1.0, with negative values representing a bad situation (the assignments are strongly uncorrelated), a score of 0.83 means that the clustering is quite similar to the ground truth.


    ### Adjusted Mutual Info

    !!! segment ""

        * Adjusted mutual information is the information obtained about one random variable by observing another random variable adjusted to account for chance. Measure of mutual information overlap between cluster assignments. So, the changes in variable affect another or is it just by chance.
        * 1 actual and predicted clusters are identical.
        * 0 means assignment of clusters has been done at random i.e. labels and clusters are independent.


    ### Silhouette

    !!! segment ""

        - The silhouette score is based on the principle of `maximum internal cohesion and maximum cluster separation`. In other words, we would like to find the number of clusters that produce a subdivision of the dataset into dense blocks that are well separated from each other.
        - Silhouette coefficient uses a distance metric to measure how similar a point is to its own cluster and how dissimilar the same point is form points in other clusters. Overall silhouette score averages silhouette coefficient of each sample.
        - Only this can be calculated without labelled data i.e. it works on features.
        - Score ranges between -1 & 1.
            - Score close to 1 indicate clustering was good.
            - A value close to 0 means that the difference between intra and inter cluster measures is almost null and therefore there's a cluster overlap.
            - A value close to -1 means that the sample has been assigned to a wrong cluster.


    ### Calinski-Harabasz index

    !!! segment ""

        Another method that is based on the concept of dense and well-separated clusters is the Calinski-Harabasz index. The Calinski-Harabasz index is defined as the ratio between BCD (inter-cluster dispersion, k) and WCD (intra-cluster dispersion, k). We look for a low intra-cluster dispersion (dense agglomerates) and a high inter-cluster dispersion (well-separated agglomerates), we need to find the number of clusters that maximizes this index. Higher values indicate better defined (more separated) clusters.


    ### Davies Bouldin Score

    !!! segment ""

        It is is the ratio of within-cluster distances (distances between points in a cluster) to the between cluster distances (distances between points in different clusters). Values closer to zero indicate better partitions between clusters.




## Relationship with other analysis

!!! segment ""

    - The idea of “within” vs. “between” variation is central to cluster analysis as it is to ANOVA.
    - ANOVA or discriminant analysis are not used as much in the spirit of “shooting in the dark” as is cluster analysis. We are unaware of group membership. This is the exact reason why we are performing the cluster analysis. In contrast, in ANOVA, MANOVA, and discriminant analysis, group membership has already been defined on one or more variables.
    - In ANOVA, the researcher presumably has a theory as to why groups may be different, which is expressed as a factor with levels on the independent variable. How about a discriminant analysis? Since a discriminant analysis is essentially an ANOVA or MANOVA flipped around, group membership is now a response variable because we are attempting to predict the classification into one group vs. the other.


## Reference

!!! bookmark-outline "&nbsp;"

	!!! border-radius "Issues"

		:	[`Issues with Tableau`](http://vizdiff.blogspot.com/2020/10/analysis-of-tableaus-multi-variable.html){target="_blank"}
