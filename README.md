# Core skills program - week 4 - multivariate analysis and dimensionality reduction

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/core-skills/04-multivariate-analysis.git/master)

The aim of today's session will be to generalize the concepts for unidimensional data we learnt about last week to multidimensional data types.  We'll also introduce approaches to reduce the dimensionality of a dataset - that is (a) how we can identify when a dataset can be represented accurately with a smaller number of variables, and (b) how we can identify the variables that contain the most information, with techniques like Principal Components Analysis (PCA) and clustering.  We'll touch on applying regression on dimension-reduced data, and Partial Least Squares Regression (PLSR, and also called Projection to Latent Structures).  These multivariate methods can be very powerful in situations where you need to create models with many variables, but you have few observations to work with and it happens that the variables are correlated.  This is often the case with datasets from multichannel instruments. 

You should aim to understand the similarities and differences between univariate and multivariate data settings (you'll still need to be able to apply EDA on multivariate data for example). You should also aim to understand the basis of dimensionality reductions, execute measures of correlations, as well as understanding when correlations might be spurious.

## Pre-session Reading & Resources

Topics that we'll be discussing in today's workshop include:

[sklearn.linear_model.LinearRegression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

[Robust Regression](http://scikit-learn.org/stable/modules/linear_model.html#robustness-regression-outliers-and-modeling-errors)

Template Regression:  I haven't found a good explanation of this without lots of maths appearing.  But if you're comfortable with linear algebra then this is an example of "basis function" regression.  We'll be discussing this on the whiteboard during the workshop, using the idea that a linear system is one where the whole is literally the sum of the parts. When we solve the linear system then the coefficients in linear regression are how much of each part is present, and the parts don't have to be simple variables like "x" or "y" they can be squiggly lines that represent components that we believe we can decompose our observations into.  These components are represented as vectors and can take on any shapes we want.

[Principal Component Analysis](https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html)
Unfortunately most descriptions of the theory of PCA and regression following transformation to principal components become very mathematical quickly.  But this link is practical and shows how PCA works in 2D.


*Extension reading:*

When dealing with multivariate data there is risk of us finding spurious correlations.  That is, the bigger our datasets become the more likely it is that we'll see relationships appearing my chance alone.  In machine learning we mostly deal with by cross-validation and other methods that judge methods that we use by how well they predict on new data previously unseen by the model.  

Tyler Vigen has an amusing site which finds spurious correlations in US statistical data (covered in the [Harvard Business Review](https://hbr.org/2015/06/beware-spurious-correlations). Have a play here: http://www.tylervigen.com/spurious-correlations

You'll also see a lot about 'correlation isn't causation' - however this phrase is often overstated. We can construct statistical models which invoke causation although it requires some new statistical tools to cover _interventions and counterfactuals_. These allow us to answer questions along the lines of 'what would happen if?'. Judea Pearl is a researcher who has done a lot of work into the statistics of causation (i.e. how we can make machines that reason causally like humans) and he has just released a very readable book on this topic recently [_The Book of Why_](https://www.amazon.com/Book-Why-Science-Cause-Effect/dp/046509760X) which is well worth a look.
