print("*****Python Calculator*****")

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

def mult(x,y):
    return x*y

print("\nselecione o numero desejado: \n")
print("1 - Soma")
print("2 - subtração")
print("3 - divisão")
print("4 - multiplicação")

escolha = input("digite a sua opção(1-2-3-4): ")
num1 = int(input("\nDigite o primeiro numero: "))
num2 = int(input("\nDigite o segundo numero: "))

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1,num2))

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", sub(num1,num2))

elif escolha == '3':
    print("\n")
    print(num1, "/", num2, "=", div(num1,num2))

elif escolha == '4':
    print("\n")
    print(num1, "*", num2, "=", mult(num1,num2))

