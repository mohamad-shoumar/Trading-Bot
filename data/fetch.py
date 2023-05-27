import MetaTrader5 as mt5
from datetime import datetime

account = int(69956869)

mt5.initialize()
authorized = mt5.login(account)

if authorized:
    print("Connected: Connecting to MT5 Client")
else:
    print(
        "Failed to connect at account #{}, error code: {}".format(
            account, mt5.last_error()
        )
    )

utc_from = datetime(2023, 6, 20)
utc_to = datetime(2023, 6, 27)
rates = mt5.copy_rates_range("EURUSD", mt5.TIMEFRAME_H4, utc_from, utc_to)

for rate in rates:
    print(rate)
