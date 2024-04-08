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
