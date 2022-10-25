import requests

response = requests.post('http://127.0.0.1:8000/api-token-auth/',
                         data={'user_name': 'big', 'password': 'big123456'})
print(response.status_code)
print(response.json())
