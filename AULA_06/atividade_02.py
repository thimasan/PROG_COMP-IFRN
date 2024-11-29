# Fazer um programa que fique lendo números inteiros do usuário até que ele digite 0.
# Quando o usuário digitar 0, o programa deve imprimir a soma de todos os números digitados bem como a média aritmética.
numero = int(input("Digite um número qualquer : "))
soma = 0
contador = 0
while True:
    if numero == 0:
        break
    soma += numero
    contador += 1
    numero = int(input("Digite um número qualquer : "))

print(f'A soma dos números digitados é {soma}')
print(f'A média aritmética dos números é {soma/contador}')
