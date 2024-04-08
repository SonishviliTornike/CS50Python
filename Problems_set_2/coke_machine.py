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
