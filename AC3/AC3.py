from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# Parte 1 — Materiais (abstração base)
# ---------------------------------------------------------------
class Material(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def disponibilizar(self):
        pass

    def mensagem_notificacao(self):
        # Comportamento padrão; cada material pode sobrescrever.
        # Assim o serviço não precisa de if/elif para saber o tipo.
        return "Empréstimo realizado com sucesso!"


# ---------------------------------------------------------------
# Parte 2 — ISP: só quem pode ser devolvido implementa Devolvivel
# ---------------------------------------------------------------
class Devolvivel(ABC):
    @abstractmethod
    def devolver(self):
        pass


class Livro(Material, Devolvivel):
    def disponibilizar(self):
        print(f"Livro: {self.titulo} emprestado.")

    def devolver(self):
        print(f"Livro: {self.titulo} devolvido.")


class Revista(Material, Devolvivel):
    def disponibilizar(self):
        print(f"Revista: {self.titulo} emprestada.")

    def devolver(self):
        print(f"Revista: {self.titulo} devolvida.")


class Ebook(Material):  # não implementa Devolvivel
    def disponibilizar(self):
        print(f"Ebook: {self.titulo} liberado.")

    def mensagem_notificacao(self):
        return "Acesso digital liberado com sucesso!"


# ---------------------------------------------------------------
# Parte 3 — SRP: só registra empréstimos
# ---------------------------------------------------------------
class EmprestimoRepository:
    def registrar(self, usuario):
        print(f"Empréstimo registrado para {usuario}.")


# ---------------------------------------------------------------
# Parte 4 — DIP: abstração de notificação + implementações
# ---------------------------------------------------------------
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass


class EmailService(Notificador):
    def enviar(self, mensagem):
        print(f"Email: {mensagem}")


class SMSService(Notificador):
    def enviar(self, mensagem):
        print(f"SMS: {mensagem}")


# ---------------------------------------------------------------
# Parte 5 — OCP/LSP: serviço depende só de abstrações
# ---------------------------------------------------------------
class EmprestimoService:
    def __init__(self, notificador: Notificador, repositorio: EmprestimoRepository):
        self.notificador = notificador
        self.repositorio = repositorio

    def emprestar(self, material: Material, usuario):
        material.disponibilizar()
        self.repositorio.registrar(usuario)
        self.notificador.enviar(material.mensagem_notificacao())


# Novo material: não exige alterar nenhuma classe anterior (OCP)
# e substitui qualquer Material no serviço sem quebrar nada (LSP).
class Audiobook(Material):
    def disponibilizar(self):
        print(f"Audiobook: {self.titulo} liberado para audição.")

    def mensagem_notificacao(self):
        return "Audiobook liberado para audição com sucesso!"

if __name__ == "__main__":
    repositorio = EmprestimoRepository()

    EmprestimoService(EmailService(), repositorio).emprestar(
        Livro("Python para Iniciantes", "Autor A"), "Maria"
    )
    print()
    EmprestimoService(SMSService(), repositorio).emprestar(
        Revista("Tecnologia Hoje", "Editora B"), "João"
    )
    print()
    EmprestimoService(EmailService(), repositorio).emprestar(
        Ebook("Aprendendo POO", "Autor C"), "Ana"
    )
    print()
    EmprestimoService(SMSService(), repositorio).emprestar(
        Audiobook("Clean Code em Áudio", "Autor D"), "Carlos"
    )