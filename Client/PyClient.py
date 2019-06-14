from flask import request
from pathlib import Path

home = str(Path.home())
file = open(home + '/.ssh/id_rsa.pub', 'r')
public_key = file.read()

data = public_key
r = request.post('http://127.0.0.1:5000/', data = public_key)
print(data.text)
