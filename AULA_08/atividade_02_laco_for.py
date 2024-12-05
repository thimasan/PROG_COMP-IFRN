'''
 Faça um programa que solicite ao usuário um valor n inteiro positivo e 
   imprima os n primeiros trios de valores que formam um triângulo pitagórico
'''
numero = int(input("Digite um número inteiro positivo: "))

for i in range (1, numero + 1):
    for j in range (1, numero + 1):
        for k in range (1, numero + 1):
            if i**2 == j**2 + k**2:
                print(f'{i} {j} {k}')
                break
            if i**2 < j**2 + k**2:
                break
