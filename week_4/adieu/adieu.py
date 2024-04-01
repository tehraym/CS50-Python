import inflect
p = inflect.engine()

def main():
    x = []
    while True:
        try:
            name = input("")
            x.append(name)
        except EOFError:
            break
    x = p.join(x)
    print("Adieu, adieu, to", x)

if __name__ == "__main__":
    main()
