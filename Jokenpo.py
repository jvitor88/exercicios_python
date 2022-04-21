from random import randint
print('{:=^30}'.format(' JO - KEN - PO '))
lista = ['NDA', 'PEDRA', 'PAPEL', 'TESOURA']
pc = randint(1, 3)
print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
esc = int(input('Qual é a sua jogada: '))
print("-=" * 10)
if esc == 1:
    print('PC jogou {}'.format(lista[pc]))
    print('Vc jogou {}'.format(lista[esc]))
    print("-=" * 10)
    if pc == 1:
        print('EMPATE')
    elif pc == 2:
        print('SE FERROU! PC GANHOU')
    else:
        print('PARABÉNS! VC GANHOU')
elif esc == 2:
    print('PC jogou {}'.format(lista[pc]))
    print('Vc jogou {}'.format(lista[esc]))
    print("-=" * 10)
    if pc == 1:
        print('PARABÉNS! VC GANHOU')
    elif pc == 2:
        print('EMPATE')
    else:
        print('SE FERROU! PC GANHOU')
elif esc == 3:
    print('PC jogou {}'.format(lista[pc]))
    print('Vc jogou {}'.format(lista[esc]))
    print("-=" * 10)
    if pc == 1:
        print('SE FERROU! PC GANHOU')
    elif pc == 2:
        print('PARABÉNS! VC GANHOU')
    else:
        print('EMPATE')
else:
    print('\033[31mERROR\033[m')