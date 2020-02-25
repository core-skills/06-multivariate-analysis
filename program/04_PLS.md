[Overview](./00_overview.md) |
[More Regression](./01_regression.md) |
[Dimensionality Reduction](./02_dimreduction.md) |
[Clustering and High-D Regression](./03_clusteringAndHigherD.md) |
[Partial Least Squares](./04_PLS.md)  |
[Closeout](./05_closeout.md)

# PLS Regression

| 30 min |
| ------ |

PLS regression stands for partial least squares regression, another useful approach when dealing with multivariate problems, especially ill-conditioned ones.

## PLS Regression vs PCA regression

| 10 min |
| ------ |

Both PLS and PCA regressions defines new, uncorrelated variables (components) as a linear combination of the original variables as to maximize the variability observed in the data. PCA regression does so by considering the input variables only, whereas PLS regression also considers the output variables and tries to maximize the covariance between inputs and outputs. This can lead to better fits with fewer components, but PLS regression is also a useful approach when there are more variables than observations or multicollinearity between the input variables.

## Exercise

| 20 min |
| ------ |

Open [am2-PLS.ipynb](../notebooks/am2_PLS.ipynb) and go through the notebook.

[Overview](./00_overview.md) |
[More Regression](./01_regression.md) |
[Dimensionality Reduction](./02_dimreduction.md) |
[Clustering and High-D Regression](./03_clusteringAndHigherD.md) |
[Partial Least Squares](./04_PLS.md)  |
[Closeout](./05_closeout.md)
