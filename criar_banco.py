import sqlite3

# Conecta ao banco de dados (ou cria, se não existir)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criação da tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
''')

# Criação da tabela de ingressos
cursor.execute('''
CREATE TABLE IF NOT EXISTS ingressos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_evento TEXT NOT NULL,
    preco REAL NOT NULL,
    disponivel INTEGER NOT NULL
)
''')

# Adiciona a coluna 'descricao' se ainda não existir
try:
    cursor.execute("ALTER TABLE ingressos ADD COLUMN descricao TEXT")
except sqlite3.OperationalError:
    pass  # Coluna já existe

# Criação da tabela de logs
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    acao TEXT NOT NULL,
    data_hora TEXT NOT NULL
)
''')

# Verifica se os ingressos já estão cadastrados
cursor.execute("SELECT COUNT(*) FROM ingressos")
qtd = cursor.fetchone()[0]

if qtd == 0:
    # Insere ingressos
    cursor.executemany('''
    INSERT INTO ingressos (nome_evento, preco, disponivel)
    VALUES (?, ?, ?)
    ''', [
        ("Show A", 100.0, 50),
        ("Show B", 80.0, 30),
        ("Teatro X", 50.0, 20)
    ])

    # Adiciona descrições aos ingressos
    cursor.execute("UPDATE ingressos SET descricao = 'Show de rock nacional com banda ao vivo.' WHERE nome_evento = 'Show A'")
    cursor.execute("UPDATE ingressos SET descricao = 'Festival de música pop com artistas internacionais.' WHERE nome_evento = 'Show B'")
    cursor.execute("UPDATE ingressos SET descricao = 'Peça teatral infantil para toda a família.' WHERE nome_evento = 'Teatro X'")

conn.commit()
conn.close()
print("Banco de dados criado com sucesso!")
