'''
   EXEMPLO 04:
   Fazer um programa em que o usuário informe uma palavra e em seguida
   o programa exiba a palavra invertida e diga se ela é um palíndromo ou não.
'''

palavra = str(input("Digite uma palavra para verificar se é palíndromo:"))
palindromo = ''
for i in range(len(palavra)-1, -1, -1):
    palindromo += palavra[i]

if palavra.lower() == palindromo.lower():
    print('É palindromo')
else:
    print('Não é palindromo')