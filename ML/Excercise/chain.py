import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Function for dot product
def dot_product(A, B):
    return sum(a * b for a,b in zip(A,B))

# Forward pass
def forward_pass(x, W1, b1, W2, b2):
    # Layer 1: z1 = W1 * x + b1
    z1 = [dot_product(W1[i], x) + b1[i] for i in range(len(W1))]
    # Apply sigmoid to each element of z1
    a1 = [sigmoid(z) for z in z1]

    # layer 2: z2 = W2 * a1 + b2 (dot product of W2 and a1)
    z2  = dot_product(W2, a1) + b2
    a2 = sigmoid(z2)

    return a2

# Define input
x = [0.5, 0.3]

# Define weigths and biases
W1 = [[0.1, 0.2],
      [0.3, 0.4]] 
b1 = [0.5, 0.6] # Bias for layer 1 (2 neurons)
W2 = [0.7, 0.8] # Weights for layer 2 (1 neuron,  2 inputs)
b2 = 0.9 # Bias for layer 2 (1 neuron)

output = forward_pass(x, W1, b1, W2, b2)
print("Output:", output)
