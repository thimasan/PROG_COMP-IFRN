'''
   EXEMPLO 01:
   Fazer um programa que solicite ao usuário valor inteiro positivo e em seguida
   imprima conforme o exemplo abaixo:  

   Exemplo:
   Digite um valor inteiro: 5

   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
'''
valor = int(input('Digite um número inteiro positivo:'))

#laço

for i in range (1,valor + 1):
   for j in range (1, i+1):
      print(j, end='')
   print()