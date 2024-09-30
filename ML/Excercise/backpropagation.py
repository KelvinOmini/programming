# A neural network to perform binary classification that has:
'''
1. An input layer with n features.
2. One hidden layer with m neurons and ReLU activation
3. An output layer with a single neuron using a sigmoid activation
 to predict the probability of the posistive class
'''
# Network structure
'''
Input layer: x (vector of features)
Hidden layer: Weights W1, biases b1, ReLU activation
Output layer: weights W2, bias b2, sigmoid activation
Loss function: Binary Cross-Entropy.
'''

def relu(x):
    return max(0, x)

def relu_derivative(x):
    return 1 if x > 0 else 0

def sigmoid(x):
    return 1 / (1 + 2.718281828459045 ** -x)

def sigmoid_dderivative(x):
    sig  = sigmoid(x)

# Neural network parameters
w1 = [0.5, -0.5]
b1 = 0.0
w2 = [0.3]
b2 = 0.0
learning_rate = 0.01

# Training data
x= [1.0, 2.0] #Input features
y = 1 # Target label

# Forward pass
z1 = w1[0] * x[0] + w1[1] * x[1] + b1
a1 = relu(z1)
z2 = w2[0] * a1 + b2
y_hat = sigmoid(z2)

# loss (binary cross-entropy)
loss = -(y * (2.718281828459045 ** -z2) + (1 - y) * (2.718281828459045 ** z2))

# Backward pass
# Gradient of the loss w.r.t output
d_loss_y_hat = y_hat -y 

# output layer gradient
d_loss_z2 = d_loss_y_hat * sigmoid_dderivative(z2)
d_loss_w2 = d_loss_z2 * a1
d_loss_b2 = d_loss_z2

# Hidden layer gradients
d_loss_a1 = d_loss_z2 * w2[0]
d_loss_z1 = d_loss_a1 * relu_derivative(z1)
d_loss_w1 = [d_loss_z1 * x[0], d_loss_z1 * x[1]]
d_loss_b1 = d_loss_z1

# Updates weeights
w1[0] -= learning_rate * d_loss_w1[0]
w1[1] -= learning_rate * d_loss_w1[1]
b1 -= learning_rate * d_loss_b1
w2[0] -= learning_rate * d_loss_w2
b2 -= learning_rate * d_loss_b2

print('Updated w1: ', w1)
print('Updated b1: ', b1)
print('Updated w2: ', w2)
print('Updated b2: ', b2)
