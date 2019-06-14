import requests
from pathlib import Path

# V grabs the public key and makes it into a string V
home = str(Path.home())
file = open(home + '/.ssh/id_rsa.pub', 'r')
public_key = file.read()

r = requests.post('http://127.0.0.1:5000/', json=public_key) #Data was used previously, json works by default though ...
# print('Public key response from server:', data)
# rFromServer = r.json()

dataToSend = {'question':'what is the answer?'} #set up a dictionary to send... equivalent might be %dict(question='what is the answer')%
res = requests.post('http://127.0.0.1:5000/', json=dataToSend) #post to localhost and jsonify it
print('response from server:', res.text)
dataFromServer = res.json() #stores the server's response ? IDK

#
# data = public_key
# r = request.post('http://127.0.0.1:5000/', data = public_key)
# print(data.text)
