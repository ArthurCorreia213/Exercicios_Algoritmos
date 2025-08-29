#Receba as 4 notas de um aluno, calcule sua média e exiba mensagens de acordo com o resultado

nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))
nota3= float(input("Digite a terceira nota: "))
nota4= float(input("Digite a quarta nota: "))

media = (nota1+nota2+nota3+nota4)/4

if media >=6:
    print("Aprovado")
elif media >=3:
    print("Exame")
else:
    print("Retido")