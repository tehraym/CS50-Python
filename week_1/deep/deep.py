def main():
    x = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    s = x.strip()
    is42(s.lower())

def is42(x):
    if x == "42" or x == "forty two" or x =="forty-two":
        print("Yes")
    else:
        print("No")

main()