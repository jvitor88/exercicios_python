print('CADASTRO DE PRODUTOS')
print('='*22)
soma = pmaior = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Valor R$: '))
    cont += 1
    r = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    print('='*20)
    soma += preco
    if preco > 1000:
        pmaior += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if r == 'N':
        break
print(f'Total da compra e R$ {soma:.2f}')
print(f'Temos {pmaior} produtos valendo + 1.000,00')
print(f'O nome do produto mais barato é {barato} e custa: R${menor:.2f}')

