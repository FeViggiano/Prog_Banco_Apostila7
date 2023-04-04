import psycopg
print(psycopg)

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

def existe (usuario):
    with psycopg.connect(
        host="localhost",
        dbname="Progrmacao_Hoje",
        port=5432,
        user='postgres',
        password='123456'
    ) as conexao:  
      with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
        (f'{usuario.login}',
        f'{usuario.senha}')
        )
        result = cursor.fetchone()
        return result != None
      
def novo_usuario (usuario):
    with psycopg.connect(
        host="localhost",
        dbname="Progrmacao_Hoje",
        port=5432,
        user='postgres',
        password='123456'
    ) as conexao:  
      with conexao.cursor() as cursor:
         cursor.execute('INSERT INTO tb_usuario (login,senha) VALUES (%s, %s)', 
        (f'{usuario.login}',
         f'{usuario.senha}')
         )    

# print(existe(Usuario('admin', 'admin')))
        
def menu():
    texto = '0-Fechar sistema\n1-Login\n2-Logoff\n3-Add\n'
    usuario = None
    opcao = int(input(texto))
    while opcao != 0:
        if opcao == 1:
            login = input("Digite seu login\n")
            senha = input("Digite sua senha\n")
            usuario = Usuario(login, senha)
            # Expressão condicional (if/else de uma linha só)
            print("Usuário OK!" if existe(usuario) else "Usuário NOK!")
        elif opcao == 2:
            usuario = None
            print ("Logoff realizado com sucesso")
        
        # Inserindo o novo Usuário
        elif opcao == 3:
            login = input('Digite o novo usuario do sistema\n')
            senha = input('Digite a senha do novo usuário do sistema\n')
            novo_user = Usuario (login, senha)
            print('Usuário não inserido no sistema' if novo_usuario(novo_user)
                else 'Usuário inserido no sistema com sucesso')
    else:
        print('Até mais')
    opcao = int(input(texto))

menu()