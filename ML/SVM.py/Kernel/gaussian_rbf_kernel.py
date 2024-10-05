import numpy as np

def gaussian_rbf_kernel(w, x, sigma):
    """
    Computes the Gaussian RBF kernel between two vectors w and x.

    Parameters:
    - w: np.ndarray, first input vector
    - x: np.ndarray, second input vector
    - sigma: float, length scale parameter

    Returns:
    - K: float, computed RBF kernel value
    """
    # Compute the squared Euclidean distance
    distance_squared = np.sum((w - x) ** 2)
    
    # Compute the Gaussian RBF kernel value
    K = np.exp(-distance_squared / (2 * sigma ** 2))
    
    return K

# Example usage
if __name__ == "__main__":
    # Define two sample data points
    w = np.array([1.0, 2.0])
    x = np.array([2.0, 3.0])
    
    # Set the length scale parameter
    sigma = 1.0
    
    # Compute the Gaussian RBF kernel value
    kernel_value = gaussian_rbf_kernel(w, x, sigma)
    
    print(f"Gaussian RBF Kernel K(w, x): {kernel_value}")
