#                       DIAS TRANSCORRIDOS
#---------------------------------------------------------------------------------------------------
print('*'*60)
# ENTRADA DOS DADOS E VALIDAÇÃO SIMULTÂNEA A CADA ENTRADA:

Dia_Inicial = int(input('Digite o dia inicial:'))
while Dia_Inicial > 31:
    print("O dia Inicial não pode ser superior a 31!")
    Dia_Inicial = int(input('Digite o dia inicial:'))

Mes_Inicial = int(input('Digite o mês inicial:'))
while Mes_Inicial > 12:
    print('O mês Inicial não pode ser suerior a 12!')
    Mes_Inicial = int(input('Digite o mês Inicial:'))

Dia_Final   = int(input('Digite o dia Final:'))
while Dia_Final > 31:
    print('O dia Final não pode ser superior a 31!')
    Dia_Final = int(input('Digite o dia final:'))

Mes_Final   = int(input('Digite o mês Final:'))
while Mes_Final > 12:
    print('O mês Final não pode ser superior a 12!')
    Mes_Final   = int(input('Digite o mês Final:'))
    
    
#Validação do Mês
while Mes_Final < Mes_Inicial:
    print('O mês Inicial não pode ser maior que o mês final!')
    Mes_Inicial = int(input('Digite o mês inicial:'))
    Mes_Final   = int(input('Digite o mês Final:'))

# Validação do dia para o mesmo mês:
while Mes_Inicial == Mes_Final and Dia_Final < Dia_Inicial:
    print('Para datas do mesmo mês, o dia Inicial não pode ser maior que o dia Final:')
    Dia_Inicial = int(input('Digite o dia inicial:'))
    Dia_Final   = int(input('Digite o dia Final:'))

# Cálculo dos Dias Transcorridos

if Mes_Inicial <= 2:
    if Mes_Inicial == Mes_Final:
        diferenca_dias = Dia_Final - Dia_Inicial
        print(f'Se passaram {diferenca_dias} dias!')
    elif Dia_Inicial > Dia_Final:
        diferenca_mes = (Mes_Final - Mes_Inicial) * 30
        dias_total = diferenca_mes - ((30 - Dia_Inicial) + Dia_Final) - 2
        print(f'Se passaram {dias_total} dias!')
    else:
        diferenca_mes = (Mes_Final - Mes_Inicial) * 30
        dias_total = diferenca_mes + (Dia_Final - Dia_Inicial) 
        print(f'Se passaram {dias_total} dias!')
else:
    if Mes_Inicial == Mes_Final:
        diferenca_dias = Dia_Final - Dia_Inicial
        print(f'Se passaram {diferenca_dias} dias!')
    elif Dia_Inicial > Dia_Final:
        diferenca_mes = (Mes_Final - Mes_Inicial) * 30
        dias_total = diferenca_mes - ((30 - Dia_Inicial) + Dia_Final) -1
        print(f'Se passaram {dias_total} dias!')
    else:
        diferenca_mes = (Mes_Final - Mes_Inicial) * 30
        dias_total = diferenca_mes + (Dia_Final - Dia_Inicial) + 1
        print(f'Se passaram {dias_total} dias!')
        
print('*'*60)