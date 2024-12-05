'''Faça um programa que solicite um valor n inteiro positivo e 
   imprima na tela o seguinte padrão:

   para n = 4

   o programa deverá imprimir

   1
   2 2
   3 3 3
   4 4 4 4
'''
numero = int(input("Digite um número inteiro positivo: "))

for i in range (numero + 1):
    print(f'{i} ' * i)