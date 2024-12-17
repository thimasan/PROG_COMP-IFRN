'''
   EXEMPLO 04:
   Fazer um programa que solicite ao usuário uma palavra e em seguida imprima a palavra
   conforme o exemplo abaixo:

   Exemplo:
   Digite uma palavra: NATAL

   N
   NA
   NAT
   NATA
   NATAL
   NATA
   NAT
   NA
   N
'''
palavra = input('Digite uma palavra:')
#laço
for i in range(1, len(palavra)+1):
    print(palavra[:i])
for i in range(len(palavra)-1, 0, -1):
    print(palavra[:i])
