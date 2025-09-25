#Receba os valores de hora e minuto inicial, hora e minuto final. Calcule a duração da partida e os exiba.
#Partida deve ter menos que 24 horas obrigatoriamente
#Pode começar num dia e terminar em outro
#Arthur Correia

hora_inicio = int(input("Digite a hora inicial da partida: "))
minuto_inicio = int(input("Digite o minuto inicial da partida: "))

hora_fim = int(input("Digite a hora do fim da partida: "))
minuto_fim = int(input("Digite o minuto final da partida: "))

duracao_hora = 0
duracao_minutos = 0

if minuto_fim>=minuto_inicio:
    duracao_minutos = minuto_fim-minuto_inicio
else:
    duracao_hora -=1
    duracao_minutos = minuto_inicio-minuto_fim

if hora_fim>hora_inicio:
    duracao_hora += hora_fim-hora_inicio
else:
    duracao_hora += (hora_fim+24)-hora_inicio

print(f"O jogo teve a duração de {duracao_hora} horas e {duracao_minutos} minutos")