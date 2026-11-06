from functools import reduce
vendas=[50,150,200,80,300]
valores=list(vendas)
print(valores)
filtrados=filter(
    lambda valor:valor>100,
    vendas
)
print(filtrados)

com_taxa=map(
    lambda valor : valor *1.05,
    filtrados
)
print(com_taxa)

total = reduce(
    lambda acumulador, valor:acumulador+valor,
    com_taxa,
    0
)

print(total)