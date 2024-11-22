#               AQUISIÇÃO DE DADOS

strSexo = input('Informe seu Sexo: (Masculino/Feminino)')
while strSexo != 'masculino' or strSexo != 'feminino':
    print('Sexo inválido! Use Masculino ou Feminino.')
    strSexo = input('Informe seu Sexo: (Masculino/Feminino)')

data_nascimento = input('Informe sua data de nascimento (DD/MM/AAAA):')
data_inic_contrib = input('Informe sua data de INICIO da contribuição Previdenciaria (DD/MM/AAAA):')