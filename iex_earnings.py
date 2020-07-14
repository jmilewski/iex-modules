import requests

class Earnings:

    def __init__(self, key, ticker):

        self.api_key = key
        self.ticker = ticker

    def next_earnings_date(self):

        API_KEY = self.api_key
        ticker = self.ticker
        URL = f'https://cloud.iexapis.com/stable/stock/{ticker}/estimates/1/reportDate?token={API_KEY}'

        r = requests.get(URL)

        return r.text
