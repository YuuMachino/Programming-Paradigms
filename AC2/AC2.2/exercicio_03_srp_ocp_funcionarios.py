from abc import ABC, abstractmethod


class Funcionario(ABC):

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_bonus(self):
        ...


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20


class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05


class FuncionarioRepository:

    def salvar(self, funcionario):
        print(f"Salvando {funcionario.nome} no banco de dados...")


class RelatorioFuncionarios:

    def gerar(self, funcionarios):
        print("=== Relatório de Funcionários ===")
        for f in funcionarios:
            print(
                f"{f.nome:<8} | {type(f).__name__:<13} | "
                f"Salário: R$ {f.salario:>8.2f} | Bônus: R$ {f.calcular_bonus():>7.2f}"
            )

class Analista(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15


def main():
    funcionarios = [
        Desenvolvedor("Carlos", 5000),
        Gerente("Maria", 8000),
        Estagiario("João", 2000),
        Analista("Beatriz", 6000),  
    ]

    for funcionario in funcionarios:
        print(funcionario.calcular_bonus())

    print()
    repositorio = FuncionarioRepository()
    for funcionario in funcionarios:
        repositorio.salvar(funcionario)

    print()
    RelatorioFuncionarios().gerar(funcionarios)


if __name__ == "__main__":
    main()
