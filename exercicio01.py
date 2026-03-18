class ContaBancaria:
    def __init__(self,nome,saldo):
        self.__nome = nome
        self.__saldo = saldo
    
    def depositar(self,valor):
        
        if valor > 0: 
            self.__saldo += valor
            print("valor depositado")
        else:
            print("valor invalido")
    
    def sacar(self,valor):
        if(sacar > self.__saldo):
            print("não tem saldo suficiente")
        
        elif valor <= 0:
            print("valor invalido")

        else:   
         self.__saldo -= valor
            
    def ver_nome(self):
        return self.__nome
    def ver_saldo(self):
        return self.__saldo

nome = input("digite seu nome:")
saldo = float(input("digite seu saldo inicial:"))



conta = ContaBancaria(nome,saldo)







while True:
        print("1-deposito\n"\
        "2-sacar\n"\
         "3-ver nome\n"\
        "4-ver saldo\n"\
        "5-sair")
                
                
        escolha = int(input("digite oque deseja:"))            

        if escolha == 1: 
            deposito = float(input("digite o valor que deseja depositar: "))
            conta.depositar(deposito)
    
        elif escolha == 2:
            sacar = float(input("digite o seu valor que deseja sacar:"))
            conta.sacar(sacar) 
            

        elif escolha == 3:
                print("nome:",conta.ver_nome())

        elif escolha == 4:
                print("saldo:",conta.ver_saldo())

        elif escolha == 5:
            print("encerrando codigo....")
            break

        else:
            print("erro numero invalido")
