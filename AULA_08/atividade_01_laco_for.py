'''Faça um programa que solicite um valor n inteiro positivo e 
   imprima na tela o seguinte padrão:

   para n = 4

   o programa deverá imprimir

   1
   2 2
   3 3 3
   4 4 4 4
'''
import sys
numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    sys.exit("Número inválido!")
for i in range (1, numero + 1):
    print(f'{i} ' * i)