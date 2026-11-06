from abc import ABC, abstractmethod


class Frete(ABC):

    @abstractmethod
    def calcular(self, valor):
        ...


class FreteNormal(Frete):
    def calcular(self, valor):
        return valor * 0.05


class FreteExpresso(Frete):
    def calcular(self, valor):
        return valor * 0.10


class FreteSedex(Frete):
    def calcular(self, valor):
        return valor * 0.15


def calcular_frete(frete, valor):
    return frete.calcular(valor)


class FreteInternacional(Frete):
    def calcular(self, valor):
        return valor * 0.20


def main():
    frete = FreteExpresso()
    valor_frete = calcular_frete(frete, 1000)
    print(valor_frete)  # 100.0

    for f in (FreteNormal(), FreteExpresso(), FreteSedex(), FreteInternacional()):
        print(f"{type(f).__name__}: R$ {calcular_frete(f, 1000):.2f}")


if __name__ == "__main__":
    main()
