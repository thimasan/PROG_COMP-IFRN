#Fazer um programa que fique solicitando ao usuário para digitar um número
#  e informe se o número é par ou ímpar. O programa só deve encerrar quando o
#  usuário digitar o número 0.

numero = int(input("Digite um número qualquer : "))

while numero != 0:
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
    numero = int(input("Digite um número qualquer : "))