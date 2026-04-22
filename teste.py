class Pessoa:
    def __init__(self, nome, idade):
     self.nome = nome 
     self.idade = idade

pessoa1 = Pessoa("Maria santos", 30)


print("nome:", pessoa1.nome)
print("idade:", pessoa1.idade)
