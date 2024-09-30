def prefix_to_postfix(expression):
    stack = []
    # Split the expression into tokens
    tokens = expression.split()
    # Reverse the list of tokens
    tokens = tokens[::-1]
    
    # Process each character in the reversed expression
    for token in tokens:
        if token.isalpha() or token.isdigit():
            stack.append(token)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + " " + op2 + " " + token)
    
    return stack[-1]

# # Example usage:
# prefix_expression = "+ + * 4 5 6 7"
# postfix_expression = prefix_to_postfix(prefix_expression)
# print("Postfix Expression:", postfix_expression)