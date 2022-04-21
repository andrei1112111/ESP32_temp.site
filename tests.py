import requests

data = {'temperature': 54.3}

print(requests.post('http://192.168.1.104:5000/send', data=data))
