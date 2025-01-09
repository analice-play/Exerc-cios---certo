#Quero um programa que faça um loop com while pra solicitar a senha de um login.
#o programa tem que continuar rodando até o usuário colocar a senha ("python123")

print('Seja bem-vindo!')

senha = str(input('Digite a senha: '))

while senha not in 'python123':
    senha = str(input('Senha errada! Tente novamente: '))

print('Senha correta! Acesso concluído.')

