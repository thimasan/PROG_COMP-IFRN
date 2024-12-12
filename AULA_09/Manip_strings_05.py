'''
   EXEMPLO 05:
   Fazer um programa em que o usuário informe uma string e depois uma palavra
   e em seguida o programa informe se a palavra informada está na string informada
'''

palavra = str(input("Digite uma palavra"))
frase = str(input("Digite uma frase ou string:"))

palavras = frase.split()

for palavra in palavras :
    print('A palavra está na frase')

if palavra.lower() == palindromo.lower():
    print('É palindromo')
else:
    print('Não é palindromo')