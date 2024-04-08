# Define the main function to get user input and calculate the tip
def main():
    # Get user input for the meal cost and tip percentage
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip amount and print the result
    tip = dollars * percent / 100
    print(f"Leave ${tip:.2f}")

# Convert the dollar amount from string to float
def dollars_to_float(d):
    dollars = d.replace('$', '')  # Remove dollar sign if present
    dollars = float(dollars)
    return dollars

# Convert the percentage from string to float
def percent_to_float(p):
    percent = p.replace('%', '')  # Remove percentage sign if present
    percent = float(percent)
    return percent

# Call the main function to start the program
main()
