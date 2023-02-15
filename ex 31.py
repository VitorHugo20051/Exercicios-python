# programa que leia preço de produtos e no final mostre o total a pagar, se for mais de 1000 desconto de 10%

soma = 0

while True:
    preço = float(input('Digite o preço do produto[0 para parar]: €'))
    soma += preço
    if preço < 0:
        print('Preço inválido, tente novamente.')
    if soma > 1000:
        soma = soma - (soma * (10 / 100))
    if preço == 0:
        break
print(f'O total da compra é {soma:.2f}€')