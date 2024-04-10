# CS50Python Code Snippets

## Description

This repository contains various Python code snippets that perform different tasks. Below are the explanations and usage instructions for each code snippet.

## Code Snippets

### Einstein
```python
m = int(input("m: "))
c = 300000000 * 300000000
e = m * c
print(f"E: {e}")
```
### making Faces
```python
usr_input = input("")
usr_input = usr_input.replace(":)", "🙂")
usr_input = usr_input.replace(":(", "🙁")
print(usr_input)
```

### Indoor voice
```python 
usr_input = input("").lower()
print(usr_input)
```

### Tip Calculator
```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent / 100
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dollars = d.replace('$', '')
    dollars = float(dollars)
    return dollars

def percent_to_float(p):
    percent = p.replace('%', '')
    percent = float(percent)
    return percent

main()
```
