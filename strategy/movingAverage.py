import MetaTrader5 as mt5
from datetime import datetime
import numpy as np
from binance.client import Client
import os
from dotenv import load_dotenv
from binance.spot import Spot as Client

client = Client(base_url="https://testnet.binance.vision")

print(client.time())

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
print(api_key)
print(api_secret)


try:
    account_info = client.get_account()
    print("Connected to Binance API successfully!")
    print("Account Info:", account_info)
except Exception as e:
    print("Failed to connect to Binance API:", str(e))

symbol = "BTCUSD"
quantity = 0.01


def calculate_sma(prices, period):
    sma = np.mean(prices[-period:])
    return sma


mt5.initialize()
authorized = mt5.login(69956869, password="qh5eyrsp")

utc_from = datetime(2023, 6, 20)
utc_to = datetime(2023, 6, 27)
rates = mt5.copy_rates_range("BTCUSD", mt5.TIMEFRAME_H1, utc_from, utc_to)

close_prices = [rate[4] for rate in rates]
short_term_period = 20
long_term_period = 50
short_term_sma = calculate_sma(close_prices, short_term_period)
long_term_sma = calculate_sma(close_prices, long_term_period)

if short_term_sma > long_term_sma:
    # Generate a buy signal
    order = Client.create_order(
        symbol=symbol,
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=quantity,
    )
    print("Buy order executed:", order)
elif short_term_sma < long_term_sma:
    # Generate a sell signal
    order = Client.create_order(
        symbol=symbol,
        side=Client.SIDE_SELL,
        type=Client.ORDER_TYPE_MARKET,
        quantity=quantity,
    )
    print("Sell order executed:", order)
else:
    print("No Trading Signal")
