valor_produto = float(input("Informe o preço do produto que deseja:"))
desconto_produto = float(input("Informe quantos % de desconto irá descontar:"))

valor_final =  valor_produto - ((desconto_produto/100) * valor_produto)

print(f'O valor final do produto com desconto é de: R$ {valor_final:.2f}')