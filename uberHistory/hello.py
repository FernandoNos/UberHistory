from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    print request
    print request.args
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)


