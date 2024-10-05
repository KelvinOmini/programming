import numpy as np

def sigmoid_kernel(xi, xj, alpha=1.0, c=0.0):
    """
    Compute the Sigmoid kernel between two vectors.

    Parameters:
    xi : array-like, shape (n_features,)
        First input vector.
    xj : array-like, shape (n_features,)
        Second input vector.
    alpha : float, optional, default=1.0
        Scale parameter.
    c : float, optional, default=0.0
        Constant that shifts the function.

    Returns:
    float
        The value of the Sigmoid kernel between xi and xj.
    """
    # Compute the dot product
    dot_product = np.dot(xi, xj)
    # Apply the Sigmoid function
    return np.tanh(alpha * dot_product + c)

# Example usage
xi = np.array([1, 2, 3])
xj = np.array([4, 5, 6])

# Calculate the Sigmoid kernel
kernel_value = sigmoid_kernel(xi, xj, alpha=0.5, c=1.0)
print("Sigmoid Kernel value:", kernel_value)
