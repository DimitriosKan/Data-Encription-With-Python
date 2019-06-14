from flask import Flask, request

app = Flask(__name__)
# @app.route('/', methods = ['POST'])
@app.route('/')
def flask_server():
    x = request.data
    return "Your post request is: " + str(x)
    print(x)

if __name__ == "__main__":
    app.run()
