def main():
    x = input("What Time is it? ")
    s = convert(x)
    if 7.0 <= s <= 8.0:
        print("Breakfast time")
    elif 12.0 <= s <= 13.0:
        print("Lunch time")
    elif 18.0 <= s <= 19.0:
        print("Dinner time")

def convert(time):
    a = 0
    if time.endswith("p.m.") or time.endswith("a.m."):
        o, p = time.split(" ")
        if p == "p.m.": a += 12
        h, m = o.split(":")
        h = float(h)
        m = float(m)
        m = m / 60
        return a + h + m

    else:
        h, m = time.split(":")
        h = float(h)
        m = float(m)
        m = m / 60
        return h + m

if __name__ == "__main__":
    main()