"""
POR QUE Pinguim VIOLA O LSP?
-------------------------------
Liskov Substitution Principle: se B herda de A, deve ser possível usar B no
lugar de A sem quebrar o programa. 

A raiz do erro é de modelagem: "voar" não é característica de TODAS as aves,
então não deveria estar na classe base.

"""

from abc import ABC, abstractmethod


class Ave(ABC):

    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")


class AveVoadora(Ave):

    @abstractmethod
    def voar(self):
        ...


class AveNaoVoadora(Ave):

    @abstractmethod
    def locomover(self):
        ...


class Aguia(AveVoadora):
    def voar(self):
        print("A águia está voando.")


class Pardal(AveVoadora):
    def voar(self):
        print("O pardal está voando.")


class Pinguim(AveNaoVoadora):
    def locomover(self):
        print("O pinguim está nadando/caminhando.")

    def nadar(self):
        print("O pinguim está nadando.")


def fazer_voar(aves: list[AveVoadora]):
    for ave in aves:
        ave.voar()


def main():
    voadoras = [Aguia("Águia"), Pardal("Pardal")]
    fazer_voar(voadoras)

    pinguim = Pinguim("Pinguim")
    pinguim.nadar()
    todas = voadoras + [pinguim]
    for ave in todas:
        ave.comer()


if __name__ == "__main__":
    main()
