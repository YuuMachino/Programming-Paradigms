#MAP() praticamente é o nosso FOR
#map (funcao, iteravel)
precos=[100, 200, 300, 400]
def aplicar_aumento(preco):
    return preco * 1.10

novos_precos = list(map(lambda preco : preco *1.10, precos))

#FILTER()
produtos=[
    {"nome": "notebook", "Preço": 3500},
    {"nome": "mouse", "Preço": 80},
    {"nome": "teclado", "Preço": 150},
    {"nome": "monitor", "Preço": 900}
]

promocao=list(
    filter(
        lambda produto : produto["Preço"]<200,
        produtos
    )
)

print(promocao)

#REDUCE
from functools import reduce
valores=[100,200,50,150]
total=reduce(
    lambda acumulador, valor : acumulador + valor,
    valores, 
    0
)

print(total)