import math

class BayesianLinearRegression:
    def __init__(self, sigma_y2, sigma_theta2):
        self.sigma_y2 = sigma_y2  # Variance of observation noise
        self.sigma_theta2 = sigma_theta2  # Prior variance of parameters
        self.posterior_mean = None
        self.posterior_cov = None

    # Matrix multiplication (works for any n x n matrix)
    def matrix_multiply(self, A, B):
        return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

    # Transpose of a matrix
    def transpose(self, A):
        return list(map(list, zip(*A)))

    # Identity matrix
    def identity_matrix(self, size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    # Matrix addition
    def matrix_add(self, A, B):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    # Scalar multiplication of a matrix
    def scalar_multiply(self, scalar, A):
        return [[scalar * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    # Matrix inversion using adjugate and determinant (for any n x n matrix)
    def matrix_inverse(self, matrix):
        det = self.determinant(matrix)
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted")
        
        adjugate = self.adjugate(matrix)
        return [[adjugate[row][col] / det for col in range(len(matrix))] for row in range(len(matrix))]

    # Determinant for any n x n matrix
    def determinant(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for col in range(len(matrix)):
            cofactor_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * self.determinant(cofactor_matrix)

        return det

    # Adjugate of a matrix
    def adjugate(self, matrix):
        cofactors = []
        for row in range(len(matrix)):
            cofactor_row = []
            for col in range(len(matrix)):
                minor = [r[:col] + r[col + 1:] for r in (matrix[:row] + matrix[row + 1:])]
                cofactor_row.append(((-1) ** (row + col)) * self.determinant(minor))
            cofactors.append(cofactor_row)
        return self.transpose(cofactors)

    # Fit the model by computing the posterior distribution over theta
    def fit(self, X, y):
        N, D = len(X), len(X[0])
        
        # Prior covariance matrix (sigma_theta^2 * I)
        prior_cov = self.scalar_multiply(self.sigma_theta2, self.identity_matrix(D))
        
        # Posterior covariance: (X^T X / sigma_y^2 + I / sigma_theta^2)^(-1)
        Xt = self.transpose(X)
        XtX = self.matrix_multiply(Xt, X)
        XtX_scaled = self.scalar_multiply(1 / self.sigma_y2, XtX)
        prior_cov_inv = self.matrix_inverse(prior_cov)
        cov_sum = self.matrix_add(XtX_scaled, prior_cov_inv)
        self.posterior_cov = self.matrix_inverse(cov_sum)
        
        # Posterior mean: posterior_cov * (X^T y / sigma_y^2)
        XTy = self.matrix_multiply(Xt, [[yi] for yi in y])
        XTy_scaled = self.scalar_multiply(1 / self.sigma_y2, XTy)
        self.posterior_mean = self.matrix_multiply(self.posterior_cov, XTy_scaled)

    # Log determinant of a matrix (determinant is already implemented)
    def log_determinant(self, matrix):
        det = self.determinant(matrix)
        if det <= 0:
            raise ValueError("Determinant must be positive for log-determinant")
        return math.log(det)

    # Log marginal likelihood
    def log_marginal_likelihood(self, X, y):
        N, D = len(X), len(X[0])

        # Prior covariance (sigma_theta^2 * I)
        prior_cov = self.scalar_multiply(self.sigma_theta2, self.identity_matrix(D))
        
        # Posterior covariance
        Xt = self.transpose(X)
        Sigma_y = self.matrix_add(self.matrix_multiply(X, self.matrix_multiply(self.posterior_cov, Xt)),
                                  self.scalar_multiply(self.sigma_y2, self.identity_matrix(N)))
        
        # Log determinant of Sigma_y
        log_det_Sigma_y = self.log_determinant(Sigma_y)
        
        # Sigma_y^-1
        Sigma_y_inv = self.matrix_inverse(Sigma_y)
        
        # y^T * Sigma_y^-1 * y (quadratic form)
        y = [[yi] for yi in y]
        quadratic_form = self.matrix_multiply(self.transpose(y), self.matrix_multiply(Sigma_y_inv, y))[0][0]
        
        # Log marginal likelihood
        log_marg_likelihood = -0.5 * (N * math.log(2 * math.pi) + log_det_Sigma_y + quadratic_form)
        
        return log_marg_likelihood

# Example data
X = [[1, 2], [3, 4], [5, 6]]  # N x D matrix (3 samples, 2 features)
y = [7, 9, 11]  # N x 1 target vector (3 samples)

# Bayesian Linear Regression parameters
sigma_y2 = 1  # Observation noise variance
sigma_theta2 = 1  # Prior variance of parameters

# Create the model and fit it to the data
model = BayesianLinearRegression(sigma_y2, sigma_theta2)
model.fit(X, y)

# Compute the log marginal likelihood
log_marg_likelihood = model.log_marginal_likelihood(X, y)
print(f"Log marginal likelihood: {log_marg_likelihood}")
