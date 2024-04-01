import random


def main():
    while True:
        try:
            level = get_level()
            score = 0
            for _ in range(10):
                tries = 0
                answer = 0
                x, y = generate_integer(level)
                answer = x + y
                while tries < 3:
                    prompt = input((f"{x} + {y} = "))
                    if prompt.isdigit(): prompt = int(prompt)
                    if prompt == answer:
                        score += 1
                        break
                    else:
                        print("EEE")
                        tries += 1
                    if tries == 3:
                        print(f"{x} + {y} = {answer}")
            print(f"Score: {score}")
            break
        except ValueError:
            pass


def get_level():
    while True:
        try:
            p = int(input("Level: "))
            if p not in [1,2,3]:
                raise ValueError
            return p
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9), random.randint(0,9)
    elif level == 2:
        return random.randint(10,99), random.randint(10,99)
    elif level == 3:
        return random.randint(100,999), random.randint(100,999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()