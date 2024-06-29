usuario = ("Sarah57")
senha = ('123456')

login = input("Digite seu usuario: ")
login_senha = input("Digite sua senha: ")

if login == usuario and login_senha == senha:
    print("Usuario e senha concedido")
else:
    print('usuario e senha negado')    