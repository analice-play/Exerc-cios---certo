frutas = [
            'Banana', 
            'Maça', 
            'Abacaxi', 
            'Uva'
        ]

resp = str(input('Você deseja adicionar ( A ) ou retirar ( R )? ')).upper().split()[0]

while resp not in 'AR':
    resp = str(input('Opção inexistente! Você deseja adicionar ( A ) ou retirar ( R )? ')).upper().split()[0]

if resp == 'A':
    adicionar = str(input('Fruta a ser adicionada: '))

    while adicionar in frutas:
        print('Essa fruta já existe! Tente novamente.')
        adicionar = str(input('>>> '))

    frutas.append(adicionar)

elif resp == 'R':
    print('Frutas disponíveis')
    print(frutas)
    retirar = str(input('Fruta a ser retirada: '))

    while retirar not in frutas:
        print('A opção escolhida não existe! Tente novamente.')
        retirar = str(input('>>> '))
    
    frutas.remove(retirar)
print('---'*20)
for f in range(0,len(frutas)):
    print(frutas[f])

print('\nPrograma finalizado com sucesso!')