'''
   EXEMPLO 07:

   Usando o dicionário dictAlunos faça um programa que solicite ao usuário a matrícula de um 
   aluno:
   
    - Caso a matrícula não exista no dicionário, o programa deverá solicitar as duas notas 
    da disciplina e adicione os valores digitados no dicionário;

    - Caso a matrícula já exista no dicionário, o programa deverá exibir a mensagem "Matrícula já  existe!" 
    mostrar as notas cadastradas e solicitar as novas notas.  

   O programa deve continuar solicitando a matrícula e as notas até que o usuário digite a
   matrícula 0.

   Ao final, o programa deve exibir o dicionário dictAlunos.
'''

dictAlunos = dict()

matricula = input('Digite a matrícula do aluno: ')
if matricula in dictAlunos.keys():  #verificar se está nas chaves do dicionário
    print('Matrícula já existe!')
    print(dictAlunos[matricula])
else:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    dictAlunos[matricula] = [nota1, nota2]

while matricula != '0':
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    dictAlunos[matricula] = [nota1, nota2]
    matricula = input('Digite a matrícula do aluno: ')

print(dictAlunos)
