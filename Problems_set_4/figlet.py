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
