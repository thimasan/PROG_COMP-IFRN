#AQUISIÇÃO DE DADOS E VALIDAÇÃO SIMULTÂNEA - CHECK-IN
print('#' * 100)
print(' ' * 30, 'CHECK - IN', ' '*50)
print(' ' * 30, 'INFORMAR AS HORAS NO PADRÃO 24 HORAS', ' '*50)
print('#' * 100)
intDia_Entrada = int(input('Digite o dia de Entrada:'))
while intDia_Entrada > 31:
    print("O dia de Entrada não pode ser superior a 31!")
    intDia_Entrada = int(input('Digite o dia de Entrada:'))

intMes_Entrada = int(input('Digite o mês de Entrada:'))
while intMes_Entrada > 12:
    print('O mês de Entrada não pode ser suerior a 12!')
    intMes_Entrada = int(input('Digite o mês de Entrada:'))

intAno_Entrada = int(input('Digite o Ano de Entrada:'))

intHora_Entrada   = int(input('Digite a Hora de Entrada:'))
while intHora_Entrada > 24:
    print('A Hora de Entrada não pode ser superior a 24!')
    intHora_Entrada = int(input('Digite a Hora de Entrada:'))

intMinuto_Entrada   = int(input('Digite o Minuto de Entrada:'))
while intMinuto_Entrada > 59:
    print('O Minuto de Entrada não pode ser superior a 59!')
    intMinuto_Entrada   = int(input('Digite o Minuto de Entrada:'))

print('*'*100)

#AQUISIÇÃO DE DADOS E VALIDAÇÃO SIMULTÂNEA - CHECK-OUT

print('#'*100)
print(' '*30, 'CHECK - OUT', ' '*50)
print('#'*100)
intDia_Saida = int(input('Digite o dia de Saída:'))
while intDia_Saida > 31:
    print("O dia de Saída não pode ser superior a 31!")
    intDia_Saida = int(input('Digite o dia de Saída:'))

intMes_Saida = int(input('Digite o mês de Saída:'))
while intMes_Saida > 12:
    print('O mês de Saída não pode ser suerior a 12!')
    intMes_Saida = int(input('Digite o mês de Saída:'))

intAno_Saida = int(input('Digite o Ano de Saída:'))

intHora_Saida   = int(input('Digite a Hora de Saída:'))
while intHora_Saida > 24:
    print('A Hora de Saída não pode ser superior a 24!')
    intHora_Saida = int(input('Digite a Hora de Saída:'))

intMinuto_Saida   = int(input('Digite o Minuto de Saída:'))
while intMinuto_Saida > 59:
    print('O Minuto de Saída não pode ser superior a 59!')
    intMinuto_Saida   = int(input('Digite o Minuto de Saída:'))

print('*'*100)

##############################################################################################################################################################################
#                                   VALIDAÇÕES LÓGICAS

#VALIDAÇÃO DO ANO
while intAno_Entrada > intAno_Saida:
    print('O Ano de Entrada não pode ser maior que o Ano de Saída!')
    intAno_Entrada = int(input('Digite o Ano de Entrada:'))
    intAno_Saida   = int(input('Digite o Ano de Saída:'))

#VALIDAÇÃO DOS MESES
while intMes_Entrada > intMes_Saida and intAno_Entrada == intAno_Saida:
    print('O Mês de Entrada não pode ser maior que o Mês de Saída!')
    intMes_Entrada = int(input('Digite o Mês de Entrada:'))
    intMes_Saida   = int(input('Digite o Mês de Saída:'))
################################################################################################################################################################################
#                               CÁLCULO DA DIFERENÇA DE HORAS PARA MESMO DIA, MÊS E ANO
if intDia_Entrada == intDia_Saida and intMes_Entrada == intMes_Saida and intAno_Entrada == intAno_Saida:
    intMinutos_Total = ((intHora_Saida - intHora_Entrada)*60 ) + (intMinuto_Saida - intMinuto_Entrada)
    
    if intMinutos_Total <= 120:
        fltCusto_Total = (intMinutos_Total / 60) * 8.0
        print(f'O valor a ser pago é de R${fltCusto_Total}')
    elif 120 < intMinutos_Total <= 240:
        fltHoras_Total = intMinutos_Total / 60
        fltCusto_Total = (2 * 8.0) + ((fltHoras_Total - 2) * 5.0)
        print(f'O valor a ser pago é de R${fltCusto_Total}')
    elif intMinutos_Total <= 720:
        fltHoras_Total = intMinutos_Total / 60
        fltCusto_Total = (2 * 8.0) + (2 * 5.0) + ((fltHoras_Total - 4) * 3.0)
        print(f'O valor a ser pago é de R${fltCusto_Total}')
    else :
        print("Custo fixo de R$ 30,00 para o restante do dia!")
else:
    
    intDif_Ano = (intAno_Saida - intAno_Entrada) * 365
    
    if intMes_Entrada <= 2:
        if intMes_Entrada == intMes_Saida:
            intDif_Dias = intDia_Saida - intDia_Entrada
        elif intDia_Entrada > intDia_Saida:
            diferenca_mes = (intMes_Saida - intMes_Entrada) * 30
            intDif_Dias = diferenca_mes - ((30 - intDia_Entrada) + intDia_Saida) - 2
        else:
            diferenca_mes = (intMes_Saida - intMes_Entrada) * 30
            intDif_Dias = diferenca_mes + (intDia_Saida - intDia_Entrada) 
    else:
        if intMes_Entrada == intMes_Saida:
            diferenca_dias = intDia_Saida - intDia_Entrada
            intDif_Dias = diferenca_dias
        elif intDia_Entrada > intDia_Saida:
            diferenca_mes = (intMes_Saida - intMes_Entrada) * 30
            intDif_Dias = diferenca_mes - ((30 - intDia_Entrada) + intDia_Saida) -1
        else:
            diferenca_mes = (intMes_Saida - intMes_Entrada) * 30
            intDif_Dias = diferenca_mes + (intDia_Saida - intDia_Entrada) + 1
    
    intDias_Total = intDif_Ano + intDif_Dias
    fltCusto_Total = intDias_Total * 30.0
    print(f'O custo total do Estacionamento (R$ 30 / dia) foi de R${fltCusto_Total}!')
    print('Não se preocupe podemos NEGOCIAR!')
    print('#' * 100)