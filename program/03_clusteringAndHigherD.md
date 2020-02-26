[Overview](./00_overview.md) |
[More Regression](./01_regression.md) |
[Dimensionality Reduction](./02_dimreduction.md) |
[Clustering and High-D Regression](./03_clusteringAndHigherD.md) |
[Partial Least Squares](./04_PLS.md)  |
[Closeout](./05_closeout.md)

# Clustering and Regression in Higher Dimensions

Clustering and multivariate regression are useful techniques with high-dimensional data. We will build upon the use of Principal Component Analysis, and illustrate some cases where it can be used in combination with clustering. 

The aim of clustering is to group a set of observations based on similarities. There are a substantial number of techniques that have been developed to group data into clusters.

## Clustering background

| 15 min |
| ------ |

The aim of clustering is to group a set of observations based on similarities. There are a substantial number of techniques that have been developed to group data into clusters.

Scikit-learn has a nice overview of built-in [clustering](https://scikit-learn.org/stable/modules/clustering.html) functionality.

### K-means clustering
A commonly used method is K-means clustering, and we will spend half of this session learning how to apply K-means clustering to data.

The *K* in K-means refers to the number of clusters one wants to identify in the data. In practice, this is usually specified in advance.

A general K-means clustering algorithm works in the following way:
- K points called centroids are randomly initialised in the data space
- Data points close to the centroid are assigned to that cluster'
- The centroid location is then calculated based on the data that has been assigned to the cluster
- The centroid is iteratively updated like this, moving it towards the center of each cluster
- The process is stopped when there are no further changes in the centroid values
- The centroids are taken to be representative of the clusters.

[Understanding K-means clustering in machine learning](https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1)

### Hierarchical clustering

Hierarchical clustering works using a measure of similarity between observations. The choice of the similarity measure depends on the problem.

Data values start all in one cluster and splits are carried out recursively using different linkage criteria. This process is represented using a dendogram.

[Hierarchical clustering example](https://towardsdatascience.com/machine-learning-algorithms-part-12-hierarchical-agglomerative-clustering-example-in-python-1e18e0075019)

### Spectral clustering

Spectral clustering is an advanced technique for clustering. It is called ‘spectral’ because it uses a spectral decomposition of a similarity matrix

The key idea of spectral clustering is to cluster the raw data using the eigenvectors of the similarity matrix. 

## Exercise 1: K-means clustering in scikit-learn

| 30 min |
| ------ |

Open the notebook [pm1_clustering.ipynb](../notebooks/pm1_clustering.ipynb) and go through Exercise 1.

The first exercise consists of two examples of applying k-means clustering to PCA data; one on a synthetic dataset and the other on the Octane dataset used earlier.

## Checkpoint
| :triangular_flag_on_post: Is everyone up to speed? How are people going? |
| ------------------------------------------------------------------------ |

| 10 min  |
| ------ |

## Exercise 2: Principal Components Regression

| 30 min |
| ------ |

The second exercise is to apply principal components regression to the Octane dataset. 

As part of this exercise, we will revisit model validation. See the [pm1-linear-models-II_filled](../../05-simple-predictions/notebooks/pm1-linear-models-II_filled.ipynb) notebook for a refresh.

Continue going through Exercise 2 in the notebook [pm1_clustering.ipynb](../notebooks/pm1_clustering.ipynb).


## Wrap-up

| 5 min |
| ------ |

| :triangular_flag_on_post: Is everyone up to speed? How are people going? |
| ------------------------------------------------------------------------ |

[Overview](./00_overview.md) |
[More Regression](./01_regression.md) |
[Dimensionality Reduction](./02_dimreduction.md) |
[Clustering and High-D Regression](./03_clusteringAndHigherD.md) |
[Partial Least Squares](./04_PLS.md)  |
[Closeout](./05_closeout.md)
