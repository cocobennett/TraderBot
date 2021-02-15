import MetaTrader5 as mt5
from datetime import datetime

account = int(41464506)

mt5.initialize()
authorized=mt5.login(account)

if authorized:
    print("Connected: Connecting to MT5 Client")
else:
    print("Failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

utc_from = datetime(2021, 1, 1)
utc_to = datetime(2021, 1, 10)
rates = mt5.copy_rates_range("EURUSD", mt5.TIMEFRAME_H4, utc_from, utc_to)

for rate in rates:
    print(rate)
