# Python Code Snippets

This repository contains various Python code snippets that perform different tasks. Below are the explanations and usage instructions for each code snippet.

## Restaurant Menu Ordering System

```python
# Menu dictionary with menu items and their prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# List to store the user's order
your_order = []

# Continuously prompt the user to make an order
while True:
    try:
        # Get user input for the ordered item and convert it to title case
        make_order = input("Item: ").title()

        # Add the price of the ordered item to the order list
        your_order.append(menu[make_order])
        
        # Calculate and display the total cost of the order
        total = sum(your_order)
        print(f"Total: ${total:.2f}")

    # Handle the case where the ordered item is not in the menu
    except KeyError:
        print("Invalid item. Please choose from the menu.")
        continue

    # Handle the case where the user signals the end of the order (EOFError)
    except EOFError:
        break
```

This code snippet implements a simple restaurant menu ordering system. The user can continuously input menu items, and the program will add the corresponding price to the order list. The total cost of the order is calculated and displayed after each item is added. If the user enters an invalid item, an error message is displayed, and the user is prompted to choose from the menu again. The program ends when the user signals the end of the order (e.g., by pressing Ctrl+D).

## Fraction to Percentage Converter

```python
import math

# Continue prompting the user for input until a valid fraction is provided
while True:
    try:
        # Get user input for a fraction and split it into numerator and denominator
        fraction = input("Fraction: ").split("/")

        # Check if the fraction is a proper fraction (numerator less than or equal to denominator)
        if int(fraction[0]) > int(fraction[1]):
            continue

        # Calculate the percentage representation of the fraction
        fraction_percentage = int(fraction[0]) / int(fraction[1]) * 100

        # Evaluate and print the corresponding grade based on the calculated percentage
        if fraction_percentage <= 1:
            print("E")
            break
        elif 1 < fraction_percentage < 99:
            print(f"{round(fraction_percentage)}%")
            break
        elif fraction_percentage >= 99:
            print("F")
            break

    # Handle input errors and exceptions
    except ValueError:
        print("Invalid input! Please enter a valid fraction.")
        continue
    except ZeroDivisionError:
        print("You cannot divide by zero! Please enter a non-zero denominator.")
        continue
```

This code snippet prompts the user to input a fraction, and it converts the fraction to a percentage representation. The program continues to prompt the user until a valid fraction is provided. If the fraction is not a proper fraction (numerator greater than denominator), the program will ask the user to enter a valid fraction again. The program then evaluates the percentage and prints the corresponding grade: "E" for 1% or less, the rounded percentage value for values between 1% and 99%, and "F" for 99% or more.

## Grocery List

```python
# Dictionary to store grocery items and their quantities
grocery_list = {}

# Continuously prompt the user to input grocery items
while True:
    try:
        # Get user input for a grocery item
        item = input()

        # Check if the item is already in the grocery list and update the quantity
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            # If the item is not in the list, add it with a quantity of 1
            grocery_list.update({item: 1})
    
    # Handle the case where the user signals the end of input (EOFError)
    except EOFError:
        break
    # Handle the case where the user interrupts the program (KeyboardInterrupt)
    except KeyboardInterrupt:
        break

# Sort the grocery list alphabetically and print the items with their quantities
grocery_list = dict(sorted(grocery_list.items()))
for product in grocery_list:
    print(f"{str(grocery_list[product])} {product.upper()}")
```

This code snippet implements a simple grocery list program. It continuously prompts the user to input grocery items, and it keeps track of the quantities of each item in a dictionary. When the user signals the end of input (e.g., by pressing Ctrl+D) or interrupts the program (e.g., by pressing Ctrl+C), the program sorts the grocery list alphabetically and prints each item with its corresponding quantity.

## Date Formatter

```python
# List of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Continuously prompt the user to input a date
while True:
    try:
        # Get user input for a date in the format "month/day/year" and title case
        inputed_date = input("Date: ").title()
        month, day, year = inputed_date.split("/")

        # Check if the entered date is valid
        if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and len(year) == 4:
            # Print the date in the format "year-month-day" with leading zeros for month and day
            print(f"{year}-{int(month):02}-{int(day):02}")
            break

    # Handle the case where the input cannot be split into three components
    except ValueError:
        try:
            # Attempt to split the input when the date is given in the format "month day, year"
            day_month, year = inputed_date.split(", ")
            month, day = day_month.split()
            indexed_month = months.index(month) + 1

            # Check if the entered date is valid
            if month in months and 1 <= int(day) <= 31 and 1 <= indexed_month <= 12 and len(year) == 4:
                # Print the date in the format "year-month-day" with leading zeros for month and day
                print(f"{year}-{indexed_month:02}-{int(day):02}")
            else:
                continue

            # Break out of the loop after processing the valid date
            break
        # Handle the case where the input cannot be split into two components
        except ValueError:
            continue
```

This code snippet prompts the user to input a date and formats the date in the "year-month-day" format with leading zeros for the month and day. The program can handle dates in two different formats: "month/day/year" and "month day, year". If the input is not in a valid format, the program will continue to prompt the user until a valid date is entered.
