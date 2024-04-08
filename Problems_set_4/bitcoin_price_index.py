import sys
import requests


try:

    if len(sys.argv) <= 1:
        raise requests.RequestException
    if sys.argv[1].isalpha():
        raise ValueError
    
    
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    data = response.json()
    usd = data["bpi"]["USD"]["rate"]


    bitcoin = float(sys.argv[1])
    usd = usd.replace(",", "")
    bitcoin_to_usd = float(usd) * float(bitcoin)
    print(f"${bitcoin_to_usd:,.4f}")
    
except requests.RequestException:
    sys.exit("Missing Command-line argument.")
except ValueError:
    sys.exit("Comand-line argument is not a number ")   