#encontrar numeros primos entre 2 e 30 usando loop for e while

primos = []

for num in range(2,31):

    eh_primo = True

i = 2
while i<=num // 2:
    if num % i == 0:
        eh_primo = False
        break
    i += 1

 #adicionando numero primo na lista
if eh_primo:
    primos.append(num)

print(primos)