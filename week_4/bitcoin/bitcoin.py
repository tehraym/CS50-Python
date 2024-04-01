import sys
import requests

def main():
    try:
        total = sys.argv[1]
        total = float(total)
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        r = r.json()
        data = float(r["bpi"]["USD"]["rate"].replace(",", ""))
        amount = total * data
        print(f"${amount:,.4f}")


    except requests.RequestException:
        pass

main()
