# Python Code Snippets README

This repository contains various Python code snippets that perform different tasks. Below are the explanations and usage instructions for each code snippet.

## Get camelCase input

```python
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
```

## Coke machine

```python
# Set the initial amount due
amount_due = 50

# Continue processing until the amount due becomes 0
while amount_due != 0:
    # Display the absolute value of the amount due
    print(f"Amount Due: {abs(amount_due)}")

    # Check if the amount due is negative, indicating that change is owed
    if amount_due < 0:
        break

    # Get user input for the coin inserted
    inserted_coin = int(input("Insert Coin: "))

    # Define the coin denominations accepted by the machine
    machine_coins = [25, 10, 5]

    # Iterate through the machine coins
    for num in range(len(machine_coins)):
        # Skip to the next iteration if the inserted coin does not match the current machine coin
        if machine_coins[num] != inserted_coin:
            continue

        # Subtract the inserted coin from the amount due
        if machine_coins[num] == inserted_coin:
            amount_due -= inserted_coin

# Calculate the absolute value of the updated amount due
change_owed = abs(amount_due)

# Display the final change owed
print(f"Change Owed: {change_owed}")
```

## Nutrition

```python
# Get user input for the item and capitalize the first letter of each word
item = input("Item: ").title()

# Define a dictionary containing fruits and their corresponding calorie values
fruits = {
    "Apple": "130",
    "Avocado": "50",
    "Banana": "110",
    "Cantaloupe": "50",
    "Grapefruit": "60",
    "Honeydew Melon": "50",
    "Kiwifruit": "90",
    "Lemon": "15",
    "Lime": "20",
    "Nectarine": "60",
    "Orange": "80",
    "Peach": "60",
    "Pear": "100",
    "Pineapple": "50",
    "Plums": "70",
    "Strawberries": "50",
    "Sweet Cherries": "100",
    "Tangerine": "50",
    "Watermelon": "80"
}

# Check if the entered item is in the dictionary
if item in fruits:
    # Display the calorie value for the specified item
    print(f"Calories: {fruits.get(item)}")
```

## Twttr

```python
Define a list of vowels
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O"]

Get user input
s = input("Input: ")

Iterate through each character in the input string
for c in s:
    # Check if the character is a vowel
    if c in vowels:
        # If it is a vowel, replace it with an empty string (remove it)
        s = s.replace(c, "")

Print the modified string without vowels
print(s)
```

## Vanity plates
```python
def main():
    # Get user input for the plate and convert it to uppercase
    plate = input("Plate: ").upper()
    
    # Check if the plate is valid using the is_valid function
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length_function(s) and first_two_letter(s) and digits_from_end(s) and first_no_zero(s):
        return True
    return False
def length_function(s):    
    # Check if the length of the plate is not between 2 and 6 characters
    if not (len(s) >= 2 and len(s) <= 6):
        return False
    return True

def first_two_letter(s):
    # Check if the first two characters are not alphabetic
    if not s[:2].isalpha():
        return False
    return True

def digits_from_end(s):
    # Check for the presence of digits and '0' in the plate
    for c in range(2, len(s)):
        # Check if the character is a digit and not all digits
        if s[c].isdigit() and not s[c:].isdigit():
            return False
    return True    

def first_no_zero(s):
    for c in range(2, len(s)):    
        # Check if '0' follows an alphabetic character
        if s[c] == '0' and s[c - 1].isalpha():
            return False
    return True

def only_alnums(s):
    # Check if the plate contains only alphanumeric characters
    if not s.isalnum():
        return False
    return True

# Call the main function to start the program
main()
```
