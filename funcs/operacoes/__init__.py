def metade(a):
    return a / 2


def dobro(a):
    return a * 2


def aumento(a, b):
    b = a + (a * b / 100)
    return b


def reducao(a, c):
    b = a - (a * c / 100)
    return b


def moeda(a, r = 'R$'):
    return f'{r}{a : .2f}'.replace('.', ',')


def resumo(a=0, b=0, c=0):
    print('-'*32)
    print(f'{"RESUMO DO VALOR" : ^32}')
    print('-'*32)
    print(f'Preço analisado: {moeda(a) : >15}')
    print(f'Dobro do preço: {moeda(dobro(a)) : >16}')
    print(f'Metade do preço: {moeda(metade(a)) : >15}')
    print(f'{b} de aumento: {moeda(aumento(a, b)) : >17}')
    print(f'{c} de aumento: {moeda(reducao(a, c)) : >17}')