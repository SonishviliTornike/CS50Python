# Python Code Snippets

This repository contains various Python code snippets that perform different tasks. Below are the explanations and usage instructions for each code snippet.

## Line Counter

```python
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
```

This code snippet is a program that counts the number of non-empty, non-comment lines in a Python file. The program takes a single command-line argument, which should be the path to the Python file. If the file does not exist or the number of command-line arguments is incorrect, the program will exit with an appropriate error message.

## CSV Translator

```python
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
```

This code snippet is a program that reads a CSV file, extracts the name, surname, and house information, and writes a new CSV file with the information in the desired format. The program takes two command-line arguments: the input CSV file and the output CSV file. If the number of command-line arguments is incorrect or the input/output files are not in the correct format, the program will exit with an appropriate error message.

## Image Processor

```python
import sys
from PIL import Image, ImageOps

def main():
    before_file = sys.argv[1]
    after_file = sys.argv[2]
    if validation(before_file, after_file):
        print(create_an_image(before_file, after_file))

def validation(before, after):
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command_line arguments")
    elif not (before.endswith(".jpg") or after.endswith(".jpg") or before.endswith(".jpeg") or after.endswith(".jpeg") or before.endsiwth(".png") or after.endswith('.png')):
        sys.exit("Invalid input")
    else:
        if not (before.endswith(".jpg") and after.endswith(".jpg") or before.endswith(".jpeg") and after.endswith(".jpeg") or before.endsiwth(".png") and after.endswith('.png')):
            sys.exit("Input and output have different extensions")
        else:
            return True

def create_an_image(before, after):
    try:
        img = Image.open(before)
        shirt_img = Image.open('shirt.png')
        size = shirt_img.size
        img = ImageOps.fit(img,size)
        img.paste(shirt_img, shirt_img)
        img.save(after)
        return "Image created succsesfuly"
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
```

This code snippet is a program that overlays a shirt image onto a user-provided image. The program takes two command-line arguments: the input image file and the output image file. The input and output files must be in the same image format (e.g., both JPG, both PNG). The program performs various validations to ensure the correct usage and file formats, and it creates the modified image by overlaying the shirt image on the user-provided image.

## Names Sorter

```python
import csv

def main():
    count = count_lines()
    sorted_list = write_new_file(read_file(), count)
    for element in sorted_list:
        new_element = ", ".join(element)
        print(new_element)

def count_lines():
    with open("76_names_sorter.csv", 'r') as file:
        amount_names = file.readlines()      
        return amount_names

def read_file():
    new_list = []
    with open("76_names_sorter.csv", 'r') as file:
        reader = csv.reader(file)      
        for element in reader:
            new_list.append(element)
        return sorted(new_list)

def write_new_file(sorted_list, count):
    sorted_list.insert(0,[f"Total of {len(count)} names"])
    sorted_list.insert(1,["-----------------"])
    with open("76_sorted_names.csv", 'w') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(sorted_list)
        return sorted_list

if __name__ == "__main__":
    main()
```

This code snippet is a program that reads a CSV file named "76_names_sorter.csv", sorts the names in the file, and writes the sorted names to a new CSV file named "76_sorted_names.csv". The program also prints the sorted names to the console. The program does not take any command-line arguments, as it assumes the input and output file names are fixed.

Overall, these Python code snippets cover various topics, including file handling, CSV manipulation, image processing, and command-line argument parsing. Each snippet includes a brief explanation of its functionality and usage instructions.
