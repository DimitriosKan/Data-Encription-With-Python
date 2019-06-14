from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def hello_world():
    print(request.data)
    return "You sent me this: " + str(request.data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
