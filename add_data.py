import sqlite3

conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO login (nome, usuario, senha)
VALUES ('Usuario Master', 'master', 'master')
""")


# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()