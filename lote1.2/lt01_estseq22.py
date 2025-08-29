#Receba dois valores, mostre seus valores em ordem crescente

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor2>valor1:
    print(f"Os valores em ordem crescente ficam: {valor1}, {valor2}")
else:
    print(f"Os valores em ordem crescente ficam: {valor2}, {valor1}")
