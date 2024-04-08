# Get user input for the answer to the Great Question
question = input("What is the answer to the Great Question of life, the Universe, and Everything? ").casefold().strip()

# Check various forms of the answer and provide the corresponding response
if question == "42":
    # Print "Yes" if the answer is "42"
    print("Yes")
elif question == "forty-two":
    # Print "Yes" if the answer is "forty-two"
    print("Yes")
elif question == "forty two":
    # Print "Yes" if the answer is "forty two"
    print("Yes")
else:
    # Print "No" if none of the conditions are met
    print("No")
