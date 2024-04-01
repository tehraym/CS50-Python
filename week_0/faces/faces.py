def main():
    x = input()
    print(convert(x))

def convert(to):
    converted = to.replace(":)", "🙂").replace(":(", "🙁")
    return(converted)

main()