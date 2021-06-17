print('Vamos calcular as raizes da equação de 2 grau')
print('Lembrando que a equação tem a forma de: ax²+bx+c=0')
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
if a != 0:
    if b > 0:
        if c > 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² + {b}x + {c} = 0'.center(40))
        elif c == 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² + {b}x = 0'.center(40))
        elif c < 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² + {b}x {c} = 0'.center(40))
    if b == 0:
        if c > 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² + {c} = 0'.center(40))
        elif c == 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² = 0'.center(40))
        elif c < 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² {c} = 0'.center(40))
    if b < 0:
        if c > 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² {b}x + {c} = 0'.center(40))
        elif c == 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² {b}x = 0'.center(40))
        elif c < 0:
            print('\033[34m-='*20)
            print('Sua é quação é:'.center(40))
            print(f'{a}x² {b}x {c} = 0'.center(40))
    print('-='*20, '\033[m')
    delta = b**2 - (4*a*c)
    x = x1 = x2 = xn = yn = 0
    y = c
    xn = -(b/(2 * (a)))
    yn = -((delta)/ (4 * (a)))
    if delta > 0:
        print('Sua equanção tem duas raizes reais.')
        x1 = (-(b) + delta**(1/2)) / (2*(a))
        x2 = (-(b) - delta**(1/2)) / (2*(a))
        print(f'As raizes da equação são: {x1} e {x2}')
    if delta == 0:
        print('A equação tem apenas uma solução real.')
        x = (-(b))/(2*(a)) 
        print(f'A raiz da equação é: {x}')
    if delta < 0:
        print('Não existe solução em reais.')
else:
    print('Você não digitou uma equação de 2° grau.')
    print('Finalizando....')
