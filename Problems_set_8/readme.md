# Python Code Snippets

This repository contains various Python code snippets that perform different tasks. Below are the explanations and usage instructions for each code snippet.

## Shirtificate Generator

```python
from fpdf import FPDF
from PIL import Image

name = input("Name: ")

pdf = FPDF('P', 'mm', (210, 297))
pdf.add_page(format='A4')
pdf.image("shirtificate.png", x=0, y=60)

pdf.set_font("Helvetica", 'B', 35)
pdf.cell(200, 50, text='CS50 Shirtificate', align="C")

pdf.set_font("Helvetica", 'B', 28)
pdf.cell(-200, 250, text=name, align='C')

pdf.output("shirtificate.pdf")
```

This code snippet generates a PDF "shirtificate" using the `fpdf` and `PIL` libraries. The program prompts the user to enter their name, and then it creates a PDF file with the name of the user centered on the page, along with the "CS50 Shirtificate" text. The generated PDF file is saved as `shirtificate.pdf`.

## Cookie Jar

```python
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("No space available")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError(f"This {n} amount of cookies aren't available")
        self.size = self.size - n
    
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Cant be 0 or Negative number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("No space")
        self._size = size
```

This code snippet defines a `Jar` class that represents a cookie jar. The class has attributes for the jar's capacity and the current number of cookies in the jar. The class provides methods for depositing and withdrawing cookies, as well as properties for accessing and modifying the capacity and size of the jar. The `__str__` method is overridden to display the cookies in the jar as cookie emojis.

## Unit Tests

```python
from seasons_82 import convert_minutes_to_words
from jar_83 import Jar
import pytest

def test_convert_minutes_to_words():
    assert convert_minutes_to_words(8814) == "Twelve million, six hundred ninety-two thousand, one hundred sixty minutes"

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1) 
    assert jar.size == 1
    
def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1) == 0
```

This code snippet contains unit tests for the `convert_minutes_to_words()` function from the `seasons_82` module and the `Jar` class from the `jar_83` module. The tests cover various aspects of the functions and class, including initialization, string representation, depositing, and withdrawing cookies.

## Age to Minutes Converter

```python
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
```

This code snippet is a program that calculates the total number of minutes a person has been alive based on their date of birth. The program prompts the user to enter their date of birth, calculates the number of days between the date of birth and the current date, and then converts the total number of minutes into words using the `inflect` library. If the user enters an invalid date, the program will exit with an error message.

Overall, this repository contains a variety of Python code snippets that cover different programming concepts, such as PDF generation, object-oriented programming, unit testing, and date/time manipulation. Each snippet includes a brief explanation of its functionality and usage instructions.
