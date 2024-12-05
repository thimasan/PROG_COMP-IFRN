'''
Faça um programa que solicite um valor n inteiro positivo e 
   apresente o seu correspondente em binário.
'''
numero = int(input("Digite um número inteiro positivo:"))

for i in range (numero + 1):
    print(f'{i} em binário é {bin(i)}')