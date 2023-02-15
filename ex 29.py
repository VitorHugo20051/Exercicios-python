# soma dos números digitados
soma = 0
while True:

    num = int(input('Digite um número:[0 para parar]: '))
    soma += num
    if num == 0:
        break
print(f'A soma dos números digitados é {soma}.')