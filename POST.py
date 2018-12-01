import requests
from settings import URL

url = URL['test']

login = URL['login']
dataLogin = {'email': '1', 'password': '1'}
r = requests.post(url=url+login, json=dataLogin)
print(r.url, r.json())