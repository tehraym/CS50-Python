def main():
    while True:
        try:
            fuel = input("Fraction: ")
            a,b = fuel.split("/")
            a = int(a)
            b = int(b)
            if a > b:b = 0
            x = a/b
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if x <= 0.01:
                print("E")
                break
            elif x >= 0.99:
                print("F")
                break
            else:
                s = x * 100
                print(f"{round(s)}%")
                break
main()
