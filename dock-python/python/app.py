import time
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Co do chuja aaa?"

@app.route("/hello")
def BU():
    return "Witaj wielki BU"

@app.route('/potega/<int:liczba>')
def potega(liczba):
    wynik = liczba ** 2
    wynikczy = liczba ** 3
    return f"{liczba} do potęgi: {wynik}, a do 3 gratis {wynikczy}"


@app.route("/time")
def time():
    return {'time': time.time()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
