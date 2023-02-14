# alagrismos pares em números

for c in range(100,401):
    n = str(c)
    if int(n[0]) % 2 == 0 and int(n[1]) % 2 == 0 and int(n[2]) % 2 == 0 :
        print(f'{c} ',end='')