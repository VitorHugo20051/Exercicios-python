# reajuste salarial

salario = float(input('Digite o seu salário: €'))

if salario < 500:
    novo_salario = salario + (salario * 0.15)
    print(f'Com um aumento de 15% seu salario passa de {salario}€ para {novo_salario}€.')

elif 500 <= salario <= 1000:
    novo_salario = salario + (salario * 0.10)
    print(f'Com um aumento de 10% seu salario passa de {salario}€ para {novo_salario}€.')

else:
    novo_salario = salario + (salario * 0.05)
    print(f'Com um aumento de 5% seu salario passa de {salario}€ para {novo_salario}€.')