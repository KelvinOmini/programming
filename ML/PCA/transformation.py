from Eigen import dot_product, eigenvector
from covariance import X_centered

def project_data(X, eigenvector):
    return [[dot_product(row, eigenvector)] for row in X]

# Project the data onto the first principle component
x_pca = project_data(X_centered, eigenvector)
print('PCA Transformed Data (1D):', x_pca)
