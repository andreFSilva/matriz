"""
MATRIZ


matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(0)
    matriz.append(linha)
print(matriz)


=============================================


# Calcular a média da turma

turma = [[5.0, 4.5, 7.0, 5.2, 6.1], [2.1, 6.5, 8.0, 7.0, 6.7], [8.6, 7.0, 9.1, 8.7, 9.3]]

media = 0

for i in range(3):
    for j in range(5):
        media += turma[i][j]
media = media / 15

print(media)


===================================================================

# Preencher a matriz por leitura

turma = []
for i in range(3):
    linha  = []
    for j in range(5):
        linha.append(int(input('Digite a nota [' + str(i) + ', ' + str(j) + '] :  ')))
    turma.append(linha)

print(turma)


=====================================================================================
# Programa que cria uma matriz n x m preenchida com zeros

n = int(input('Digite a dimensão N da matriz: '))
m = int(input('Digite a dimensão M da matriz: '))
matriz = []
for i in range(n):
    lista = []
    for j in range(m):
        lista.append(0)
    matriz.append(lista)
print(matriz)
=================================================================================
# Simplificando o exemplo
# Programa que cria uma matriz n x m preenchida com zeros


n = int(input('Digite a dimensão N da matriz: '))
m = int(input('Digite a dimensão M da matriz: '))
matriz = []
for i in range(n):
    matriz.append([2] * m)

============================================================================


# Imprimir em forma de matriz
# Programa que cria uma matriz n x m preenchida com
# zeros e a imprime no formato de matriz


matriz = []
n = int(input('Digite a dimensão N da matriz: '))
m = int(input('Digite a dimensão M da matriz: '))

for i in range(n):
    matriz.append([0] * m)
    print(matriz[i])


=========================================================================

Programa que lê uma matriz 3x3 digitada pelo usuário e
conta quantos números pares existem na matriz,
imprimindo na tela o resultado e a matriz.

matriz = [] # a matriz
n = int(input('Digite a dimensão N da matriz: ')) # valor de n
m = int(input('Digite a dimensão M da matriz: ')) # valor de m

for i in range(n):
    lista = [] # lista vazia
    for j in range(m):
        lista.append(int(input('Digite os valores [' + str(i) + ', ' + str(j) + '] :')))
    matriz.append(lista)

    # Conta os números pares
pares = 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] % 2 == 0:
            pares += 1

for i in range(n):
    print(matriz[i])
print('A matriz contém', pares, 'números pares')

===========================================================================================

matriz = [] # a matriz
n = int(input('Digite a dimensão N da matriz: ')) # valor de n
m = int(input('Digite a dimensão M da matriz: ')) # valor de m

for i in range(n):
    linha = []
    for j in range(m):
        linha.append(int(input('Digite os números [' + str(i) + ', ' + str(i) + ' ] :')))
    matriz.append(linha)

for i in range(n):
    print(matriz[i])

# valores pares
pares = 0
for linha in matriz:
    for valores in linha:
        if valores % 2 == 0:
            pares += 1

print(f'Contém {pares} números na matriz')

==============================================================

matriz = []  # a matriz
for i in range(4):
    linha = []
    linha.append(input('Digite seu nome: ' + str(i) + ' : '))
    linha.append(int(input('Digite sua idade: ' + linha[0] + ' : ')))
    matriz.append(linha)

for i in range(4):
    print(matriz[i])

# procura a pessoa mais nova
menor = matriz[0][1]
pos = 0
for i in range(5):
    if matriz[i][1] < menor:
        menor = matriz[i][1]
        pos = i

print(f'A pessoa mais nova é: {matriz[pos][0]}')


============================================================================

"""


class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        row = []
        for i in range(index):



    def column(self, index):


