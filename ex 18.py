# string ao contrário
palavra = str(input('Digite uma palavra: '))

for c in range(len(palavra) - 1, -1, -1):
    print(palavra[c],end='')