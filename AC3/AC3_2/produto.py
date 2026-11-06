class Produto:

    def __init__(self, nome: str, preco: float, quantidade: int):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self) -> str:
        return self.__nome

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    def calcular_subtotal(self) -> float:
        return self.__preco * self.__quantidade
