numero = int(input("Digite um número inteiro: "))
fatorial = 1
print(f"O fatorial de {numero} é: ", end='')
while numero >1:
    fatorial*=numero
    numero-=1
print(fatorial)