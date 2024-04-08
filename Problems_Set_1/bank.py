# Get user input for the greeting
greeting = input("Greeting: ")

# Check the content of the greeting and determine the corresponding response
if "Hello" in greeting:
    # Print "$0" if "Hello" is present in the greeting
    print("$0")
elif "H" in greeting:
    # Print "20$" if the letter 'H' is present in the greeting
    print("20$")
else:
    # Default to "$100" if neither condition is met
    print("$100")
