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