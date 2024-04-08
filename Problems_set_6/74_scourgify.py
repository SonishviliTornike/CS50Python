import sys, csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        before = sys.argv[1]
        after = sys.argv[2]
        read_and_write_file(before, after)

def read_and_write_file(before, after):
    if before.endswith(".csv"):
        with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                if after.endswith(".csv"):
                    with open(sys.argv[2], 'w') as new_file:
                            fieldnames = ["name", "surname", "house"]
                            writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                            writer.writeheader()
                            for row in reader:
                                surname, name = row['name'].split(", ")
                                house = row['house']
                                writer.writerow({"name":name, 'surname':surname, 'house':house})
                else:
                     raise ValueError
    else:
         raise ValueError
    
if __name__ == "__main__":
    main()


