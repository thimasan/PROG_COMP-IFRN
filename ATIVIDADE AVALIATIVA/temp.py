# Coletando dados de entrada
hora_inicio = int(input("Hora de início (HH): "))
minuto_inicio = int(input("Minuto de início (MM): "))
hora_fim = int(input("Hora de chegada (HH): "))
minuto_fim = int(input("Minuto de chegada (MM): "))
segundos_parados = int(input("Tempo parado para descanso (em segundos): "))
litros_gastos = float(input("Quantidade de combustível gasto (em litros): "))
preco_por_litro = float(input("Preço do litro de combustível (em R$): "))
distancia_percorrida = float(input("Distância percorrida (em Km): "))

# Convertendo os horários para segundos desde o início do dia
inicio_segundos = hora_inicio * 3600 + minuto_inicio * 60
fim_segundos = hora_fim * 3600 + minuto_fim * 60

# Calculando o tempo total de viagem em segundos
tempo_total_viagem = fim_segundos - inicio_segundos

# Calculando o tempo em movimento (tempo total - tempo parado)
tempo_movimento = tempo_total_viagem - segundos_parados

# Calculando a velocidade média global (Km/h)
# tempo_total_viagem em horas
tempo_total_viagem_horas = tempo_total_viagem / 3600
velocidade_media_global = distancia_percorrida / tempo_total_viagem_horas

# Calculando a velocidade média em movimento (Km/h)
# tempo_movimento em horas
tempo_movimento_horas = tempo_movimento / 3600
velocidade_media_movimento = distancia_percorrida / tempo_movimento_horas

# Calculando o custo da viagem com combustível
custo_total_combustivel = litros_gastos * preco_por_litro

# Calculando o desempenho do carro
consumo_medio_km_por_litro = distancia_percorrida / litros_gastos
consumo_litros_por_hora = litros_gastos / tempo_movimento_horas
custo_por_km = custo_total_combustivel / distancia_percorrida

# Exibindo os resultados
print("\n--- Detalhes da Viagem ---")
print(f"a) Tempo total de viagem: {tempo_total_viagem} segundos")
print(f"b) Velocidade média global: {velocidade_media_global:.2f} Km/h")
print(f"   Velocidade média em movimento: {velocidade_media_movimento:.2f} Km/h")
print(f"c) Custo total da viagem: R$ {custo_total_combustivel:.2f}")
print(f"d) Desempenho do carro:")
print(f"   - Consumo médio: {consumo_medio_km_por_litro:.2f} Km/l")
print(f"   - Consumo em movimento: {consumo_litros_por_hora:.2f} l/h")
print(f"   - Custo por Km: R$ {custo_por_km:.2f} por Km")
