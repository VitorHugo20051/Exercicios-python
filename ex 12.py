# relatório de controlo de consumo de água

altura_reservatorio = float(input('Digite a altura do reservatório:(cm) '))
largura_reservatorio = float(input('Digite a largura do reservatório:(cm) '))
comprimento_reservatorio = float(input('Digite o comprimento do reservatório:(cm) '))
consumo = float(input('Digite o consumo diário de água:(litro/dia) '))

volume = (altura_reservatorio * largura_reservatorio * comprimento_reservatorio) / 1000
autonomia = volume / consumo

print(f'A capacidade total do reservatório é de {volume:.1f} litros.')
print(f'Para um consumo de {consumo} litros/dia o reservatório tem uma autonomia de {autonomia:.0f} dias.')

if autonomia < 2:
    print('Consumo elevado!')

elif 2 <= autonomia <= 7:
    print('Consumo moderado!')

elif autonomia > 7:
    print('Consumo reduzido!')