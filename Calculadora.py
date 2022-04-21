n1 = int(input('Digite o 1° Valor: '))
n2 = int(input('Digite o 2° Valor: '))
op = 0
while op != 5:
    print('=-' * 10)
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    print('=-' * 10)
    op = int(input('>>>>> Qual é a sua opção: '))
    if op == 1:
        resp = n1 + n2
        print('O resultado de {} + {} é: {}'.format(n1, n2, resp))
    elif op == 2:
        resp = n1 * n2
        print('O resultado de {} x {} é: {}'.format(n1, n2, resp))
    elif op == 3:
       if n1 > n2:
           print('O maior numero entre {} e {} é: {}'.format(n1, n2, n1))
       elif n1 == n2:
           print('Os numeros {} e {} são iguais'.format(n1, n2))
       else:
           print('O maior numero entre {} e {} é: {}'.format(n1, n2, n2))
    elif op == 4:
        n1 = int(input('Digite o 1° Valor: '))
        n2 = int(input('Digite o 2° Valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-' * 10)
print('FIM')
