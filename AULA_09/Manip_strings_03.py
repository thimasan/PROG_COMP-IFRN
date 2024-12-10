'''
   EXEMPLO 03:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantas palavras existem na string digitada
'''

frase = input('Informe uma frase ou string:')

intPosicao    = 0
intQtPalavras = 0

while intPosicao < len(frase):

    if frase[intPosicao] == ' ' and frase[intPosicao -1] != ' ':
        intQtPalavras += 1
    intPosicao += 1 


#verifica se a última palavra da frase foi contabilizada
if frase[-1] != ' ': intQtPalavras += 1

print(f"A quantidade de palavras é: {intQtPalavras}")