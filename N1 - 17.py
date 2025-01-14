#Faça uma função que calcula o número fatorial de um número.
def line():
    print('-'*40)

def title(msg):
    line()
    print(f"{msg:^40}")
    line()
    print()

def fatorial(num, resu):

    opção_num = num
    multi = opção_num * (opção_num - 1)
    opção_num -= 2

    while opção_num != 0:
        resu += multi * opção_num
        opção_num -= 1

    print(f'\nA fatorial de {num}! é:')

    opção_num = num
    for c in range(0, opção_num):

        if c == (num -1):
            print(opção_num, end=' = ')
            print(resu)

        else:
            print(opção_num, end=' * ')

        opção_num -= 1


msg = 'FATORIAL!'
title(msg)

num = int(input('Digite um número: '))

opção_num = num
multi = resu = 0

fatorial(num, resu)


