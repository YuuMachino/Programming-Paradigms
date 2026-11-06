nome=(input("Informe o seu nome: "))
ali=int(input("Informe a quantidade de alimentos doados: "))
meta=int(input("Informe a meta: "))
print ("Foi doado", ali)

if ali >= meta:
    print ("Meta atingida")
else:
    print ("Falta:", (meta-ali))