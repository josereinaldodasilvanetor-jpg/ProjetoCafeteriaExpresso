class Cafeteria:
    def __init__(self,cafe,lanche):
        self.__cafe = cafe
        self.__lanche = lanche
    def produtos(self):
        self.__cafe = [

               ("café preto",15),
               ("café gelado",30),
               ("chá",15),
               ("cappuccino",25),
               ("expresso",15)
               
]

        for produto, preco in self.__cafe:
            cafes = f"{produto}: R$ {preco:2f}"
            

       

    def menu():
        while True:
            print("1-cafes," ,"\n"
            "2-lanches", "\n"
            "3-acessorios","\n"
            "4-sair")
            escolha = int(input("escolha uma das opções"))

            if(escolha == 1):
                print("")
            elif(escolha == 2):
                print("")    

            elif(escolha == 3):
                print("")

            elif(escolha == 4):
                print("saindo....")
                break    

            else:
                print("opção invalida")

p1 = Cafeteria
print(p1.produtos)

