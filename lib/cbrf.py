import requests
import xmltodict


class CBRFApi:
    BASE_URL = 'https://www.cbr-xml-daily.ru/'

    def get_daily_rates(self):
        """Получение ежедневных курсов валют."""
        response = requests.get(f'{self.BASE_URL}daily_json.js')
        response.raise_for_status()
        return response.json()

    def get_dynamic_rates(self, currency_id, start_date, end_date):
        """Получение динамики курсов валюты за период."""
        dynamic_url = f'{self.BASE_URL}dynamic/{start_date}/{end_date}/{currency_id}.json'
        response = requests.get(dynamic_url)
        response.raise_for_status()
        return response.json()

    def get_currencies_list(self):
        """Получение списка валют."""
        response = requests.get(f'{self.BASE_URL}daily_json.js')
        response.raise_for_status()
        data = response.json()
        return data['Valute']

    def get_currency_info(self, currency_char_code):
        """Получение информации о конкретной валюте."""
        daily_rates = self.get_daily_rates()
        return daily_rates['Valute'].get(currency_char_code)


class CBRService:
    def __init__(self):
        self.base_url = "http://www.cbr.ru/scripts/"

    def get_daily_quotes(self, date_req=None):
        url = self.base_url + "XML_daily.asp"
        params = {'date_req': date_req} if date_req else {}
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content)

    def get_currency_codes(self, daily=True):
        url = self.base_url + "XML_val.asp"
        params = {'d': '0' if daily else '1'}
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content)

    def get_dynamic_quotes(self, date_req1, date_req2, val_nm_rq):
        url = self.base_url + "XML_dynamic.asp"
        params = {
            'date_req1': date_req1,
            'date_req2': date_req2,
            'VAL_NM_RQ': val_nm_rq
        }
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content)

    def get_correspondent_account_balances(self, date_req1, date_req2):
        url = self.base_url + "XML_ostat.asp"
        params = {
            'date_req1': date_req1,
            'date_req2': date_req2
        }
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content)