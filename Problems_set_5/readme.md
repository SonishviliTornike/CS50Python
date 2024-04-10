# Python Code Snippets

This repository contains various Python code snippets that perform different tasks. Below are the explanations and usage instructions for each code snippet.

## Vowel Remover

```python
from twttr_63 import shorten

def test_shorten():
    assert shorten("tornike") == "trnk"
```

This code snippet contains a unit test for the `shorten()` function from the `twttr_63` module. The `shorten()` function is responsible for removing vowels from a given word.

## Bank Value

```python
from bank_64 import value

def test_value():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0
    assert value("h") == 20
    assert value("H") == 20
    assert value("flip world") == 100
    assert value("FLIP WORLD") == 100
```

This code snippet contains a unit test for the `value()` function from the `bank_64` module. The `value()` function determines the value of a greeting based on certain rules.

## License Plate Validator

```python
from plates_65 import is_valid

def test_is_valid():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False

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
```

This code snippet contains a function `is_valid()` that validates the format of a given license plate. The `main()` function prompts the user to input a license plate and then prints whether the plate is valid or not. The unit test checks the `is_valid()` function with different inputs.

## Fuel Gauge

```python
from fuel_66 import *
import pytest

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("!/!")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(67) == "67%"

def main():
    greeting = input("Greeting: ").lower().strip()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
```

This code snippet contains two functions: `convert()` and `gauge()`. The `convert()` function takes a fraction as input and calculates the percentage representation of the fraction. The `gauge()` function takes the percentage value and returns the corresponding fuel gauge reading ("E", "F", or the percentage value). The unit tests ensure that the `convert()` and `gauge()` functions work as expected, including handling invalid inputs.

The `main()` function prompts the user for a greeting and prints the corresponding value based on the rules defined in the `value()` function.

Overall, this repository contains a variety of Python code snippets that cover different programming concepts, such as unit testing, input validation, and problem-solving. Each snippet includes a brief explanation of its functionality and usage instructions.
