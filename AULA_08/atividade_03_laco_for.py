'''
Faça um programa que solicite um valor n inteiro positivo e 
   apresente o seu correspondente em binário.
'''
import sys

n = int(input("Digite o valor a ser convertido em binário: "))

if n <= 0:
   sys.exit('O número deve ser positivo...')
   
binario = ''
    
# Enquanto o número for maior que 0
while n >= 0:
   resto = n % 2
   binario = str(resto) + binario
   n = n // 2

print(f'O número em binário é: {binario}')