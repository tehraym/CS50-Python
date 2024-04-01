def main():
    tweet = input("Input: ")
    twtter = ""
    for i in tweet:
        if i not in ["a","e","i","o","u","A","E","I","O","U"]:
            twtter += i
    print(twtter)

main()