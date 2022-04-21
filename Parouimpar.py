from random import randint
from time import sleep
cont = 0
while True:
    print('+'*20)
    print('{:^20}'.format('PAR OU IMPAR'))
    print('+'*20)
    j = int(input('Diga o valor: '))
    pi = str(input('Par ou Impar [P/I]: ')).upper()[0]
    pc = randint(0, 10)
    soma = j + pc
    if pi == 'P':
        if soma % 2 == 0:
            print(f'Vc jogou {j} e o PC {pc}. Total de {soma}, DEU PAR')
            print('Parabéns! Você ganhou')
            print('Vamos jogar novamente...')
            print('+' * 20)
        else:
            print(f'Vc jogou {j} e o PC {pc}. Total de {soma}, DEU ÍMPAR')
            print('Você perdeu!')
            print('\033[31m-----GAME OVER-----\033[m')
            print(f'Você acertou {cont} vezes.')
            break
    if pi == 'I':
        if soma % 3 == 0:
            print(f'Vc jogou {j} e o PC {pc}. Total de {soma}, DEU ÍMPAR')
            print('Você perdeu!')
            print('\033[31m-----GAME OVER-----\033[m')
            print(f'Você acertou {cont} vezes.')
            break
        else:
            print(f'Vc jogou {j} e o PC {pc}. Total de {soma}, DEU PAR')
            print('Parabéns! Você ganhou')
            print('Vamos jogar novamente...')
            print('+' * 20)
    cont += 1


