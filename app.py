from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'segredo_super_secreto'

# Caminho seguro para o banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

def conectar():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.before_request
def carregar_usuario():
    g.usuario = None
    if "usuario_id" in session:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (session["usuario_id"],))
        g.usuario = cursor.fetchone()
        conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
            conn.commit()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            return render_template("cadastro.html", erro="Email já cadastrado.")
        finally:
            conn.close()
    return render_template("cadastro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()
        conn.close()
        if usuario:
            session["usuario_id"] = usuario["id"]
            return redirect(url_for("ingressos"))
        else:
            return render_template("login.html", erro="Email ou senha incorretos.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/ingressos")
def ingressos():
    if not g.usuario:
        return redirect(url_for("login"))
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingressos")
    lista = cursor.fetchall()
    conn.close()

    sucesso = request.args.get("sucesso")  # ← Novo
    return render_template("ingressos.html", ingressos=lista, sucesso=sucesso)

@app.route("/comprar/<int:id>", methods=["POST"])
def comprar(id):
    if not g.usuario:
        return redirect(url_for("login"))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nome_evento, preco, disponivel FROM ingressos WHERE id = ?", (id,))
    ingresso = cursor.fetchone()

    if ingresso and ingresso["disponivel"] > 0:
        cursor.execute("UPDATE ingressos SET disponivel = disponivel - 1 WHERE id = ?", (id,))
        cursor.execute('''
            INSERT INTO logs (usuario, acao, data_hora)
            VALUES (?, ?, datetime('now', 'localtime'))
        ''', (g.usuario["nome"], f"Comprou ingresso para: {ingresso['nome_evento']}"))
        conn.commit()

    conn.close()
    return redirect(url_for("ingressos", sucesso="compra"))  # ← Adicionado

if __name__ == "__main__":
    app.run(debug=True)
