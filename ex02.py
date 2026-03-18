class Pessoa:
    

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def saudação(self):
        print("Ola, meu nome é", self.nome)

p1 = Pessoa("Reinaldo", 17)

p1.saudação()

print(p1.nome,p1.idade)




    