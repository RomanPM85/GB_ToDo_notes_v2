import requests
from requests.auth import HTTPBasicAuth

# auth = HTTPBasicAuth(username='Roman', password='roman1')
# response = requests.get('http://127.0.0.1:8000/api/', auth=auth)
# print(response.json())
data = {'username': 'Roman', 'password': 'roman1'}
response = requests.post('http://127.0.0.1:8000/api-auth/', data=data)
token = response.json().get('token')
response_auth = requests.get('http://127.0.0.1:8000/api/books/', headers={'Authorization': f'Token {token}'})
print(response_auth.json())
