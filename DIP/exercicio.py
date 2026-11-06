from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def disponibilizar(self):
        pass

    def mensagem_notificacao(self):
        return "Empréstimo realizado com sucesso!"

class Devolvivel(ABC):
    @abstractmethod
    def devolver(self):
        pass

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass


class Livro (Material, Devolvivel):
    def disponibilizar(self):
        print(f"Livro: {self.titulo} emprestado.")

    def devolver(self):
        print(f"Livro: {self.titulo} devolvido.")

class Revista (Material, Devolvivel):
    def disponibilizar(self):
        print(f"Revista: {self.titulo} emprestada.")

    def devolver(self):
        print(f"Revista: {self.titulo} devolvida.")

class Ebook (Material):
    def disponibilizar(self):
        print(f"Ebook: {self.titulo} liberado.")

    def mensagem_notificacao(self):
        return "Acesso digital liberado com sucesso!"


class EmprestimoRepository:
    def registrar(self, usuario):
        print(f"Empréstimo registrado para {usuario}.")


class EmailService (Notificador):
    def enviar(self, mensagem):
        print("Email:", mensagem)

class SMSService (Notificador):
    def enviar(self, mensagem):
        print("SMS:", mensagem)


class EmprestimoService:
    def __init__(self, notificador: Notificador, repositorio: EmprestimoRepository):
        self.notificador = notificador
        self.repositorio = repositorio

    def emprestar(self, material: Material, usuario):
        material.disponibilizar()
        self.repositorio.registrar(usuario)
        self.notificador.enviar(material.mensagem_notificacao())


class Audiobook (Material):
    def disponibilizar(self):
        print(f"Audiobook: {self.titulo} liberado para audição.")

    def mensagem_notificacao(self):
        return "Audiobook liberado para audição com sucesso!"


email = EmailService()
sms = SMSService()
repositorio = EmprestimoRepository()

livro = Livro("Python para Iniciantes", "Autor A")
revista = Revista("Tecnologia Hoje", "Editora B")
ebook = Ebook("Aprendendo POO", "Autor C")
audiobook = Audiobook("Clean Code em Áudio", "Autor D")

servico_email = EmprestimoService(email, repositorio)
servico_sms = EmprestimoService(sms, repositorio)

servico_email.emprestar(livro, "Maria")
servico_sms.emprestar(revista, "João")
servico_email.emprestar(ebook, "Ana")
servico_sms.emprestar(audiobook, "Carlos")
