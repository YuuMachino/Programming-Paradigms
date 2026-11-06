#criar um programa para cadastrar voluntarios de um campanha social.
#cada voluntario possui nome, idade e quantidade de horas de trabalho

nome=input("Ditige o nome do voluntario: ")
idade=int(input("Digite a idade do voluntario: "))
horas=float(input("Digite a quantidade de horas trabalhadas: "))

print("Parabens! Cadastro realizado com sucesso!",)
print("Nome: ", nome)
print("Idade: ", idade)
print("Horas trabalhadas: ", horas)

#Lista para agrupar os nomes dos voluntarios

nomes= ["Ana", "Carla", "Bruna"]
idades = [22, 24, 25]
horarios = [10,5, 16]

#Para mostrarmos o que queremos da lista, podemos usar os indeces de cada lista, como por exemplo print(nome[0])
#Que mostrara o nome "Ana"