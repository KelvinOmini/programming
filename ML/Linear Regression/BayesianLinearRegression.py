class BayesianLinearRegression_:
    def __init__(self, sigma_y2, sigma_theta2):
        self.sigma_y2 = sigma_y2  # Variance of observation noise
        self.sigma_theta2 = sigma_theta2  # Variance of prior over parameters
        self.posterior_mean = None
        self.posterior_cov = None

    # Matrix multiplication (works for any n x n matrix)
    def matrix_multiply(self, A, B):
        result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
        return result

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

    # General matrix inversion using adjugate and determinant (works for any n x n matrix)
    def matrix_inverse(self, matrix):
        det = self.determinant(matrix)
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted")
        
        adjugate = self.adjugate(matrix)
        return [[adjugate[row][col] / det for col in range(len(matrix))] for row in range(len(matrix))]

    # Determinant for any n x n matrix
    def determinant(self, matrix):
        # Base case for 2x2 matrix
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        # Recursive case for larger matrices
        det = 0
        for col in range(len(matrix)):
            # Create the cofactor matrix by removing the first row and col-th column
            cofactor_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
            det += ((-1) ** col) * matrix[0][col] * self.determinant(cofactor_matrix)

        return det

    # Adjugate of a matrix
    def adjugate(self, matrix):
        cofactors = []
        for row in range(len(matrix)):
            cofactor_row = []
            for col in range(len(matrix)):
                # Create the minor matrix by removing the current row and column
                minor = [r[:col] + r[col + 1:] for r in (matrix[:row] + matrix[row + 1:])]
                cofactor_row.append(((-1) ** (row + col)) * self.determinant(minor))
            cofactors.append(cofactor_row)
        # Return the transpose of the cofactor matrix (which is the adjugate)
        return self.transpose(cofactors)

    # Fit the model by computing the posterior distribution over theta
    def fit(self, X, y):
        # Prior covariance matrix (sigma_theta^2 * I)
        N, D = len(X), len(X[0])
        prior_cov = self.scalar_multiply(self.sigma_theta2, self.identity_matrix(D))
        
        # Posterior covariance: (X^T X / sigma_y^2 + I / sigma_theta^2)^(-1)
        Xt = self.transpose(X)
        XtX = self.matrix_multiply(Xt, X)
        XtX_scaled = self.scalar_multiply(1 / self.sigma_y2, XtX)
        prior_cov_inv = self.matrix_inverse(prior_cov)  # Works for any size now
        cov_sum = self.matrix_add(XtX_scaled, prior_cov_inv)
        self.posterior_cov = self.matrix_inverse(cov_sum)
        
        # Posterior mean: posterior_cov * (X^T y / sigma_y^2)
        XTy = self.matrix_multiply(Xt, [[yi] for yi in y])
        XTy_scaled = self.scalar_multiply(1 / self.sigma_y2, XTy)
        self.posterior_mean = self.matrix_multiply(self.posterior_cov, XTy_scaled)

    # Predictive distribution for a new input x_*
    def predict(self, x_star):
        # Predictive mean: x_*^T * posterior_mean
        mu_star = sum(x_star[i] * self.posterior_mean[i][0] for i in range(len(x_star)))
        
        # Predictive variance: x_*^T * posterior_cov * x_* + sigma_y^2
        x_star_T = [[xi] for xi in x_star]
        sigma_star2 = self.matrix_multiply(
            self.matrix_multiply([x_star], self.posterior_cov), x_star_T
        )[0][0] + self.sigma_y2
        
        return mu_star, sigma_star2


# Test the class with sample data (for a 3x2 matrix X)
X = [[1, 2], [3, 4], [5, 6]]  # N x D matrix (3 samples, 2 features)
y = [7, 9, 11]  # N x 1 target vector (3 samples)

# Bayesian Linear Regression parameters
sigma_y2 = 1  # Observation noise variance
sigma_theta2 = 1  # Prior variance of parameters

# Create the model and fit it to the data
model = BayesianLinearRegression_(sigma_y2, sigma_theta2)
model.fit(X, y)

# New input for prediction
x_star = [2, 3]

# Predictive distribution at new input
mu_star, sigma_star2 = model.predict(x_star)
print(f"Predictive mean: {mu_star}")
print(f"Predictive variance: {sigma_star2}")
