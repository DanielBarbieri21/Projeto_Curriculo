import psycopg2

class Curriculo:
    def __init__(self, conn):
        self.conn = conn
        self.criar_tabelas()

    def criar_tabelas(self):
        cur = self.conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS experiencia_trabalho (
                id SERIAL PRIMARY KEY,
                cargo TEXT,
                empresa TEXT,
                local TEXT,
                periodo TEXT,
                descricao TEXT
            )
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS formacao_academica (
                id SERIAL PRIMARY KEY,
                curso TEXT,
                instituicao TEXT,
                local TEXT,
                periodo TEXT
            )
        ''')

        # Adicione tabelas para cursos e hobbies aqui

        self.conn.commit()

    def imprimir_curriculo(self):
        # Implemente a lógica para imprimir o currículo
        pass

# Conectar ao PostgreSQL
try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="246895"
    )
    print("Conexão com o PostgreSQL bem-sucedida")

    meu_curriculo = Curriculo(conn)
    meu_curriculo.imprimir_curriculo()

except Exception as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")

finally:
    if conn is not None:
        conn.close()
        print("Conexão com o PostgreSQL fechada")
