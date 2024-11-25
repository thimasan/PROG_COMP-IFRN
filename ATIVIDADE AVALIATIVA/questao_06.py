from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
#               AQUISIÇÃO DE DADOS

strSexo = input('Informe seu Sexo (Masculino/Feminino):')
while strSexo.lower() not in ["masculino","feminino"]:  
    print('Sexo inválido! Use Masculino ou Feminino!')
    strSexo = input('Informe seu Sexo (Masculino/Feminino):')

data_nascimento = input('Informe sua data de nascimento (DD/MM/AAAA):')

data_inic_contrib = input('Informe sua data de INICIO da contribuição Previdenciaria (DD/MM/AAAA):')


# CALCULO DA IDADE
data_nascimento = parse(data_nascimento)
data_atual = datetime.now()
idade = relativedelta(data_atual, data_nascimento).years

# IDADE DE TRABALHO
data_nascimento = parse(data_nascimento)
data_inic_contrib = parse(data_inic_contrib)
idade_trabalho = relativedelta(data_inic_contrib, data_nascimento).years

if idade_trabalho < 18:
    print('Você não pode contribuir com a previdência com menos de 18 anos!')
    print(f'Você tem {idade_trabalho} anos de idade!')

# CALCULO TEMPO DE CONTRIBUIÇÃO
data_inic_contrib = parse(data_inic_contrib)
data_atual = datetime.now()
tempo_contribuicao = relativedelta(data_atual, data_inic_contrib).years


# APÓS A PROVA SER AVALIADA, REFAZER AS CONDIÇÕES ABAIXO TRANSFORMANDO EM FUNÇÕES! PARA EVITAR A REPETIÇÃO DA RESPOSTA AO USUÁRIO!
# E SOMENTE ENTRAR NA SEGUNDA CONDIÇÃO SE A PRIMEIRA FOR FALSA!

#   APOSENTADORIA POR IDADE

if strSexo == 'masculino':
    if idade >= 65 and tempo_contribuicao >= 15:
        print('Você já pode se aposentar!')
    else:
        print('Você ainda não pode se aposentar!')
else:    
    if idade >= 62 and tempo_contribuicao >= 15:
        print('Você já pode se aposentar!')
    else:
        print('Você ainda não pode se aposentar!')
        print(f'Você tem {idade} anos de idade!')

# APOSENTADORIA POR TEMPO DE CONTRIBUIÇÃO
if strSexo == 'masculino':
    if tempo_contribuicao >= 35:
        print('Você já pode se aposentar por tempo de contribuição!')
    else:
        print('Você ainda não pode se aposentar por tempo de contribuição!')
else:    
    if tempo_contribuicao >= 30:
        print('Você já pode se aposentar por tempo de contribuição!')
    else:
        print('Você ainda não pode se aposentar por tempo de contribuição!')