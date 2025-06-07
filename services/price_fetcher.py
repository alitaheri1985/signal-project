import requests

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["bitcoin"]["usd"]
        return f"${price:,.2f}"
    except Exception as e:
        return "خطا در دریافت قیمت بیت‌کوین"
