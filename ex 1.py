# dizer se número é positivo, negativo ou neutro

num = int(input('Digite um número: '))

if num < 0:
    print('Este número é negativo.')

elif num == 0:
    print('Este número é neutro.')

else:
    print('Este número é positivo.')