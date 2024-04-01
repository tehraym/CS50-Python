import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            guess = 0
            x = random.randrange(1,level)
            while True:
                guess = input("Guess: ")
                if not guess.isdigit():
                    guess = input("Guess: ")
                else:
                    guess = int(guess)
                    if x > guess:
                        print("Too small!")
                    elif guess > x:
                        print("Too large!")
                    elif guess == x:
                        print("Just right!")
                        break
        except ValueError:
            pass

if __name__ == "__main__":
    main()