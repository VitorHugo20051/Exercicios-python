# placar de um jogo de futebol

equipa1 = int(input('Golos da equipa 1: '))
equipa2 = int(input('Golos da equipa 2: '))

if equipa1 > equipa2:
    print(f'A equipa 1 ganhou {equipa1} x {equipa2} á equipa 2.')

elif equipa1 == equipa2:
    print('O jogo ficou empatado.')

else:
    print(f'A equipa 2 ganhou {equipa2} x {equipa1} á equipa 1.')