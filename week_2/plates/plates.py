def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not format(s):
        return False

    for i in s:
        if i in [' ', '.', ',']:
            return False

    return True

def format(x):
    h = 0

    # string cannot be longer than 6 and needs at least 2 char
    if 2 <= len(x) <= 6:
         h += 1

    #First two characters needs to be alphabet
    if x[0].isalpha() or x[1].isalpha():
        h += 1

    #Check if the first number is 0
    #Check if numbers are used in the middle of a plate
    i = 0
    j = 0
    while i < len(x):
        if x[i].isalpha() == False:
            if x[i] == '0':
                h -= 1
                break
            else:
                while j < len(x):
                    if x[j].isdigit() == False:
                        h -= 1
                    j += 1
                break
        i += 1
        j += 1

    if h >= 2:
        return True

main()

#("0","1","2","3","4","5","6","7","8","9"):