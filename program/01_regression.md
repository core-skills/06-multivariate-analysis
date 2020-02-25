[Overview](./00_overview.md) |
[More Regression](./01_regression.md) |
[Dimensionality Reduction](./02_dimreduction.md) |
[Clustering and High-D Regression](./03_clusteringAndHigherD.md) |
[Partial Least Squares](./04_PLS.md)  |
[Closeout](./05_closeout.md)

# More Regression

## Review of outliers and robust regression

We will begin with a refresher on what we covered last time by implementing a linear and robust regession. Remember that robust regression is useful when there are outliers in the data.

This morning we recommend working through these first two exercises using pair programming and practicing code-sharing workflows.

### Robust regression with seaborn

| 10 min |
| ------ |

Open [am1_more_regression](../notebooks/am1_more_regression.ipynb) and start Exercise 1 with your partner. 

| :triangular_flag_on_post: If you finish this section, start the next section. After 10 minutes, we will go this section on using Seaborn to fit a linear regression model as a group.|
| ------------------------------------------------------------ |


### Robust regression with scikit-learn

| 10 min |
| ------ |

Continue Exercise 1 in [am1_more_regression](../notebooks/am1_more_regression.ipynb).

| :triangular_flag_on_post: If you finish this section, start the next section. After 10 minutes, we will go through the section on using scikit-learn to fit a robust regression model as a group. |
| ------------------------------------------------------------ |



## Multivariate regression

| 15 min |
| ------ |

Multivariate regression is an extension of linear regression, often called a *general linear model*, where there is more than one explanatory variable that can be used.

A good example of the benefits and pitfall of using multivariate regression is on [Towards Data Science ](https://towardsdatascience.com/data-science-simplified-part-5-multivariate-regression-models-7684b0489015).

### Linear systems: Recognize a linear problem

Up until now we have been using linear regression to fit a line to a set of data. A line is a *linear model* defined by an equation of the form

y = m*x + b + &epsilon;

where m is the slope and b is the intercept. The &epsilon; is an error term representative of what we have been calling residuals (difference between our observations and predictions) where most of the assumptions of linear regression must be met (see [Models & Regression](../../05-simple-predictions/program/01_modelsregression.md) to review assumptions).


This equation can be re-written in linear algebra friendly notation as

y = &beta;<sub>0</sub> + &beta;<sub>1</sub>x

where &beta;<sub>0</sub>  is the intercept and &beta;<sub>1</sub> is the slope. The &beta;<sub>i</sub> are the coefficients we solve for in linear regression and x is the sole explanatory variable (N=1).
 
 When there are multiple explanatory variables, the data are considered to be of higher-dimension.

In the case of two (N=2) explanatory variables and one dependent variable, we can use linear regression to fit a plane to the data in three-dimensional space. A plane is a *linear model* defined by an equation of the form

y = &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + &beta;<sub>1</sub>x<sub>2</sub>

where we now have three &beta;<sub>i</sub> coefficients that define our model with two explanatory variables: x<sub>1</sub> and x<sub>2</sub>.

 A more general expression of a linear model for multiple (N) explanatory variables is of the form

y = &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + &beta;<sub>1</sub>x<sub>2</sub> + ... + &beta;<sub>i</sub>x<sub>i</sub> + &beta;<sub>N</sub>x<sub>N</sub>

In this general case we solve for the &beta; regression coefficients (there are N+1 of them). And this is where the idea of a linear model comes in: the *linear model* is simply a linear combination (addition) of the regression coefficient, &beta;<sub>i</sub>, terms.

The techniques we will cover today work on these higher-dimensional data. For higher dimensional data it can be difficult to visualize how to fit a *linear model* to our data.

| :triangular_flag_on_post: Takeaway: Linear model: Each &beta;x is a piece of the model, and when we sum up the pieces (additivity), we get the whole model. |
| ------------------------------------------------------------ |


### Validating a Multivariate Regression Model

### Analysing the statistical results

### Missing data

In some cases, we have missing data that will actually bias our regression results. If possible, we would like to try and account for this.

[6 Different Ways to Compensate for Missing Values In a Dataset (Data Imputation with examples)](https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779)

## Basis function regression using templates

| 30 min |
| ------ |

The explanatory variables, x, in the general linear model can be numbers or functions.

y = &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + &beta;<sub>1</sub>x<sub>2</sub> + ... + &beta;<sub>i</sub>x<sub>i</sub> + &beta;<sub>N</sub>x<sub>N</sub>

We have already seen a case where the explanatory variables are *basis functions* when we discussed polynomial regression. The x can represent a range of functions, and in this example the explanatory variables represent *kernel* functions. Do not worry too much about what the kernel function is; the key thing in this type of regression problem is that we know what these functions look like.  What we are interested in is understanding how much (&beta;) of each is present in our observations (y).

The example we will use is spectral data where we have a good understanding of the spectral response (x) of each component (&beta;x) that contributes to our overall observations (y). What we would like to solve for is how much (&beta;) of each component is present.

Let's go through Exercise 2 in [am1_more_regression]((../notebooks/am1_more_regression.ipynb)).

| :triangular_flag_on_post: Is everyone up to speed? How are people going? |
| ------------------------------------------------------------------------ |

[Overview](./00_overview.md) |
[More Regression](./01_regression.md) |
[Dimensionality Reduction](./02_dimreduction.md) |
[Clustering and High-D Regression](./03_clusteringAndHigherD.md) |
[Partial Least Squares](./04_PLS.md)  |
[Closeout](./05_closeout.md)
