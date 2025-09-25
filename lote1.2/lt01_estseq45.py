# Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225 
#Arthur Correia

resultado = 0
for numero in range(1, 16):
    termo = numero / (numero ** 2)
    if numero % 2 == 0:
        termo = -termo
    resultado += termo

print(resultado)
