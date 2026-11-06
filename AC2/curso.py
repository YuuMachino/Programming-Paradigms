class CursoOnline:
    def __init__(self, titulo, carga_horaria):
        self.__titulo = titulo
        self.__carga_horaria = carga_horaria
    
    def get_titulo(self):
        return self.__titulo

    def get_carga_horaria(self):
        return self.__carga_horaria

    def iniciar_aula(self):
        pass

class Instrutor:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome


class CursoProgramacao(CursoOnline):
    def __init__(self, titulo, carga_horaria, nomeInstrutor):
        super().__init__(titulo, carga_horaria)
        self.instrutor = Instrutor(nomeInstrutor)

    def iniciar_aula(self):
        super().iniciar_aula()
        print(f"Iniciando aula de programação com o instrutor: {self.instrutor.get_nome()}")

class CursoDesign(CursoOnline):
    def __init__(self, titulo, carga_horaria, nomeInstrutor):
        super().__init__(titulo, carga_horaria)
        self.instrutor = Instrutor(nomeInstrutor)

    def iniciar_aula(self):
        super().iniciar_aula()
        print(f"Iniciando aula de design com o instrutor: {self.instrutor.get_nome()}")

cursos = [
    CursoProgramacao("Java", "60h", "Jose"),
    CursoDesign("Croma", "60h", "Paulo")
]
for curso in cursos:
    curso.iniciar_aula()