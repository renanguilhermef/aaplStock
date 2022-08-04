#This module connects on StockData.org api and retrieve data 
import requests                         # requests package for REST interaction
import urllib3

class stock:
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.url = " https://api.stockdata.org/"
        self.token = "eB88KmJBcVooWGckgvx9QIP9CuUL7iHddna7Fd0X"

    def get_historical_data(self,ticker):
        end_point = self.url + "v1/data/eod?symbols=" + ticker + "&api_token=" + self.token
        response = requests.get(end_point, verify=False)
        return response.json()    


