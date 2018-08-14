import sqlite3

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE vendas (
        cpf VARCHAR(30) NOT NULL,
        produto VARCHAR(30) NOT NULL,
        valor INTEGER NOT NULL
);
""")

print('Tabela criada com sucesso.')

conn.close()