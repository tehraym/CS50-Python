from validator_collection import validators

def main():
    try:
        if validators.email(input("Whats Your Email Address? ")):
            print("Valid")
        else:
            print("Invalid")
    except Exception as err:
        print("Invalid")

if __name__ == "__main__":
    main()
