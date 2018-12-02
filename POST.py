import requests
from settings import URL

url = URL['test']

login = URL['login']
dataLogin = URL['jsonStudent']
r = requests.post(url=url+login, json=dataLogin)
print(r.url, r.json())
token = r.json()['token']

login = URL['group']
dataLogin = {'token': token}
r = requests.post(url=url+login, json=dataLogin)
print(r.url, r.json())
