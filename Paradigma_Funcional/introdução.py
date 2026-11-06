numeros = [1, 2, 3, 4, 5, 6]
dobrados =[]

#Exemplo sem função 
for item in numeros:
    dobrados.append(item*2)
print (dobrados)

#Isso é praticamente o que o for está fazendo, mas desta vez utilizando apenas funções
dobrados = list(map(lambda n:n*2, numeros))
print(dobrados)

#Função pura, quando todas as minhas variaveis necessarias para a função ja estão na função
def calcular_desconto (valor, percentual):
    return valor * (percentual /100)
print (calcular_desconto(220, 10))

#Função impura, quando eu tenho uma ou mais variaveis necessarias para a função que não se encontram nela
desconto = 10
def calcular_desconto2(valor):
    return valor*(desconto/100)


#Função de alta ordem
#funções como valores
#funções com retorno
def saudacao(nome):
    return f"Ola, {nome}!"

mensagem =saudacao
print(mensagem("Maria"))

#função de alta ordem 2
def calcular (a, b, operacao):
    return operacao(a,b)
def somar(a, b):
    return a+b
def multiplicar (a, b):
    return a*b
print(calcular(10,5,somar))
print(calcular(10,5, multiplicar))

#Expressao LAMBDA
def qd(numero):
    return numero*2

print("Sem lambda: ", qd(5))
quadrado = lambda numero : numero **2
print(f"Com lambda: {quadrado(5)}")

#Uso mais interessante
def executar_operacao(a, b, operacao):
    return operacao(a,b)

resultado=executar_operacao(10,5,lambda x, y: x-y)

print(resultado)