ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

if ano_atual>ano_nascimento:
    print(f"Você completa {ano_atual-ano_nascimento} anos em {ano_atual} e terá {(ano_atual-ano_nascimento)+17} anos daqui a 17 anos")
else:
    print("Input inválido")