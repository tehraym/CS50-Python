def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    float_ = float(d.replace("$", ""))
    return(float_)

def percent_to_float(p):
    pfloat = float(p.replace("%", ""))
    return(pfloat / 100)
main()