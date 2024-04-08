import sys
from PIL import Image, ImageOps



def main():
    before_file = sys.argv[1]
    after_file = sys.argv[2]
    if validation(before_file, after_file):
        print(create_an_image(before_file, after_file))


def validation(before, after):
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command_line arguments")
    elif not (before.endswith(".jpg") or after.endswith(".jpg") or before.endswith(".jpeg") or after.endswith(".jpeg") or before.endsiwth(".png") or after.endswith('.png')):
        sys.exit("Invalid input")
    else:
        if not (before.endswith(".jpg") and after.endswith(".jpg") or before.endswith(".jpeg") and after.endswith(".jpeg") or before.endsiwth(".png") and after.endswith('.png')):
            sys.exit("Input and output have different extensions")
        else:
            return True





def create_an_image(before, after):
    try:
        img = Image.open(before)
        shirt_img = Image.open('shirt.png')
        size = shirt_img.size
        img = ImageOps.fit(img,size)
        img.paste(shirt_img, shirt_img)
        img.save(after)
        return "Image created succsesfuly"


    except FileNotFoundError:
        sys.exit("Input does not exist")



if __name__ == "__main__":
    main()

