import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Not enough Arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many Arguments")
        elif not sys.argv[1].endswith('.py'):
            sys.exit("Not a Python File")
        else:
            with open(sys.argv[1]) as file:
                count = 0
                for i in file:
                    i = i.strip()
                    if i.startswith('#'):
                        count -= 1
                    elif len(i) == 0:
                        count -= 1
                    count += 1
                print(count)
    except FileNotFoundError as Err:
        sys.exit("File Does not Exist")

if __name__ == "__main__":
    main()
