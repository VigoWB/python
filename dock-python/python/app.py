import time
from flask import Flask
from models.lista_notatek import ListaNotatek

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


# @app.route('/lists', methods=['GET'])
# def lista():
#     return "TO JEST LISTA LIST"


@app.route('/lists/<int:listId>', methods=['GET'])
def lista(listId: int):
    lista = ListaNotatek(listId)
    lista.title = "Test"
    lista.pin = False
    lista.color = "Magenta"
    return lista.response()


@app.route("/time")
def time():
    return {'time': time.time()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
