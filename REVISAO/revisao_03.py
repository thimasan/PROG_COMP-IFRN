'''
   REVISÃO 03:

   Crie um arquivos chamado 'valores_entrada.txt' e no seu conteúdo digite 10 valores 
   inteiros quaisquer separados por espaço. 
   
   Em seguida, crie um programa que leia o conteúdo do arquivo e para cada valor lido calcule 
   seu fatorial e escreva o resultado em um arquivo chamado 'valores_saida.txt'.

   O arquivo 'valores_saida.txt' deve conter em cada linha o valor lido e seu fatorial separados por ;
'''

#LEITURA DO ARQUIVO 'valores_entrada.txt'
with open('valores_entrada.txt', 'w') as valores:
    valores.write('2 3 4 5 6 7 8 9 10 11')
    valores.close()

lstValores = list()
with open('valores_entrada.txt', 'r') as valores:
      lstValores = valores.read().split()
      valores.close()

#CÁLCULO DO FATORIAL DE CADA VALOR LIDO
lstFatoriais = list()
for valor in lstValores:
    fatorial = 1
    for i in range(1, int(valor) + 1):
        fatorial *= i
    lstFatoriais.append(f'{valor};{fatorial}')

#ESCRITA DO RESULTADO EM UM ARQUIVO CHAMADO 'valores_saida.txt'
with open('valores_saida.txt', 'w') as fatoriais:
    fatoriais.write('\n'.join(lstFatoriais))
    fatoriais.close()

#LEITURA DO ARQUIVO 'valores_saida.txt'
with open('valores_saida.txt', 'r') as fatoriais:
    print(fatoriais.read())
    fatoriais.close()
