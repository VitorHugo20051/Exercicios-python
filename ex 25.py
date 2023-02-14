# contagem e soma dos algarismos de um número

num = int(input('Digite um número: '))
cont = 0

while num != 0:
    num //= 10
    cont += 1
print(cont)