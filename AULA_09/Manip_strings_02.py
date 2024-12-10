'''
   EXEMPLO 02:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantas vogais existem na string digitada
'''

#Solicita ao usuário que informe uma frase:

frase = input("Informe uma frase:")

#Inicializa a variável que irá armazenar a quantidade de vogais

intQtVogais = 0

# Percorre cada caractere da frase digitada

for caractere in frase:
    if caractere.lower() in 'aeiouãõáéíóúâêîôûàèìòùäëïöü':
        intQtVogais += 1
    