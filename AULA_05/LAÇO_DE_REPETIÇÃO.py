# Q1. Fazer um programa que solicite um valor inteiro e calcule seu fatorial.
# Q2. Fazer um programa que solicite um valor inteiro positivo (n) e imprima os n primeiros elementos da sequência de Fibonacci.
 import sys

numero = int(input("Digite um número para calcular seu fatorial : "))

if numero < 0:
    print("Informe um número >= 0")
    sys.exit()

if numero == 0 or numero == 1:
    print(f'{numero}! = 1')

fatorial = 1
contador = numero
while contador > 0:
   fatorial *= contador
   contador -= 1
print(f'{numero}! = {fatorial})


    

