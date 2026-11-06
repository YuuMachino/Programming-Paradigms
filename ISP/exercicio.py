formfrom abc import ABC, abstractmethod

"""
#Como seria a classe sem a segregação de abstratos
class Impressora(ABC):
    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def scanear(self):
        pass

    @abstractmethod
    def enviar_fax(self):
        pass


#Como seria a classe sem a segregação de abstratos
class ImpressoraBasica(Impressora):
        @abstractmethod
    def imprimir(self):
        print("Imprimindo.....")

    @abstractmethod
    def scanear(self):
        pass

    @abstractmethod
    def enviar_fax(self):
        pass
"""

#Como é com a segregação de interfaces
class Basica(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Multifuncional(ABC):
    @abstractmethod
    def scanear(self):
        pass
    @abstractmethod
    def enviar_fax(self):
        pass

class ImpressoraBasica(Basica):
    @abstractmethod
    def imprimir(self):
        print("Imprimindo.....")

class ImpressoraMultifuncional(Basica, Multifuncional):
    @abstractmethod
    def imprimir(self):
        print("Imprimindo.....")
    @abstractmethod
    def scanear(self):
        print("Scaneando.....")
    @abstractmethod
    def enviar_fax(self):
        print("Enviando.....")