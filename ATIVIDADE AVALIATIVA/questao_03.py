#************************************************************************************************************
#                   AQUISIÇÃO DE DADOS

hora_inicial   = int(input("Digite a hora INICIAL da viagem:"))
minuto_inicial = int(input("Digite os minutos INICIAIS da viagem:"))
hora_final     = int(input("Digite a hora FINAL da viagem:"))
minuto_final   = int(input("Digite os minutos FINAIS da viagem:"))
seg_descanso   = int(input("Digite quantos SEGUNDOS ficou parado para descanso:"))
qtd_combustivel = float(input("Digite o total de combustível usado na viagem Em litros):"))
preco_combustivel = float(input("Digite o valor do combustível no dia da viagem (Em Reais):"))
distancia_total = float(input("Digite o total de kilometros da viagem:"))

#************************************************************************************************************
#                   CONVERSÃO DE MEDIDAS E CÁLCULOS

# CONVERSÃO DO TEMPO PARA SEGUNDOS

segundos_inicial = hora_inicial * 3600 + minuto_inicial * 60
segundos_final = hora_final * 3600 + minuto_final * 60

# TEMPO TOTAL DA VIAGEM

tempo_total_segundos = segundos_final - segundos_inicial

# VELOCIDADE MÉDIA GLOBAL

tempo_total_horas = tempo_total_segundos / 3600
velocidade_media_global = distancia_total / tempo_total_horas

#VELOCIDADE MÉDIA EM MOVIMENTO

tempo_total_movimento = (tempo_total_segundos - seg_descanso) / 3600
velocidade_media_movimento = distancia_total / tempo_total_movimento

# GASTOS COM COMBUSTÍVEL

gasto_total = qtd_combustivel * preco_combustivel

#*************************************************************************************************************
#                           CÁLCULO DOS DESEMPENHOS
# DESEMPENHO EM KM / L
kilometro_litro = distancia_total / qtd_combustivel
# DESEMPENHO EM LITROS POR HORA
litros_hora = qtd_combustivel / tempo_total_movimento
# CUSTOS POR KILOMETRO PERCORRIDO
reais_kilometro = preco_combustivel / distancia_total

#***********************************************************************************************************
#                           IMPRESSÃO DAS INFORMAÇÕES

print(f'O tempo total da viagem foi de {tempo_total_segundos} segundos.')
print(f'A velocidade média global foi de {velocidade_media_global} Km/h.')
print(f'A velocidade média em movimento foi de {velocidade_media_movimento} Km/h.')
print(f'O custo total com a viagem foi de R${gasto_total: .2f}.')
print(f'O desempenho do carro na viagem foi de{kilometro_litro: .1f} Km/l.')
print(f'O consumo de combustível por hora foi de{litros_hora: .2f} l/h.')
print(f'O valor gasto por kilometro foi de R${reais_kilometro: .4f}')