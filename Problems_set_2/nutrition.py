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
