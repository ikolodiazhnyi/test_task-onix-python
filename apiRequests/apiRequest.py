import json
from requests import get
res = get('https://reqres.in/api/users')
json = res.json();
users = json['data']
for user in users:
	print(user['email'])