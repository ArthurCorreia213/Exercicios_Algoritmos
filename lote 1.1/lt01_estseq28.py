# Receba o preço atual e a média mensal de um produto. Calcule e mostre o 
# novo preço sabendo que: 
# Venda Mensal            Preço Atual         Preço       Novo 
# < 500                   < 30                +           10% 
# >= 500 e < 1000         >= 30 e < 80        +           15% 
# >= 1000                 >= 80               -           5%

# Obs.: para outras condições, preço novo será igual ao preço atual. 

#Arthur Correia

venda_mensal = int(input("Digite a média de venda mensal do produto: "))
preco_atual = float(input("Digite o valor do produto: "))
