def main():
    while True:
        try:
            frac = input("Fraction: ")
            z = convert(frac)
            fuel = gauge(z)
            print(fuel)
            break

        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y: y = 0
    z = x/y
    return z

def gauge(percentage):
    if percentage < 0.01:
        return "E"
    elif percentage >= 0.99:
        return "F"
    else:
        return f"{round(percentage * 100)}%"

if __name__ == "__main__":
    main()