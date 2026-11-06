'''
1.S - Single Responsability principle
ou Principio de responsabilidade unica
'''

'''Nossa primeira classe, com 3 metodos. Agora, qual a responsabilidade
da classe aluno?
São os nossos metodos: calcular media, salvar aluno e enviar email
Se cada classe só pode ter uma responsabilidade, pq a classe aluno esta
quebrando o primeiro principio?(SRP)
pois ele tem 3 metodos
O metodo não precisa ser obrigatorio ou sempre dessa maneira
Ele verifica se esses metodos não podem ir para uma outra classe
Servindo como metodo apenas daquela classe'''
class Aluno:
    def __init__(self, nome, nota):
        self.nome=nome
        self.nota=nota
'''
    def calcular_media (self):
        #print("Calcular media do aluno")

    def salvar_aluno(self):
        #print("Salvando aluno")
    
    def enviar_email(self):
        print("Enviando e-mail...")'''
    
'''Agora, o metodo(responsabilidade) calcular foi tirada do aluno para ter uma propria
classe especifica, eu apenas vinculo as duas classes'''
class CalcularMedia:
    def calcular (self,aluno):
        return aluno.nota

'''Tiramos outra responsabilidade da classe aluno, dando uma classe propria a ela''' 
class AlunoRepository:
    def salvar(self, aluno):
        print(f"Salvando {aluno.nome}...")

class EmailService:
    def enviar(self, aluno):
        print(f"Enviando e-mail para {aluno.nome}")


'''
Quem recebe o sparametro é apenas o aluno, pois ele é o unico que tem um construtor
'''
aluno=Aluno("Joao", 7.5)
media=CalcularMedia()
db = AlunoRepository()
email=EmailService()

'''
Isso é um print pois meu metodo calcular noa tem print, ele apenas retorna o aluno
para que consigamos ver isso, precisamos colocar um print a mao
'''
print(f"A media do aluno joao é: {media.calcular(aluno)}")

'''
Apenas quando eu chamo os metodos que eu passo o parametro
que é o aluno, a unica classe que tem um contrutor e consegue receber e guardar informações
'''
media.calcular(aluno)
db.salvar(aluno)
email.enviar(aluno)