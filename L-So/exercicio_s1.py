class Funcionario:
    def __init__(self, nome, salario):
        self.nome=nome
        self.salario=salario

    def calcular_salario(self):
        print("Calculando salario...")
    
    def salvar_banco(self):
        print(f"Salvando funcionario {self.nome}")

    def enviar_email(self):
        print(f"Enviando email para {self.nome}")


class CalcularSalario:
    def calcular (self,funcionario):
        print(f"Calculando o salario do funcionario {funcionario.nome}")

class FuncionarioRep:
    def salvar(self, funcionario):
        print(f"Salvando {funcionario.nome}...")

class EmailService:
    def enviar(self, funcionario):
        print(f"Enviando e-mail para {funcionario.nome}")


funcionario=Funcionario("Fulano", 2000)
calculo=CalcularSalario()
db = FuncionarioRep()
email=EmailService()

calculo.calcular(funcionario)
db.salvar(funcionario)
email.enviar(funcionario)