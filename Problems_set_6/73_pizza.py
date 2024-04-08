import sys
import csv
from tabulate import tabulate


def main():
    try:
        if validation():
            print(validation())
       
    except FileNotFoundError:
        sys.exit("File does not exists")
    

def validation():    
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        return reading_file()  





def reading_file():
        with open(sys.argv[1], "r") as file:
            if  ".csv" == sys.argv[1][-4:]:
                reader = csv.DictReader(file)
                return tabulate(reader, tablefmt="grid", headers="keys")
            
            else:
                sys.exit("Not a CSV file.")


if __name__ == "__main__":
    main()    


