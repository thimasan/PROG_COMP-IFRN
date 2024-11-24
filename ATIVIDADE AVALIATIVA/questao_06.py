#               AQUISIÇÃO DE DADOS

strSexo = input('Informe seu Sexo (Masculino/Feminino):')
while strSexo.lower() not in ["masculino","feminino"]:  
    print('Sexo inválido! Use Masculino ou Feminino!')
    strSexo = input('Informe seu Sexo (Masculino/Feminino):')

data_nascimento = input('Informe sua data de nascimento (DD/MM/AAAA):')
data_inic_contrib = input('Informe sua data de INICIO da contribuição Previdenciaria (DD/MM/AAAA):')


#calculo_idade





#calculo_tempo_contribuicao


teste



#               PROCESSAMENTO
if strSexo == 'masculino':
    if idade >= 65 and tempo_contribuicao >= 35:
        print('Você já pode se aposentar!')
    else:
        print('Você ainda não pode se aposentar!')
else:    
    if idade >= 62 and tempo_contribuicao >= 30:
        print('Você já pode se aposentar!')
    else:
        print('Você ainda não pode se aposentar!')