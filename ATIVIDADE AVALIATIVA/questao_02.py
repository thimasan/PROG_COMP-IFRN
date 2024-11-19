import math
valor_saque = float(input("Informe o valor desejado para saque:"))

while valor_saque < 0 :
    valor_saque = float(input("Informe o valor desejado para saque:"))

# notas [100, 50, 20, 10, 5, 2]
# moedas [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

# notas 100
notas_100 = valor_saque // 100
resto_100 = valor_saque % 100

# notas 50
notas_50 = resto_100 // 50.0
resto_50 = resto_100 %  50.0

# notas 20
notas_20 = resto_50 // 20.0
resto_20 = resto_50 % 20.0

# notas 10
notas_10 = resto_20 // 10.0
resto_10 = resto_20 % 10.0

# notas 5
notas_5 = resto_10 // 5.0
resto_5 = resto_10 % 5.0

# notas 2
notas_2 = resto_5 // 2.0
resto_2 = resto_5 % 2.0

# moedas 1.0
moedas_1 = resto_2 // 1.0
resto_moedas_100 = resto_2 % 1.0

# moedas 0.50
moedas_050 = resto_moedas_100 // 0.50
resto_moedas_050 = resto_moedas_100 % 0.50

# moedas 0.25
moedas_025 = resto_moedas_050 // 0.25
resto_moedas_025 = resto_moedas_050 % 0.25

# moedas 0.10
moedas_010 = resto_moedas_025 // 0.10
resto_moedas_010 = resto_moedas_025 % 0.10

# moedas 0.05
moedas_005 = resto_moedas_010 // 0.05
resto_moedas_005 = round(resto_moedas_010 % 0.05,2)

# moedas 0.01
moedas_001 = resto_moedas_005 // 0.01
#moedas_corrigida = round(moedas_001,2)

print(f'Notas de R$ 100: {notas_100}')
print(f'Notas de R$ 50: {notas_50}')
print(f'Notas de R$ 20: {notas_20}')
print(f'Notas de R$ 10: {notas_10}')
print(f'Notas de R$ 5: {notas_5}')
print(f'Notas de R$ 2: {notas_2}')
print(f'Moedas de R$ 1.0: {moedas_1}')
print(f'Moedas de R$ 0.50: {moedas_050}')
print(f'Moedas de R$ 0.25: {moedas_025}')
print(f'Moedas de R$ 0.10: {moedas_010}')
print(f'Moedas de R$ 0.05: {moedas_005}')
print(f'Moedas de R$ 0.01: {moedas_001}')



#valores para teste
#5256.99 - erro
#576.99
#2048.09
#2048.19
#2048.29 - erro