def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    my_str = ""
    vowels = "aeiouAEIOU"
    for l in word:
        if not l in vowels:
            my_str +=  l
            
    return my_str


if __name__ == "__main__":
    main()
