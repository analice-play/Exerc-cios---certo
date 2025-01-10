list_frutas = [
    {
        'nome': 'Maça',
        'valor/kg': 18.5
    },
    {
        'nome': 'Uva',
        'valor/kg': 17.99
    },
    {
        'nome': 'Banana',
        'valor/kg': 8.55
    },
    {
        'nome': 'Pessego',
        'valor/kg': 18.99
    }
                ]

frutas = dict()
print(f'{'Frutas disponíveis':^45}')

for k in range(0, len(list_frutas)):
    print(f'{k+1} - {list_frutas[k]['nome']}')

while True:
    resp_usuário = str(input('Deseja adicionar alguma fruta a lista de vendas? ')).upper().split()[0]
    while resp_usuário not in 'SN':
        resp_usuário = str(input('Deseja adicionar alguma fruta a lista de vendas? ')).upper().split()[0]
        
    if resp_usuário == 'S':
        print('---'*20)
        nome = str(input('Fruta a ser adicionada: '))

        for k in list_frutas:
            if nome == k['nome']:
                while nome == k['nome']:
                    print('\033[31mA fruta escolhida já existe no sistema!')
                    nome = str(input('\033[mDigite novamente: '))

        valor = float(input('Valor por kg: '))
        print('---'*20)

        frutas['nome'] = nome
        frutas['valor/kg'] = valor
        list_frutas.append(frutas.copy())
        frutas.clear()

        print(f'A fruta {nome} foi adicionada com sucesso!')

    elif resp_usuário == 'N':
        break

print('--'*40)
print(f'{'Frutas disponíveis':^10} | {'Preço por kg':^8}')
for k in list_frutas:
    print(f'{k['nome']:<20}     {k['valor/kg']:.2f}')
