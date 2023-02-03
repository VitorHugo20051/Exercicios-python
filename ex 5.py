# Se o nome for "Optimus Prime", imprima "Bem-vindo, você é um guerreiro de Cybertron". Caso contrário, imprima "Bom dia, NOME"

nome = str(input('Qual é o seu nome? ')).upper().strip()

if nome in 'OPTIMUS PRIME':
    print('Bem-vindo, você é um guerreiro de Cybertron.')

else:
    print(f'Bom dia, {nome}!')