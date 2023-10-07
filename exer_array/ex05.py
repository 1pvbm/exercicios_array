'''Exercício 05
Ler um vetor A de 10 números. logo em
seguida, ler mais um número e guardar em
uma variável X.
Armazenar em um vetor M o resultado de
cada elemento de A multiplicado pelo
valor X. Logo após, imprimir o vetor M.'''
a = [''] * 10
for _ in range(10):
    a[_] = int(input(f'Digite o {_ + 1}ª Número: '))
x = int(input('Digite o valor para multiplicar cada elemento da lista: '))
m = [''] * 10
for i in range(10):
    m[i] = a[i] * x
print('-=-' * 20)
print(f'Os valores ta lista: {a}\nMultiplicador: {x}\nLista multiplicada: {m}')


