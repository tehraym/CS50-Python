import sys
import os
from PIL import Image, ImageOps

def main():
    format = ['.jpg', 'jpeg', '.png']
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too much command-line arguments")
        elif os.path.splitext(sys.argv[1].lower())[1] not in format:
            sys.exit("Invalid Extension")
        elif os.path.splitext(sys.argv[2].lower())[1] not in format:
            sys.exit("Invalid Extension")
        elif os.path.splitext(sys.argv[1].lower())[1] != os.path.splitext(sys.argv[2].lower())[1]:
            sys.exit("Input and output have different extensions")
        else:
            shirt = Image.open("shirt.png")
            with Image.open(sys.argv[1]) as muppet:
                muppet_fit = ImageOps.fit(muppet, shirt.size)
                muppet_fit.paste(shirt, shirt)
                muppet_fit.save(sys.argv[2])

    except FileNotFoundError as err:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
