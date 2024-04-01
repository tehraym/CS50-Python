import csv
import sys
from tabulate import tabulate

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line argument")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line argument")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                print(tabulate(reader, headers = 'firstrow', tablefmt = "grid"))

    except FileNotFoundError as err:
        sys.exit(f"File does not exist")

main()
