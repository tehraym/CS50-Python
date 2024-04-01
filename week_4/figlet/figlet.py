import pyfiglet
import sys
import random

figlet = pyfiglet.Figlet()

def main():
    if len(sys.argv) < 2:
        fig = input("Input: ")
        figlet.setFont(font = random.choice(figlet.getFonts()))
        print(figlet.renderText(fig))
    elif len(sys.argv) < 4 and sys.argv[1] == "-f":
        fig = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(fig))
    else:
        sys.exit("Invalid Fig")

main()