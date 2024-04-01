def interpreter(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

def main():
    equation = input("Expression: ")
    x, y, z = equation.split(" ")
    x = float(x)
    z = float(z)
    print(interpreter(x, y, z))

main()