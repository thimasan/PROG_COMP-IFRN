altura = float(input("Informe sua altura em metros:"))
peso = float(input("Informe seu peso em kilos:"))

imc = peso / (altura ** 2)

print(f"Seu IMC foi de : {imc:.2f}")

if imc < 17:
    print('Você está muito abaixo do peso ideal!')
elif (imc > 17) and (imc < 18.50):
    print('Você está abaixo do peso.')
elif (imc > 18.5) and (imc < 25):
    print('Você está com peso normal.') 
elif (imc > 25) and (imc < 30):
    print('Você está acima do peso.')       
elif (imc > 30) and (imc < 35):
    print('Você está com obesidade GRAU 1.') 
elif (imc > 35) and (imc < 40):
    print('Você está com obesidade GRAU 2.')
elif imc > 40:
    print('Você está com obesidade GRAU 3 (Mórbida).')
else:
    print("Este não é um valor válido")


