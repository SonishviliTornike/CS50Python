# Python Code Snippets

This repository contains various Python code snippets that perform different tasks. Below are the explanations and usage instructions for each code snippet.

## Name Adieu

```python
import inflect

p = inflect.engine()

name_list = []

while True:
    try: 
        get_name = input("Name: ")
        name_list.append(get_name)
    except EOFError and KeyboardInterrupt:
        sorted_list = p.join(name_list)
        print(f"Adieu, adieu, to {sorted_list}.")
        break
```

This code snippet prompts the user to input names, which are then added to a list. When the user signals the end of input (e.g., by pressing Ctrl+D) or interrupts the program (e.g., by pressing Ctrl+C), the program sorts the names alphabetically and prints a farewell message with the list of names.

## Bitcoin Value Converter

```python
import sys
import requests

try:
    if len(sys.argv) <= 1:
        raise requests.RequestException
    if sys.argv[1].isalpha():
        raise ValueError
    
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    data = response.json()
    usd = data["bpi"]["USD"]["rate"]

    bitcoin = float(sys.argv[1])
    usd = usd.replace(",", "")
    bitcoin_to_usd = float(usd) * float(bitcoin)
    print(f"${bitcoin_to_usd:,.4f}")
    
except requests.RequestException:
    sys.exit("Missing Command-line argument.")
except ValueError:
    sys.exit("Comand-line argument is not a number ")
```

This code snippet converts a given amount of Bitcoin to its equivalent value in US Dollars (USD). The program takes the Bitcoin amount as a command-line argument and uses the CoinDesk API to retrieve the current exchange rate. It then calculates the USD value and prints the result. If the command-line argument is missing or not a valid number, the program will exit with an appropriate error message.

## Emojify

```python
import emoji

usr_input = input("Input: ")

print(emoji.emojize(usr_input, language='alias'))
```

This code snippet prompts the user to input a string and then uses the `emoji` library to replace any emoji aliases in the input with their corresponding emoji characters. The `language='alias'` parameter specifies that the input should be interpreted as emoji aliases.

## Figlet

```python
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    usr_input = input("Input: ")
    random_font = random.choice(fonts)
    f = figlet.setFont(font=random_font)

if sys.argv[1] == "-f" and sys.argv[2] in fonts:
    usr_input = input("Input: ")
    f = figlet.setFont(font=sys.argv[2])  
else:
    sys.exit("Invalid usage")

print(figlet.renderText(usr_input))
```

This code snippet uses the `pyfiglet` library to generate ASCII art from user input. If the user provides no command-line arguments, the program will prompt the user for input and use a randomly selected font to generate the ASCII art. If the user provides the `-f` flag followed by a valid font name, the program will use the specified font to generate the ASCII art. If the usage is invalid, the program will exit with an error message.

## Guess the Number

```python
import random

def main():   
    usr_level = level_validation()
    while True:
        random_number = random.randint(1, usr_level)
        usr_guess = guess_validation()

        if usr_guess == random_number:
            print("Just right!")
            break
        elif usr_guess > random_number:
            print("Too large!")  
            continue   
        else:
            print("Too small!")  
            continue

def level_validation():
      while True:
            try:
                level = int(input("Level: "))
                if level <= 0:
                    continue
                else:
                    return level
            except ValueError:
                continue

def guess_validation():
    while True: 
        try:
            guess = int(input("Guess: ")) 
            if guess <= 0:
                continue
            else:
                return guess
        except ValueError:
            continue

if __name__ == "__main__":
    main()
```

This code snippet implements a simple guessing game. The user is prompted to enter a level, which determines the range of the random number to be guessed. The user then repeatedly guesses a number until they correctly guess the random number. The program provides feedback on whether the guess is too large or too small. The `level_validation()` and `guess_validation()` functions ensure that the user's input is a valid positive integer.

## Math Homework

```python
import random

def main():
    count = 10
    score = 0
    attempt = 3
    lvl = get_level()
    while count != 0:
        if attempt == 3: # User have 3 attempt to answer each equation
            # Only generate_integer for new equation if attempt == 3
            x, y = generate_integer(lvl)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                count -= 1
                score  += 1
                attempt = 3 # Reset attempt to generate new equation in case user input the right answer on 2nd/3rd try
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            attempt -= 1
            pass
        if attempt == 0:
            print((f"{x} + {y} = {answer}"))
            attempt = 3 # Reset attempt to generate new equation
            count -= 1
            continue
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level <= 0:
                raise ValueError
            else:
                return level
        except ValueError:
            print("EEE")
            continue

def generate_integer(level):
    if level == 1:
        first_random_num = random.randint(0, 9)
        second_random_num = random.randint(0, 9)
    elif level == 2:
        first_random_num = random.randint(10, 99)
        second_random_num = random.randint(10, 99)
    else:
        first_random_num = random.randint(100, 999)
        second_random_num = random.randint(100, 999)                
            
    return first_random_num, second_random_num

if __name__ == "__main__":
    main()
```

This code snippet implements a simple math homework practice program. The user is prompted to enter a difficulty level, and the program generates addition problems with random integers based on the selected level. The user has three attempts to answer each problem correctly. If the user's answer is incorrect, the program displays the correct answer. The program keeps track of the user's score and displays it at the end.
