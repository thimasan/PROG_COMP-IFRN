nome    = input('Informe o nome:')
etapa_1 = input('Informe a nota da etapa 1:')
etapa_2 = input('Informe a nota da etapa 2:')

media = (int(etapa_1) * 2 + int(etapa_2) * 3) / 5
print(f'{nome} obteve N1 = {etapa_1} e N2 = {etapa_2} e obteve média = {media}')