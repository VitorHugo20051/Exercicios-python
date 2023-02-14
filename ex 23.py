dentro_inter = 0
fora_inter = 0

for num in range(0,10):
    num = int(input('Digite um número: '))
    if 10 <= num <= 20:
        dentro_inter += 1
    else:
        fora_inter += 1

print(f'São {dentro_inter} números que estão dentro do intervalo [10,20].')
print(f'São {fora_inter} números que estão fora do intervalo [10,20].')