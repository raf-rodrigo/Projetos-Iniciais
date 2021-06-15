'''Programa que irá calcular o determinante de uma matriz quadrada de ordem mxn'''
print('\033[34m~'*40)
print('DETERMINANTE DE UMA MATRIZ:'.center(40))
print('~'*40, '\033[m')
matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
m = int(input('qual a ordem de sua matriz: '))
for l in range(0, m):
    for c in range(0, m):
        matriz[l][c] = int(input((f'Digite o valor {l+1}X{c+1}: ')))
print('\033[34m~'*40, '\033[m')
for l in range(0, m):
    for c in range(0, m):
            print(f'{matriz[l][c]:^6}', end='')
    print()
print('\033[34m~'*40, '\033[m')
#calculo do determinandte
#multiplicando as diagonais



