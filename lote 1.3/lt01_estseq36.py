def fatorial(num):
    resultado = 1
    while num >1:
        resultado*=num
        num-=1
    return resultado

resultado = 1
num = int(input("Digite um número: "))
for i in range(1,num+1):
    resultado += 1/fatorial(i)

print(resultado)