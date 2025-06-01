import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS ingressos")
cursor.execute("DROP TABLE IF EXISTS usuarios")
cursor.execute("DROP TABLE IF EXISTS logs")

cursor.execute('''
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE ingressos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_evento TEXT NOT NULL,
    descricao TEXT NOT NULL,
    preco REAL NOT NULL,
    disponivel INTEGER NOT NULL,
    data_evento TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        nome_usuario TEXT,
        email_usuario TEXT,
        acao_usuario TEXT,
        data_hora TEXT,
        classification TEXT,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)
''')

cursor.executemany('''
INSERT INTO ingressos (nome_evento, descricao, preco, disponivel, data_evento)
VALUES (?, ?, ?, ?, ?)
''', [
    ("Show A", "Espetáculo musical com banda ao vivo", 100.00, 50, "2025-07-10"),
    ("Teatro X", "Peça premiada com elenco renomado", 80.00, 40, "2025-08-05"),
    ("Festival Z", "Festival com atrações nacionais", 120.00, 60, "2025-09-20")
])

conn.commit()
conn.close()
print("Banco de dados criado com sucesso!")
