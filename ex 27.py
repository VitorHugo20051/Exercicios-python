# senhas iguais

senha = str(input('Senha: ')).strip()
senha_2 = str(input('Digite sua senha novamente: ')).strip()

while True:
    if senha == senha_2:
        break
    else:
        print('Senhas não correspondem.')
        senha_2 = str(input('Digite sua senha novamente: '))
print('Login efetuado.')