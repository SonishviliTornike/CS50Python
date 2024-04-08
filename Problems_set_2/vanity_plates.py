def main():
    # Get user input for the plate and convert it to uppercase
    plate = input("Plate: ").upper()
    
    # Check if the plate is valid using the is_valid function
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length_function(s) and first_two_letter(s) and digits_from_end(s) and first_no_zero(s):
        return True
    return False
def length_function(s):    
    # Check if the length of the plate is not between 2 and 6 characters
    if not (len(s) >= 2 and len(s) <= 6):
        return False
    return True

def first_two_letter(s):
    # Check if the first two characters are not alphabetic
    if not s[:2].isalpha():
        return False
    return True

def digits_from_end(s):
    # Check for the presence of digits and '0' in the plate
    for c in range(2, len(s)):
        # Check if the character is a digit and not all digits
        if s[c].isdigit() and not s[c:].isdigit():
            return False
    return True    

def first_no_zero(s):
    for c in range(2, len(s)):    
        # Check if '0' follows an alphabetic character
        if s[c] == '0' and s[c - 1].isalpha():
            return False
    return True

def only_alnums(s):
    # Check if the plate contains only alphanumeric characters
    if not s.isalnum():
        return False
    return True

# Call the main function to start the program
main()
