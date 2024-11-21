'''O número de dias decorridos entre duas datas é importante em uma infinidade de situações da vida cotidiana.
Faça um programa que recebe inicialmente dois valores (dia inicial e mês inicial), depois mais dois valores (dia final, mês final),
ao final deve indicar quantos dias se passaram entre as datas (considere que o ano não é bissexto). 
Exemplos:  o 02 de 05 até 03 de 05 - 1 dia o 27 de 04 até 03 de 05 - 6 dias o 03 de 02 até 03 de 05 - 79 dias 
Não esqueça de verificar se a data inicial é menor ou igual à data final. 
Dica: conte o número de dias até cada uma das datas e subtraia esses números.
'''
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