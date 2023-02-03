# encontrar números entre 100 e 400 (ambos inclusos), onde cada dígito de um número é um número par

lista = []
for c in range(100, 401):
    num = str(c)

    if int(num[0]) % 2 == 0 and int(num[1]) % 2 == 0 and int(num[2]) % 2 == 0   :
        lista.append(num)
print(','.join(lista))