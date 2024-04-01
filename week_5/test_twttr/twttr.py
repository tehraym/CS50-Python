def main():
    x = input("Input: ")
    print("Output:", shorten(x))

def shorten(word):
    s = ""
    for i in word:
        if i not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            s += i
    return s

if __name__ == "__main__":
    main()