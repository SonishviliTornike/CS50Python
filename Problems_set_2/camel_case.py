# Get user input for camelCase string
case = input("camelCase: ")

# Iterate through each character in the input string
for c in case:
    # Check if the current character is an uppercase letter
    if c.isupper():
        # Replace the uppercase letter with its lowercase version preceded by an underscore
        case = case.replace(c, "_" + c.lower()) 

# Display the modified string with underscores
print(case)
