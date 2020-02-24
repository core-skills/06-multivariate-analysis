[Overview](./00_overview.md) |
[More Regression](./01_regression.md) |
[Dimensionality Reduction](./02_dimreduction.md) |
[Clustering and High-D Regression](./03_clusteringAndHigherD.md) |
[Partial Least Squares](./04_PLS.md)  |
[Closeout](./05_closeout.md)

# Feature Extraction and Dimensionality Reduction

## Variable selection as dimension reduction

| 15 min |
| ------ |

Selecting the best set of variables to build a model leads to many benefits:
* Better predictions
* Better model interpretability and explainability
* Lower computational cost of training
* Less impact from the curse of dimensionality

| :question: What could be an easy way to select the most useful variables?   |
| --------------------------------------------------------------------------- |

This is usually called feature or variable selection, and it can be run as a preprocessing step or during training. You can have an overview of different options in scikit-learn's documentation:

[scikit-learn.org/stable/modules/feature_selection.html](https://scikit-learn.org/stable/modules/feature_selection.html)

## Dimension reduction

| 75 min |
| ------ |

Dimension reduction of dimensionality reduction is a bit different to feature selection. Feature selection aims at selecting a subset of the input variables to improve predictions. Dimensionality reduction on the other hand doesn't necessarily keep the original variables unchanged, but transform them to create new, synthetic features that maximize the information content of the first features. The idea is to be able to drop even more variables than with feature selection.

### Component decomposition

| 20 min |
| ------ |

The idea behind component decomposition is to decompose a multivariate dataset into new components that better capture the patterns in the data.

The most famous and used method is the principal component analysis (PCA). It aims at finding successive orthogonal components that express a maximum amount of the variance in the data as a linear combination of the input variables.

Multiple methods exist based on this idea of decomposing a signal, like incremental PCA, kernel PCA, or independent component analysis (ICA). You can get an overview from scikit-learn's documentation:

[scikit-learn.org/stable/modules/decomposition.html](https://scikit-learn.org/stable/modules/decomposition.html)

Note that in scikit-learn, the PCA is implemented as a *transformer*.

### Manifold learning

| 10 min |
| ------ |

PCA is a linear dimensionality reduction method, which is also its limitation: what if our data shows some non-linear relationships? A PCA will lead to sub-optimal results.

Manifold learning corresponds to an ensemble of non-linear dimensionality reduction methods. A manifold is a generalization of a curved surface. We can think of our data as lying on a more or less complicated surface (for instance an "S" or a Swiss roll). A PCA is trying to find a planar surface that can represent those data, but that surface doesn't exist in that case. That's where manifold learning comes in handy, because its looking for a low-dimensional manifold that can describe as best as possible the high-dimensional data, without assuming a planar manifold.

The two most famous famous are the multidimensional scaling (MDS), which uses as input a value of distance between the samples and finds coordinates that reproduce as best as possible those distances, and the t-distributed stochastic neighbor embedding (t-SNE), which constructs probability distributions so that similar samples have a high probability of being close to one another.

MDS, like PCA, is usually good at preserving the global structure of the data, at the expense of losing the local structures. t-SNE does the opposite, it better preserves the local structures but the global structure is not explicitly preserved. Also, MDS and t-SNE can be computationally expensive, contrary to PCA.

Other methods exist based on the idea of finding a low-dimensional manifold containing the data, like Isomap or UMAP. You can get an overview from scikit-learn's documentation:

[scikit-learn.org/stable/modules/manifold.html](https://scikit-learn.org/stable/modules/manifold.html)

You can find an in-depth and interactive discussion about t-SNE and its parameters here:

[distill.pub/2016/misread-tsne/](https://distill.pub/2016/misread-tsne/)

### Exercise: The Octane dataset

| 25 min |
| ------ |

Open [am2-dimreduction.ipynb](../notebooks/am2-dimreduction.ipynb) and go through the notebook.

[Overview](./00_overview.md) |
[More Regression](./01_regression.md) |
[Dimensionality Reduction](./02_dimreduction.md) |
[Clustering and High-D Regression](./03_clusteringAndHigherD.md) |
[Partial Least Squares](./04_PLS.md)  |
[Closeout](./05_closeout.md)
