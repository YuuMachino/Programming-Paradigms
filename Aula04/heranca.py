class Pessoa:
    #contrutor é um metodo e todo metodo precisa de um self
    def __init__(self, nome, idade, email, curso):
        self.__nome=nome
        self.__idade=idade
        self.__email=email

    def get_nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, valor):
        if valor>=18:
            self.__idade=valor


    def set_email(self, email):
        if self.__email.lenght>3:
            self.__email=email

    
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail:{self.email}")

class Aluno(Pessoa):#Dessa forma, a classe aluno é filha da classe pessoa
    def __init__(self, nome, idade, email, curso):
        super().__init__(nome, idade, email)#super é uma funcao que, com essa
        #construção, permite que a herança ocorra definitivamente no python
        self.curso=curso
    def apresentar(self):
        super().apresentar()
        print(f"Curso:{self.curso}")#o Super tambem funciona com o outros metodos que
        #tambem podem ser herdados
    
    

aluno1=Aluno("nome", 18, "email")
aluno1.apresentar()

#polimorfismo: Se a classe tiver dois metodos com o mesmo nome, eles podem ter comportamentos diferentes
#Mesmo que tenham nomes identicos