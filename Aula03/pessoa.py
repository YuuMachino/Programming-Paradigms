class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1=Pessoa("Joao", 13)
p2=Pessoa("Maria", 12)

print(p1.nome)
print(p2.nome)

#Como uma classe se transforma em função? Pelo meu construtor
#instanciar é criar um objeto
#atributos é tudo aquilo que a classe tem 
#metodos é tudo que a classe faz

