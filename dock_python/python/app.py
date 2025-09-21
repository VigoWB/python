from flask import Flask, jsonify, request, render_template
from models.lista_notatek import ListaNotatek
from config import Config #a co to i po co to?

app = Flask(__name__, static_folder='static', static_url_path='/')
app.config.from_object(Config) #a co to i po co to?


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "Vigo" and password == "haslo":
            return "Super"
        else:
            return "Błąd"

@app.route("/file_upload", methods=['POST'])
def pliki():
    return ""


@app.route("/hello")
def vigo():
    user = {'username': 'Vigo'}
    return '''
<html>
    <head>
        <title> Witanko!!!</title>
    </head>
    <body>
        <h1> Hello, ''' + user['username'] + '''! </h1>
    </body>
</html> '''



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
    lista = ListaNotatek()
    lista.id = 20
    lista.title = "Test"
    lista.pin = False
    lista.created_at = "2020-05-02 13:00:00"
    lista.updated_at = "2028-08-22 21:00:00"
    lista.color = "Magenta"
    lista.set_timestamp()
    return jsonify(lista.response())


# @app.route("/time")
# def time():
#     return {'time': time.time()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)