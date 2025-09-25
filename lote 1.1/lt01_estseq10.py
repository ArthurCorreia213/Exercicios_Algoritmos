#Receba 2 números reais. Calcule e mostre a diferença desses valores.
#Arthur Correia

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1>=numero2:
    print(f"A diferença entre {numero1} e {numero2} é {numero1-numero2}")
elif numero2>= numero1:
    print(f"A diferença entre {numero2} e {numero1} é {numero2-numero1}")