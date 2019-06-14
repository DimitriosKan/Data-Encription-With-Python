from flask import Flask, render_template, request, url_for, jsonify
from pathlib import Path

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def flask_server():
    home = str(Path.home())
    file = open(home + '/.ssh/id_rsa.pub', 'r')
    public_key = file.read()

    inbound_data = request.get_json()
    print('data from client:', inbound_data)
    return jsonify(public_key)

    # input_json = request.get_json()
    # print('data from client:', input_json)
    # dictToReturn = {'here be':'public key'} # have this call the ssh key the way it was done on client side
    # return jsonify(dictToReturn)

# @app.route('/', methods = ['POST'])
# def flask_server():
#     x = request.data
#     return "Your post request is: " + str(x)
#     print(x)

if __name__ == '__main__':
    app.run(debug=True)
