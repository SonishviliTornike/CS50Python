import sys, inflect, operator
from datetime import date


def main():
    try:
        dob = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(dob))
        words = convert_date_to_words(difference.days)
        print(f"{words} minutes")
    except ValueError:
        sys.exit("Invalid date")

def convert_date_to_words(total_days):
    p = inflect.engine()
    minutes = total_days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    return words.capitalize()

if __name__ == "__main__":
    main()