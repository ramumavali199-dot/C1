import requests

def get_ohlcv(symbol="BTCUSDT", interval="15m", limit=6):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    r = requests.get(url, timeout=10)
    data = r.json()
    candles = [[float(c[1]), float(c[2]), float(c[3]), float(c[4]), float(c[5])] for c in data]
    return candles

def get_open_interest(symbol="BTCUSDT"):
    url = f"https://fapi.binance.com/fapi/v1/openInterest?symbol={symbol}"
    r = requests.get(url, timeout=10)
    data = r.json()
    return float(data["openInterest"])
