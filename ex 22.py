# fatorial de um número sem math

num = int(input('Digite um número: '))
fatorial = 1

for c in range(num, 0, -1):
    fatorial *= c
print(fatorial)