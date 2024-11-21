#           SOMATORIO DAS UNIDADES
numero = int(input("Informe um número com no máximo 4 digitos: "))

rest_val = numero // 10000

if (rest_val >= 1):
    print("Este não é um número válido!")
else:
    valor_milhar = numero // 1000
    resto_milhar = numero % 1000
    valor_centena = resto_milhar // 100
    resto_centena = resto_milhar % 100
    valor_dezena = resto_centena // 10
    resto_dezena = resto_centena % 10
    valor_unidade = resto_dezena
    
    somatorio = valor_milhar + valor_centena + valor_dezena + valor_unidade

    print(f'A soma dos algorismos de {numero} é: {somatorio}')
    print(f'Milhar:{valor_milhar} Centena:{valor_centena} Dezena:{valor_dezena} Unidade:{valor_unidade}')