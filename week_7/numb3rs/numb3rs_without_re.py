import re
import sys
#Numb3rs without re & sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #Try & Except to catch non decimals
    try:
        #split the digits in a list & count the length of list
        list = [int(i) for i in ip.split(".")]
        if len(list) != 4: return False
        #Parsing the list
        for i in list:
            if not (0 <= i <= 255): return False
        return True
    except ValueError as err:
        return False

if __name__ == "__main__":
    main()
