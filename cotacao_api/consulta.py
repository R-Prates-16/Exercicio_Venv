import os
import requests
from dotenv import load_dotenv

load_dotenv() 

api_key = os.environ.get('API_KEY')
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

res = requests.get(url).json()
print('USD -> BRL:', res['conversion_rates']['BRL'])
print('USD -> EUR:', res['conversion_rates']['EUR'])
