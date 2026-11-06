"""
POR QUE EXISTE VIOLAÇÃO DO LSP?
----------------------------------
Conta promete dois comportamentos: depositar() e sacar(). ContaInvestimento
herda a promessa de sacar(), mas a quebra com uma exceção. A função
    realizar_saque(conta, valor)
funciona com ContaCorrente e quebra com ContaInvestimento. Logo, a subclasse
não pode substituir a superclasse sem alterar o comportamento esperado.

"""

from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, saldo=0):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo


class ContaDepositavel(Conta):
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo.")
        self._saldo += valor


class ContaSacavel(ContaDepositavel):
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor


class ContaCorrente(ContaSacavel):
    pass


class ContaPoupanca(ContaSacavel):
    pass


class ContaInvestimento(ContaDepositavel):
    """Aceita depósito (aplicação), mas NÃO promete saque direto."""

    def aplicar_rendimento(self, taxa):
        self._saldo += self._saldo * taxa


def realizar_deposito(conta: ContaDepositavel, valor):
    conta.depositar(valor)
    print(f"Depósito de R$ {valor} realizado! Saldo: R$ {conta.saldo:.2f}")


def realizar_saque(conta: ContaSacavel, valor):
    conta.sacar(valor)
    print(f"Saque de R$ {valor} realizado! Saldo: R$ {conta.saldo:.2f}")


def main():
    contas_com_saque = [ContaCorrente(1000), ContaPoupanca(1000)]
    for conta in contas_com_saque:
        realizar_saque(conta, 200)

    investimento = ContaInvestimento(1000)
    for conta in [*contas_com_saque, investimento]:
        realizar_deposito(conta, 100)

    investimento.aplicar_rendimento(0.01)
    print(f"Saldo do investimento após rendimento: R$ {investimento.saldo:.2f}")


if __name__ == "__main__":
    main()
