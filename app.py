import sqlite3

def add_usuario(nome,idade,cpf,endereco,email):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    indice_arroba = email.find('@')
    if idade < 0:
        return False
    elif idade > 120:
        return False
    elif len(cpf) != 11:
        return False
    elif indice_arroba == -1:
        return False
    elif indice_arroba == len(email)-1:
        return False
    cursor.execute("""
        INSERT INTO Usuarios (nome, idade, cpf, endereco, email) 
        VALUES (?, ?, ?, ?, ?)
    """, (nome, idade, cpf, endereco, email))

    conn.commit()
    return f'Usuário Cadastrado'

def ver_usuario(id):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT * FROM Usuarios WHERE id = {id}
    """)
    return cursor.fetchall()

def ver_usuarios():
        conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT * FROM Usuarios
    """)
    return cursor.fetchall()


