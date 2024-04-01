import sys
import csv

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                with open(sys.argv[2], 'w') as newfile:
                    fields = ['first', 'last', 'house']
                    writer = csv.DictWriter(newfile, fieldnames = fields)
                    writer.writeheader()
                    for i in reader:
                        last, first = i['name'].split(',')
                        writer.writerow({'first': first.strip(), 'last': last, 'house': i['house']})

    except FileNotFoundError as err:
        sys.exit(f"Could not read{sys.argv[1]}")

if __name__ == "__main__":
    main()
