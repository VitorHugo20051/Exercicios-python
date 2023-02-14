# sequencia de fibonacci

print('Sequencia de Fibonacci')
n = int(input('Digite a quantidade de termos desejado: '))
n1, n2 = 0, 1
cont = 0

while n > cont:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    print(f'{n1} ',end='')