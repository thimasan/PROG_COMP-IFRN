salario_base = float(input("Informe o seu salário base:"))
total_vendas = float(input("Informe o valor total de suas vendas:"))
percentual = float(input("Informe o percentual de sua comissão:"))

salario_final =  salario_base + ((percentual/100) * total_vendas)

print(f"O seu salário final (salario base + comissão) é de R$ {salario_final:.2f}")