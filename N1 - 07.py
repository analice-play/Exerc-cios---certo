#cria uma lista chamada frutas que tenha pelo menos 5 frutas.
#adicionar e remover uma fruta da lista e mostrar a lista atualizada
import time

frutas_list = [
                'Maça',
                'Ameixa',
                'Uva',
                'Abacaxi',
                'Abacate'
                ]

for n in range(0,len(frutas_list)):
    print(f'{n} {frutas_list[n]}')

print('---'*15)

print('Qual o número da fruta a ser removido:')
num_remov = int(input('>>> '))

while num_remov not in range(0,len(frutas_list)):
    num_remov = int(input('Número inexistente! Digite novamente: '))

frutas_list.pop(num_remov), time.sleep(1)
print('Lista atualizada com sucesso!')

print('---'*15)

for n in range(0,len(frutas_list)):
    print(f'{n} {frutas_list[n]}')



