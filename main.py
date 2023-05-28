import os
from dotenv import load_dotenv
import datetime
from binance.client import Client

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
client = Client(api_key, api_secret, testnet=True)
end_time = datetime.datetime.now()
start_time = end_time - datetime.timedelta(hours=24)

start_time_str = str(int(start_time.timestamp() * 1000))
end_time_str = str(int(end_time.timestamp() * 1000))

klines = client.get_historical_klines(
    "BTCUSDT", Client.KLINE_INTERVAL_1HOUR, start_time_str, end_time_str
)
for kline in klines:
    print(kline)
