'''
   EXEMPLO 01:
   Fazer um programa em que o usuário informe uma frase e depois exiba qual
   a palavra mais longa da frase. 
'''
# Solicita ao usuário que informe uma string
frase = input('Informe uma string: ')

# Separa a string em palavras
palavras = frase.split()

# Inicializa a variável que irá armazenar a maior palavra
maior_palavra = ''

# Percorre todas as palavras da lista
for palavra in palavras:
    # Verifica se a palavra atual é maior que a palavra armazenada
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra

# Exibe a maior palavra
print('A maior palavra é:', maior_palavra)
