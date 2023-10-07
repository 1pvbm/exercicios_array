'''Exercício 09
Altere o sistema anterior e faça um sistema
de login, pedindo a senha do usuário e
mostrando seu nome e a mensagem, login
efetuado com sucesso.'''
print('-' * 40)
print('Cadastre seu Usuário e senha ')
print()
list_a = [''] * 1
list_b = [''] * 1
for i in range(1):
    list_a[i] = input('Cadastre Seu Nome: ')
    list_b[i] = input('Cadastre Sua Senha: ')
print()
print('Agora efetue seu loggin: ')
senha = input('Digite a sua senha: ')

while senha != list_b[0]:
    senha = input('<ERROR> SENHA INVÁLIDA. Digite novamente sua senha: ')
else:
    print(f'Bem Vindo Sr(a). {list_a[0]}, loggin efetuado com sucesso. ')
