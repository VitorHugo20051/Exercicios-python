numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
print(numeros)
numeros_pares = numeros_impares = 0

for c in numeros:
    if c % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print(f'Nesta série de número temos {numeros_pares} números pares e {numeros_impares} números ímpares.')