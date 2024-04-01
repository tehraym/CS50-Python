import re

def main():
    print(count(input("Text: ")))

def count(s):
    ums = re.findall(r"\bum\b", s.lower())
    return ums.count('um')

if __name__ == "__main__":
    main()
