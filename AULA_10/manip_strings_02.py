'''
   EXEMPLO 02:
   Fazer um programa em que o usuário informe duas palavras e em seguida
   informe se elas são anagramas.
   
   Anagrama: é uma palavra ou frase formada pela transposição das letras de outra 
   palavra ou frase. 
'''

# Solicita ao usuário que informe uma string
strPalavra01 = input('Informe uma palavra: ')
strPalavra02 = input('Informe outra palavra: ')

strPalavra01Sub = strPalavra01.replace(' ', '')
strPalavra02Sub = strPalavra02.replace(' ', '')

strPalavra01Sub = sorted(strPalavra01Sub).lower
strPalavra02Sub = sorted(strPalavra02Sub).lower

