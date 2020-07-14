import requests

class Earnings:

    def __init__(self, key, ticker):

        self.api_key = key
        self.ticker = ticker

    def next_earnings_date(self):

        URL = f'https://cloud.iexapis.com/stable/stock/{self.ticker}/estimates/1/reportDate?token={self.api_key}'
        r = requests.get(URL)
        return r.text


    def earnings_today(self):

        URL = f'https://cloud.iexapis.com/stable/stock/market/today-earnings?token={self.api_key}'
        r = requests.get(URL)
        return r.text

    def earnings(self):

        URL = f'https://cloud.iexapis.com/stable/stock/{self.ticker}/earnings/?token={self.api_key}'
        #/stock/{symbol}/earnings/{last}/{field}
        r = requests.get(URL)
        return r.text
