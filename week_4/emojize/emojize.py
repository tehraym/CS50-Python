from emoji import emojize

def main():
    emoji = input("Input: ")
    print(emojize(emoji, language = 'alias'))

main()
