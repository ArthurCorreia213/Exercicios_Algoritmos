#Receba os coeficientes A,B,C de uma equação de segundo grau, calcula a raiz e mostre-a
#Arthur Correia

A = int(input("Digite o valor do coeficiente A: "))

B = int(input("Digite o valor do coeficiente B: "))

C = int(input("Digite o valor do coeficiente C: "))

delta = (B**2)-((4*A)*C)

if delta == 0:
    raiz = -B/(2*A)
    print(f"A raiz real dos coeficientes digitados é {raiz}")
elif delta<0:
    print(f"Delta resultou em {delta}, deltas negativos não possuem raizes reais")
else:
    x1 = (B+(delta**0.5))/2*A
    x2 = (B-(delta**0.5))/2*A
    print(f"Os coeficientes digitados produzem as raízes reais x1={x1}, e x2={x2}")