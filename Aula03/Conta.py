class ContaBancaria:
    def __init__(self, valor):
        self.__valor=valor
        #Esse __ antes do valor é como se estivessemos encapsulando a variavel 
    #Aqui ele esta sendo utilizado como get
    @porperty
    def valor(self):
        return self.__valor
    
    #aqui ele esta sendo utilizado como set
    @valor.setter
    def valor(self, dinheiro):
        if dinheiro >0:
            self.__valor+=dinheiro
        else:
            self.__valor
    
    ###Geralmente não usamos o get e set no python, pode ser usado, mas não muito recomendado, em vez disso usamos
    ###porperty (decorator)
    #def getValor(self):
    #    return self.__valor
    #def detvalor(self, dinheiro):
    #    self.__valor+=dinheiro

#cb1=ContaBancaria(1000)
#print(cb1.getValor())
#cb1.setValor(10000)
#print(cb1.getValor())

cb1=ContaBancaria(1000)
print(cb1.valor)
cb1.valor=10000
print(cb1.valor)

##Tenho uma conta bancaria com mil pila
#cb1=ContaBancaria(1000)
##Aqui esta tentando modificar a variavel mudando para 10 mil
#cb1.__valor=10000
#print(cb1.__valor)
##Obvamente isso vai dar erro pois a variavel está encapsulada, ou seja, inacessivel, escondida.

