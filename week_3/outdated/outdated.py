def main():
    list = ["Nothing",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
            ]
    while True:
        try:
            date = input("Date: ")
            if date[0].isdigit() or date[3].isdigit():
                date = date.strip('" ')
                a,b,c = date.split("/")
                a = int(a)
                b = int(b)
                c = int(c)
                if a <= 12 and b <= 30:
                    print(f"{c}-{a:02}-{b:02}")
                    break
            elif date[0].isalpha():
                if date[-6] != ",":
                    date = 0
                d,e,f = date.split(" ")
                d = d.title()
                e = e.replace(",","")
                month = list.index(d,1)
                f = int(f)
                e = int(e)
                month = int(month)
                if month <= 12 and e <= 30:
                    print(f"{f}-{month:02}-{e:02}")
                    break
        except (ValueError, EOFError, KeyError, NameError,AttributeError):
            pass

main()