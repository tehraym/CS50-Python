def payment(s):
    x = s.strip()
    if x.startswith("hello"):
        print("$0")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")

def main():
    x = input("Greeting: ")
    payment(x.lower())

main()