def tensor_add(tensor1, tensor2):
    if isinstance(tensor1, (int, float)) and isinstance(tensor2, (int, float)):
        return tensor1 + tensor2
    
    return [tensor_add(t1, t2) for t1, t2 in zip(tensor1, tensor2)]

def tensor_scalar_multiply(tensor, scalar):
    if isinstance(tensor, (int, float)):
        return tensor * scalar
    
    return [tensor_scalar_multiply(t, scalar) for t in tensor]

def matrix_multiply(matrix1, matrix2):
    rows= len(matrix1)
    cols= len(matrix2[0])
    common_dim = len(matrix2)

    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            for k in range(common_dim):
                result[i][j] += matrix1[i][j] * matrix2[k][j]
    
    return result