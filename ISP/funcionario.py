from abc import ABC, abstractmethod

class Trabalhavel(ABC):
    @abstractmethod
    def trabalhar(self):
        pass
class Progamavel(ABC):
    @abstractmethod
    def trabalhar(self):
        pass
class Dirigivel(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

"""
class Funcionario(ABC):
    @abstractmethod #nosso decorator, ele demor que o nosso metodos precise ser abstrata
    def trabalhar(self):
        pass

    @abstractmethod
    def dirigir(self):
    
    
        pass
    @abstractmethod
    def programar(self):
        pass
    """
class Progamador(Trabalhavel, Progamavel):
    @abstractmethod
    def trabalhar(self):
        print ("trabalhando...")
    @abstractmethod
    def programar(self):
        print ("trabalhando...")
    @abstractmethod
    def dirigir(self):
        pass
    


class Motorista(Trabalhavel, Dirigivel):
    @abstractmethod
    def trabalhar(self):
        pass
    @abstractmethod
    def programar(self):
        pass
    @abstractmethod
    def dirigir(self):
        pass
    