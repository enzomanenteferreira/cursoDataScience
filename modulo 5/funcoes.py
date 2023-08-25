def primeiraFunc():
    print("hello world")

primeiraFunc()

#definindo funcao com parametro
def segundaFunc(nome):
    print('Hello  %s' %(nome))

segundaFunc('aluno')

#funcao para somar numeros
def addNum(firstnum, secondnum):
    print("Primeiro Numero: " + str(firstnum))
    print("Segundo numero: " +str(secondnum))
    print("Soma: ", firstnum + secondnum)

#chamando a funcao e passando parametros
addNum(20,30)
addNum(50,100)

#funcoes com numero variavel de argumentos
def printVarInfo(arg1, *vartuple):

    #imprimindo o valor do primeiro argumento
    print("O parametro passado foi: ", arg1)

    #imprimindo o valor do segundo argumento
    for item in vartuple:
        print("O parametro passado foi: ", item)
    return 

printVarInfo('Teste1','Teste2')