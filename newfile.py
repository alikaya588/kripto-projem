# crypto_price.py
import requests

def get_crypto_price(crypto_id="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data[crypto_id]["usd"]
        print(f"{crypto_id.capitalize()} fiyatı: ${price}")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    get_crypto_price()