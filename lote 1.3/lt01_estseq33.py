numero = int(input("Digite um número inteiro: "))
resultado = 1
for i in range(1,numero+1):
    resultado/=1/i
    print(resultado)
print(resultado)