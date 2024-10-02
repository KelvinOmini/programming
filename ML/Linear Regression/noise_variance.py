from Least_Squares import matrix_multiply
from MLE import optimal_theta

# FUnction to compute the residual sum of squares (RSS)
def residual_sum_of_squares(X, y, theta):
    N = len(y)
    RSS = 0
    for i in range(N):
        y_pred = sum(X[i][j] * theta[j][0] for j in range(len(theta))) # predict y_n
        RSS += (y[i][0] - y_pred) ** 2 #(y_n - y_pred)^2
    return RSS

# Function to estimate noise variance sigma^2
def estimate_noise_variance(X, y, theta):
    N = len(y)
    D = len(X[0]) # Number of features/Parameters
    RSS = residual_sum_of_squares(X, y, theta)
    sigma_squared = RSS / (N - D) # Unbiased estimate of variance
    return sigma_squared

X = [[1, 2], [3, 4], [5, 6]]  # N x D matrix (3 samples, 2 features)
y = [[7], [9], [11]]           # N x 1 target vector (3 samples)

# Compute the optimal theta
theta_opt = optimal_theta(X, y)

# Estimate the noise variance sigma^2
sigma_squared = estimate_noise_variance(X, y, theta_opt)
print(f"Estimated noise variance (sigma^2): {sigma_squared}")