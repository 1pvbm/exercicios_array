'''Exercício 06
Faça um código para ler 5 números e
armazenar em um vetor. Após a leitura
total dos 5 números, o código deve
escrever esses 5 números lidos na ordem
inversa.'''
rafa = [''] * 5
for _ in range(0, 5, 1):
    rafa[_] = int(input(f'Digite seu {_ + 1 }ª Número: '))
for i in range(4, -1,-1):
    print(rafa[i], end=' ')