#63 homework
def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = "aeiouAEIOU"
    for l in word:
        if l in vowels:
            word =  word.replace(l, "")
            
    return word


if __name__ == "__main__":
    main()


#30 homework
# Define a list of vowels
# vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O"]

# # Get user input
# s = input("Input: ")
# # Iterate through each character in the input string
# for c in s:
#     # Check if the character is a vowel
#     if c in vowels:
#         # If it is a vowel, replace it with an empty string (remove it)
#         s = s.replace(c, "")
# # Print the modified string without vowels
# print(s)
