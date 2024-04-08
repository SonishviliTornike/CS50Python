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