num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

resultado = 0

if num1>num2:
    for i in range(num2,num1+1):
        if i % 2 != 0:
            resultado+=i
else :
    for i in range(num1,num2+1):
        if i % 2 != 0:
            resultado+=i
print(resultado)