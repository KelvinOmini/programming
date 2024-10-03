from centering import mean_center, get_matrix

def covariance_matrix(X):
    n_samples = len(X)
    n_features = len(X[0])

    # Compute covariance matrix
    cov_matrix =  [[0 for _ in range(n_features)] for _ in range(n_features)]
    for i in range(n_features):
        for j in range(n_features):
            cov_matrix[i][j] = sum(X[k][i] * X[k][j] for k in range(n_samples)) / (n_samples - 1)

    return cov_matrix

X_centered = mean_center(get_matrix())
cov_matrix = covariance_matrix(X_centered)
print('Coveriance Matrix: ', cov_matrix)