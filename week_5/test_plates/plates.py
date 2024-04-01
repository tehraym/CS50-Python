def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    plate = input("Plate: ")
    # Check the length of the plate
    if not 2 <= len(s) <= 6:
        return False
    #Check if the first two char is digits or not
    if s[0].isdigit() or s[1].isdigit():
        return False
    i = 0
    j = 0
    #Numbers cannot be used in the middle
    while i < len(s):
        if s[i] in [" ", ",", "."]:
            return False
        if s[i].isdigit():
            if s[i] == "0":
                return False
            else:
                while j < len(s):
                    if s[j].isalpha():
                        return False
                    if s[j] in [" ", ",", "."]:
                        return False
                    j += 1
                break
        i += 1
        j += 1
    return True

if __name__ == "__main__":
    main()