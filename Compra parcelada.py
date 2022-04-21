print('{:=^32}'.format(' LOJAS ZÉ '))
compra = float(input('Qual é o valor da sua compra? R$ '))
print('Selecione sua forma de pagamento?')
print('\033[33m[ 1 ] No dinheiro\033[m')
print('\033[33m[ 2 ] No Cartão à Vista\033[m')
print('\033[33m[ 3 ] Parcelado em 2x\033[m')
print('\033[33m[ 4 ] Parcelado em 3x ou mais\033[m')
opcao = int(input('Opção: '))
if opcao == 1:
    compra = compra - (compra * 10 / 100)
    print('Seu pagamento será R$ {:.2f} à vista no dinheiro.'.format(compra))
elif opcao == 2:
    compra = compra - (compra * 5 / 100)
    print('Seu pagamento será R$ {:.2f} à vista no cartão.'.format(compra))
elif opcao == 3:
    x = int(input('Em quantas vezes será o pagamento? '))
    if x == 1:
        print('Seu pagamento será R$ {:.2f} em 1x no cartão.'.format(compra))
    elif x == 2:
        print('Seu pagamento será R$ {:.2f} em 2x de {:.2f} no cartão.'.format(compra, compra / x))
    else:
        print('\033[31mERROR\033[31m')
elif opcao == 4:
    compra = compra + (compra * 20 / 100)
    x = int(input('Em quantas vezes será o pagamento? '))
    if 3 < x <= 12:
        print('Seu pagamento será R$ {:.2f}, parcelado em {}x de {:.2f} no cartão.'.format(compra, x, compra / x))
    else:
        print('ERROR')
else:
    print('\033[31mERROR\033[m')
































