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
