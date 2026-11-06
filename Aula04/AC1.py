class Pessoa:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def apresentar(self):
        print(f"Nome: {self.__nome}")
        print(f"E-mail:{self.__email}")

class Aluno(Pessoa):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.__curso=curso
    
    def get_curso(self):
        return self.__curso

    def apresentar(self):
        super().apresentar()
        print(f"Curso:{self.__curso}")

class Professor(Pessoa):#
    def __init__(self, nome, email, disciplina):
        super().__init__(nome, email)
        self.__disciplina=disciplina
    
    def get_disciplina(self):
        return self.__disciplina
    
    def apresentar(self):
        super().apresentar()
        print(f"Disciplica:{self.__disciplina}")

class Biblioteca:
    def pesquisar(self):
        print("Livro dentro da biblioteca!")

class Livro:
    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor
        self.biblioteca=Biblioteca()
    def pesquisar(self):
        print(f"Pesquisando {self.titulo} de {self.autor}")
        self.biblioteca.pesquisar()

aluno1=Aluno("Joao", "Joao@gmail.com", "ADS")
professor1=Professor("Pedro", "Pedro@gmail.com", "Programação")

aluno1.apresentar()
professor1.apresentar()

livro1=Livro("Marca da lua", "N.M.Rollings")
livro1.pesquisar()