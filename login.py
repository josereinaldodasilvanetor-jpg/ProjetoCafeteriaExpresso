class Conta: 
    def __init__(self,nome,senha,email):
        self.__nome = nome
        self.__senha = senha
        self.__email = email

    def cadastro(self):
        self.__nome = input("digite seu nome:")
        self.__senha = input("digite sua senha:")
        self.__email = input("digite seu email:")



    def login(self):
        print("-"*30)
        ab = input("digite seu email:")
        bc = input("digite sua senha:")
        if(ab == self.__email and bc == self.__senha  ):
            print("logando...")
        else:
            print("seu email ou sua senha estão incorretos")
co = Conta("a","b","c")

while True:
    print("1-cadastro","\n",
          "2-login","\n",
          "3-sair")
    opção = int(input("digite uma opção:"))

    if(opção == 1):
        co.cadastro()
    elif(opção == 2):
        co.login()
    elif(opção == 3):
        print("encerrando sistema...")
        break
    else:
        print("opção invalido")
        



        












    