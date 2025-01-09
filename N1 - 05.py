#Input: cores = ('vermelho', 'verde', 'azul') Quero que teu programa:
#Converta tupla pra lista, adicione a cor ''amarelo'' na lista e converta de volta pra tupla

cores = ('Vermelho','Verde','Azul')

while True:
    cor = str(input('Cor a ser adicionada: '))
    resp = str(input('Deseja adicionar outra cor? [S/N] ')).strip().upper()[0]

    while resp not in 'SN':
        resp = str(input('Resposta inválida! Deseja adicionar outra cor? [S/N] ')).strip().upper()[0]

    cores = list(cores)
    cores.append(cor)
    cores = tuple(cores)

    if resp == 'N':
        break

print(f'Listagem das cores: {cores}')