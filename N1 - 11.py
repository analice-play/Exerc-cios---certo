matriz = [[], [], []]

list_num = []

for l in range(0,3):
    for c in range(0,3):
        num = int(input(f'Digite o número ({l+1},{c+1}): '))
        list_num.append(num)

        matriz[l].insert(c, num)

print('-'*5, 'MATRIZ', '-'*5)

for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^5}', end=' ')
    print()

print(f'O maior número apresentado é: {max(list_num)}')
print(f'A soma dos números apresentados é: {sum(list_num)}')
