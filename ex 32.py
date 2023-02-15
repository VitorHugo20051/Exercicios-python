# soma e média

soma = media = cont = 0
while True:
    num = int(input('Digite um número[0 para parar]: '))
    soma += num
    if num == 0:
        break
    cont += 1
media = soma / cont
print(f'A soma dos números digitados é {soma} e a média é {media}.')