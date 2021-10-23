import requests


HOST = 'http://127.0.0.1:8000'


resp = requests.post(f'{HOST}/api/adverts/', json={
    'owner': 'Vasya',
    'header': 'Toster 5',
    'description': 'Used, broken, 3 bucks'
})
print(resp.status_code)
print(resp.text)

resp = requests.get(f'{HOST}/api/adverts/1')
print(resp.status_code)
print(resp.text)

resp = requests.delete(f'{HOST}/api/adverts/1')
print(resp.status_code)
print(resp.text)

resp = requests.get(f'{HOST}/api/adverts/1')
print(resp.status_code)
print(resp.text)