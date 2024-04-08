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
