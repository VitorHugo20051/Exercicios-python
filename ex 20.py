# número de letras e números numa string

string_1 = str(input('Digite qualquer coisa: '))
cont_letras = cont_num = 0

for c in string_1:
    if c.isalpha():
        cont_letras += 1
    elif c.isnumeric():
        cont_num += 1
    else:
        pass

print(f'Quantidade de letras: {cont_letras}')
print(f'Quantidade de números: {cont_num}')