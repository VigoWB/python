import time
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Co do chuja aaa?"


@app.route("/time")
def time():
    return {'time': time.time()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
