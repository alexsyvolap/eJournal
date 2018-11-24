import requests
# http://ad6e06fc.ngrok.io
url = 'http://127.0.0.1:8080'

login = '/api/auth/login'
dataLogin = {'email': 'a', 'password': 'a'}
r = requests.post(url=url+login, json=dataLogin)
print(r.url, r.json())