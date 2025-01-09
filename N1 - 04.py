#Crie uma tupla chamada dias semana que tenha os dias da semana.
#Printar o terceiro dia da semana e quero que você depois mude para outro dia da semana e me informe o que aconteceu

dias_semana = ( 'Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira')

print(f'O terceiro dia da semana é: {dias_semana[2]}') # n entendei se era para fazer só isso
print(f'Se passou mais um dia e chegados no quarto dia da semana: {dias_semana[3]}')

for c in dias_semana:
    print(f'O {c+1}º dia da semana é: {dias_semana[c]}')
