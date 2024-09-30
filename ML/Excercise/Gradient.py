import math

# Singmoid function:
def sigmoid(x):
    e = math.exp # 2.7182818288459045
    return 1/(1+e**-x)

def gradient_sigmoid(x):
    sig = sigmoid(x)
    return sig * (1 - sig)

# Tanh Function:
def tanh(x):
    e = math.exp
    e_pos = e ** x
    e_neg = e ** -x
    return (e_pos - e_neg) / (e_pos + e_neg)

def gradient_tanh(x):
    return 1 - tanh(x) ** 2

# Gradient of a vector valued funtion 
def greadient_vector_function(x): return [2 * xi for xi in x]

# ReLU function
def gradient_relu(x):
    return 1 if x > 0 else 0
