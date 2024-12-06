'''
 Faça um programa que solicite ao usuário um valor n inteiro positivo e 
   imprima os n primeiros trios de valores que formam um triângulo pitagórico
'''
numero = int(input("Digite um número inteiro positivo: "))

for c in range (1, numero + 1):
    for b in range (1, c + 1):
        for a in range (1, b + 1):
            if c**2 == b**2 + a**2:
                print(f'{c} {b} {a}')
                break
