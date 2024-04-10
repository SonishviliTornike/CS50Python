# Python Code Snippets README

This repository contains various Python code snippets that perform different tasks. Below are the explanations and usage instructions for each code snippet.

## Home Federal Savings Bank
```python
greeting = input("Greeting: ")

if "Hello" in greeting:
    print("$0")
elif "H" in greeting:
    print("20$")
else:
    print("$100")
```
## Deep Thought
```python
# Get user input for the answer to the Great Question
question = input("What is the answer to the Great Question of life, the Universe, and Everything? ").casefold().strip()

# Check various forms of the answer and provide the corresponding response
if question == "42":
    # Print "Yes" if the answer is "42"
    print("Yes")
elif question == "forty-two":
    # Print "Yes" if the answer is "forty-two"
    print("Yes")
elif question == "forty two":
    # Print "Yes" if the answer is "forty two"
    print("Yes")
else:
    # Print "No" if none of the conditions are met
    print("No")
```

## File exstensions
``` python
# Get user input for the file extension
extension = input("File name: ").strip().casefold()

# Check the file extension and determine the corresponding MIME type
if ".gif" in extension:
    print("image/" + extension[-3:])
elif ".jpg" in extension:
    # Replace "jpg" with "jpeg" and print the MIME type
    print("image/" + extension[-3:].replace("jpg", "jpeg"))
elif ".jpeg" in extension:
    print("image/" + extension[-4:])
elif ".png" in extension:
    print("image/" + extension[-3:])
elif ".pdf" in extension:
    print("application/" + extension[-3:])
elif ".txt" in extension:
    print("text/plain")
elif ".zip" in extension:
    print("application/" + extension[-3:])
else:
    # Default to "application/octet-stream" if the extension is not recognized
    print("application/octet-stream")
```

## Math interpreter
```python
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
```


## Meal time
```python
def main():
    #Take time from user
    now = input("What time is it? ")

    #Call convert function with argument now
    now = convert(now)

    #Print if there is meal time
    if now >= 7.00 and now <= 8.00:
        print("breakfast time")
    elif now >= 12.00 and now <= 13.00:
        print("lunch time")
    elif now >= 18.00 and now <= 19.00:
        print("dinner time")

#Convert time format
def convert(time):
    #Split and assign to variables
    hours, minutes = time.split(":")

    #Replacing ":" with '.'
    time = time.replace(":", '.')

    #Convert them to float
    hours = float(hours)
    minutes = float(minutes)

    #Print nothing if does not supports time format
    if hours > 24:
        False
    elif minutes > 60:
        False
    elif hours < 0:
        False
    #Fraction of an hour to print 7.5 instead of 7.3
    fraction_of_an_hour = minutes / 60.0
    time = hours + fraction_of_an_hour
    return time


if __name__ == "__main__":
    main()
```
