import requests
from settings import URL

url = URL['test']

login = URL['login']
dataLogin = URL['jsonTeacher']
r = requests.post(url=url+login, json=dataLogin)
print(r.url, r.json())
token = r.json()['token']

login = URL['group']
dataLogin = {'token': token}
r = requests.post(url=url+login, json=dataLogin)
print(r.url, r.json())

group_id = 1
login = URL['subjects']
dataLogin = {'token': token, 'group_id': group_id}
r = requests.post(url=url+login, json=dataLogin)
print(r.url, r.json())

login = URL['logout']
dataLogin = {'token': token}
r = requests.post(url=url+login, json=dataLogin)
print(r.url, r.json())
