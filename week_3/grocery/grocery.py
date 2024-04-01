def main():
    dict = {}
    while True:
        try:
            grocery = input()
            grocery = grocery.upper()
            if grocery in dict:
                dict[grocery] += 1
            else:
                dict[grocery] = 1
        except (EOFError, KeyError):
            break
    sorted_keys = sorted(dict.keys())
    for key in sorted_keys:
        value = dict[key]
        print(f"{value} {key}")

main()