def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False
    
    if not (len(s) >= 2 and len(s) <= 6):
        return False
    
    if not s.isalnum():
        return False
    
    for char in range(2, len(s)):
        if s[char].isdigit():
            if not s[char:].isdigit():
                return False

    for num in range(2, len(s)):
        if s[num - 1] == "0":
            return False
            
            
        
    return True


if __name__ == "__main__":
    main()