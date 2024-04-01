def main():
    i = 50
    while i > 0:
        print("Amount Due:", i)
        coin = int(input("Insert Coin:"))
        if coin in [5,10,25]:
            i -= coin
    print("Change Owed:", i * -1)
main()