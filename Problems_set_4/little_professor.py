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