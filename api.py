# app.py
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)

db = TinyDB("caminhos.json")
caminho_tabela = db.table('Caminhos')
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/novo", methods=["POST"])
def new(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
        x = request.form.get("x")
        y = request.form.get("y")
        z = request.form.get("z")
        r = request.form.get("r")
        caminho_tabela.insert({"nome": nome ,'coordinates':{ "x":x,"y":y,"z":z,"r":r}})
    return redirect(url_for('index'))

@app.route("/pegar_caminho/<name>")
def find_route(name):
    query = Query()
    paths = caminho_tabela.search(query.nome == name)
    print(paths)
    return render_template("path.html", paths = paths )


@app.route("/listas_caminhos")
def listar():
    var = caminho_tabela.all()
    return render_template("paths.html", paths = var )


@app.route("/atualizar")
def atualizar():
    return render_template("atualizar.html")


@app.route("/deletar/<id>")
def delete(id):
    string_new = "{id}"
    print(string_new)
    query = Query()
    caminho_tabela.remove(query.doc_id == string_new)
    return redirect(url_for('listar'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)