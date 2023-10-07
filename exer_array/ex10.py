'''Exercício 10
Faça um código para ler um valor N qualquer (que
será o tamanho dos vetores). Após, ler dois
vetores A e B (de tamanho N cada um) e depois
armazenar em um terceiro vetor Soma a soma dos
elementos do vetor A com os do vetor B
(respeitando as mesmas posições) e escrever o
vetor Soma.'''

valor_n = int(input('Digite um valor qualquer para ser o tamanho da lista: '))
A = [''] * valor_n
B = [''] * valor_n
for _ in range(valor_n):
    A[_]= int(input(f'Digite o {_ + 1}ª valor para lista "A ": '))
for i in range(valor_n):
    B[i] = int(input(f'Digite o {i + 1} valor para lista "B": '))
soma = [''] * valor_n
for j in range(valor_n):
    soma[j] = A[j] + B[j]
print(f'A soma dos vetores entra a lista A e da Lista B são : {soma}')
