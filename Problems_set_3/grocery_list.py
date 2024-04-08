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
