# programa que leia números inteiros e positivos, e que informe o maior
maior = num = 0
while True:
    num = int(input('Digite um número[0 para parar]: '))
    if num < 0:
        print('Digite um número positivo.')
    if num == 1:
        maior = num
    if num > maior:
        maior = num
    if num == 0:
        break
print(f'O maior número digitado foi {maior}.')