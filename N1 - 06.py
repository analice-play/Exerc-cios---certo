#Quero que você crie uma lista chamada números, contendo números de 1 a 15.
#Criar uma lista que tenha só múltiplos de 3
#inverter a ordem da lista
#printar o resultado

list_num = list(range(1,16))

mult_3 = []
p = 0

for p in range(0,15):
    if list_num[p] % 3 == 0:
        mult_3.append(list_num[p])

mult_3.sort(reverse=True), print(f'Números múltiplos de 3 na ordem decrescente: {mult_3}')