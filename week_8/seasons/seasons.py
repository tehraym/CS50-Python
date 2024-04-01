from datetime import date, timedelta
import operator
import re
import sys
import inflect

def main():
    print(seasons(input("Date of Birth: ")))

def seasons(x):
    #Validating the time's format
    match = re.match(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", x)
    if match:
        birth = date.fromisoformat(match.group())
        minutes = int(operator.sub(date.today(), birth).total_seconds() / 60)
        p = inflect.engine()
        return (f"{p.number_to_words(minutes, andword = '').capitalize()} minutes")

    else:
        sys.exit("Error please input YYYY-MM-DD")

if __name__ == "__main__":
    main()
