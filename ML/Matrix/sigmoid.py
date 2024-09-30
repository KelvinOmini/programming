def sigmoid_function(real_value):
    return 1 / 1 + 2.71828 ** - real_value

number = int(input('Enter any number: '))
sigmoid_value = sigmoid_function(number)
print(f'For{number} sigmoid value is: {sigmoid_value}')

