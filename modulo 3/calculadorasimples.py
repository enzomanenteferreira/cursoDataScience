num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

op = input("digite a operacao de calculo (+, -, *, /): ")

if(op == "+"):
   result = num1+num2
   print("resultado = ", result)

elif(op == "-"):
   result = num1-num2
   print("resultado = ", result)

elif(op == "*"):
   result = num1*num2
   print("resultado = ", result)

elif(op == "/"):
   result = num1/num2
   print("resultado = ", result)