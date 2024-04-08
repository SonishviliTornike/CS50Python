import sys

def main():
    try:
        if validating():
            print(validating())
    except FileNotFoundError:
        sys.exit("File does not exist")


def validating():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argumnets")
    else:
        return check_length_lines()



def check_length_lines():
    count = 0
    with open(sys.argv[1], "r") as file:
        if sys.argv[1][-3:] == ".py":
            lines = file.readlines()
            for row in lines:
                if not (row.lstrip().startswith("#") or row.strip() == ""):
                    count += 1
            return count

        else:
            sys.exit("Not a Python file")


if __name__ == "__main__":
    main()