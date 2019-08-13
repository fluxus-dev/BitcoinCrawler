import datetime
import json
import os
import time

import pandas as pd

from BitcoinAPI import get_ticker, get_order_book

while True:

    data = json.loads(get_ticker().text)
    print(data['data']['date'])
    data['data']['date'] = datetime.datetime.fromtimestamp(int(data['data']['date']) / 1000)
    df = pd.DataFrame([data['data']])

    order_data = json.loads(get_order_book().text)
    order_df = pd.DataFrame([order_data['data']])
    df['bids'] = order_df['bids']
    df['asks'] = order_df['asks']
    if not os.path.isfile('BitcoinData2.csv'):
        df.to_csv('BitcoinData2.csv')
    else:
        df.to_csv('BitcoinData2.csv', mode='a', header=False)

    time.sleep(1)


