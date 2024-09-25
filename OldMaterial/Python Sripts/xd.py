import requests
response=requests.get('https://hp-api.onrender.com/api/characters')

datajson=response.json()


for key, value in datajson.items():
    print(key, value)

