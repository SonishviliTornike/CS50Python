# Get user input for the expression
expression = input("Expression: ")

# Split the expression into three components (x, y, z)
x, y, z = expression.split(" ")

# Evaluate the expression and convert the result to a float
expression_result = eval(x + y + z)
result = float(expression_result)

# Check if the operator 'y' is a valid arithmetic operator
if y in ['+', '-', '*', '**', '/']:
    # Print the result if the operator is valid
    print(result)
else:
    # Print an error message if the operator is not valid
    print("We need an arithmetic operator.")
