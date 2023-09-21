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

def att_user(id,dict_mudancas):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor =  conn.cursor()
    cursor.execute(f"""
    SELECT * FROM Usuarios WHERE id = {id}
""")
    user = cursor.fetchall()
    if user != []:
        for coluna, valor in dict_mudancas.items():
            if coluna == 'cpf' and len(valor) != 11:
                return f'{coluna.capitalize()} precisa ter 11 digitos'
            elif coluna == 'idade' and (valor > 120 or valor < 0):
                return f'{coluna.capitalize()} irregular'
            elif coluna == 'email' and (valor.find('@') == -1 or valor.find('@') == len(valor)-1):
                return f'{coluna.capitalize()} irregular'
            cursor.execute(f"""
            UPDATE Usuarios SET '{coluna}' = '{valor}' WHERE id = {id}
""")
        conn.commit()
        return 'Usuário atualizado com sucesso'
    else:
        return 'Usuário não encontrado'
    
def del_user(id):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT * FROM Usuarios WHERE id = {id}
""")
    if cursor.fetchall() == []:
        return 'Usuário não encontrado'
    
    cursor.execute(f"""
    DELETE FROM Usuarios WHERE id = {id}
""")
    return 'Usuário deletado'


