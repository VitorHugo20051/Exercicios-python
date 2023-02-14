# validação de uma palavra-passe

password = str(input('Palavra-passe: ')).strip()

while True:
    if 6 <= len(password) <= 12:
        break
    elif password.isupper() and password.islower():
        break
    elif password in '0123456789':
        break
    elif password in '$#@':
        break
    else:
        print('Senha inválida.')
        password = str(input('Digite um senha válida: '))
print('Senha válida.')