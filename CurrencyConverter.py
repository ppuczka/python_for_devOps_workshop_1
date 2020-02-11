import requests
from requests.exceptions import HTTPError
# add logging 
class CurrencyConverter():
    

    def _url(self, query_path):
        return "https://api.exchangeratesapi.io/latest?base=" + query_path

    def get_latest_currency_rate(self, currency_code):
        request_path = self._url(currency_code)
        response = requests.get(request_path)
        if response.status_code == 200:
            json_response = response.json()
            return json_response.get('rates')
        elif response.status_code > 299:
            status_code = response.status_code
            print(f"Error while getting request {status_code}")
       