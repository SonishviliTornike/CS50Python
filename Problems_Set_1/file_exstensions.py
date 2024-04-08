# Get user input for the file extension
extension = input("File name: ").strip().casefold()

# Check the file extension and determine the corresponding MIME type
if ".gif" in extension:
    print("image/" + extension[-3:])
elif ".jpg" in extension:
    # Replace "jpg" with "jpeg" and print the MIME type
    print("image/" + extension[-3:].replace("jpg", "jpeg"))
elif ".jpeg" in extension:
    print("image/" + extension[-4:])
elif ".png" in extension:
    print("image/" + extension[-3:])
elif ".pdf" in extension:
    print("application/" + extension[-3:])
elif ".txt" in extension:
    print("text/plain")
elif ".zip" in extension:
    print("application/" + extension[-3:])
else:
    # Default to "application/octet-stream" if the extension is not recognized
    print("application/octet-stream")
