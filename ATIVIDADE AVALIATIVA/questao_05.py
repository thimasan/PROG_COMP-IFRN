#AQUISIÇÃO DE DADOS E VALIDAÇÃO SIMULTÂNEA - CHECK-IN
print('#'*100)
print(' '*30, 'CHECK - IN', ' '*50)
print('#'*100)
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
    intHora_Saída = int(input('Digite a Hora de Saída:'))

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

