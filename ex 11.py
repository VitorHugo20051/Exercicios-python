num = 1
cont = soma = 0

while num != 0:
    num = int(input('Digite um número(0 para parar): '))
    cont += 1
    soma = soma + num
media = soma / (cont - 1)
print(f'A soma dos números digitados é {soma} e a média é {media}')