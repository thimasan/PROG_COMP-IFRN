'''
   REVISÃO 01:

   O código a seguir gera uma lista com os n primeiros números da sequência de Fibonacci.

   # ------------------------------------------------------------
   n = int(input('Digite o valor de n: '))
   
   a, b = 1, 1
   
   lstFibonacci = list()
   for _ in range(n):
      lstFibonacci.append(a)
      a, b = b, a + b

   print(lstFibonacci)
   # ------------------------------------------------------------
   
   Reescreva o código acima gerando a lista lstFibonacci utilizando List Comprehension 
   e em seguida escreva o resultado em um arquivo chamado 'fibonacci.csv' escrevendo os 
   elementos da lista de Fibonacci em uma linha apenas, separando cada um deles por ;. 
'''
#GERANDO A LISTA DE FIBONACCI COM LIST COMPREHENSION
n = int(input('Digite o valor de n: '))
'''   
#a, b = 1, 1
a = 1
b = 1  
lstFibonacci = list()
for _ in range(n):
  lstFibonacci.append(a)
  a, b = b, a + b

print(lstFibonacci)
'''
#ESCREVENDO O RESULTADO EM UM ARQUIVO CHAMADO 'fibonacci.csv'
lstFibonacci = list()

lstFibonacci = [1 if i == 0 else 1 if i == 1 else lstFibonacci[i-1] + lstFibonacci[i-2] for i in range(n)]
with open('fibonacci.csv', 'w') as fibo:
      fibo.write(';'.join(map(str, lstFibonacci)))
      fibo.close()
    