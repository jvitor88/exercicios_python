print('='*30)
print('\033[33m{:^30}\033[m'.format('CAIXA ELETRÔNICO'))
print('='*30)
tot50 = c100 = c50 = c20 = c10 = c5 = c2 = 0
while True:
    sac = input('Qual valor gostaria de sacar? R$ ')
    if sac[-1] == '1' or sac[-1] == '3':
        print('\033[31mValor Incorreto!\033[m')
    else:
        sac = int(sac)
        while sac > 0:
            if sac >= 100:
                sac -= 100
                c100 += 1
            elif sac >= 50:
                sac -= 50
                c50 += 1
            elif sac >= 20:
                sac -= 20
                c20 += 1
            elif sac >= 10:
                sac -= 10
                c10 += 1
            elif sac >= 5:
                sac -= 5
                c5 += 1
            elif sac >= 2:
                sac -= 2
                c2 += 1
        if c100 != 0:
            print(f'Sairam {c100} cédulas de R$ 100')
        if c50 != 0:
            print(f'Sairam {c50} cédulas de R$ 50')
        if c20 != 0:
            print(f'Sairam {c20} cédulas de R$ 20')
        if c10 != 0:
            print(f'Sairam {c10} cédulas de R$ 10')
        if c5 != 0:
            print(f'Sairam {c5} cédulas de R$ 5')
        if c2 != 0:
            print(f'Sairam {c2} cédulas de R$ 2')
        break
