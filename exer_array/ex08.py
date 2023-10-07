'''Exercício 08
Faça um código para ler 5 nomes de
usuários e suas respectivas senhas, e
armazenar cada lista em um array
diferente, após completar a digitação,
imprimir , nome, senha e posição dos
dados no array'''
list_a = [''] * 5
list_b = [''] * 5
for i in range(0, 5):
    list_a[i] = input('Digite Seu Nome: ')
    list_b[i] = input('Digite Sua Senha: ')
for j in range(0,5):
    print(f'Nome: {list_a[j]}\nSenha: {list_b[j]}\nSeu índice: {j}')
    print()