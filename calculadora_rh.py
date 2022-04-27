print('~'*50)
print(f"{'CALCULADORA DE RH' : ^50}")
print('~'*50)
um = dois = tres = quatro = cinco = seis = sete = oito = nove = dez = 0
list = [um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez]
#Pergunta 1
print('1. Como você armazena informações e documentos dos funcionários (informações pessoais, bancárias, atestados, advertências, etc)?')
print('''a) O nosso contador armazena estas informações.
b) Há formulários em papel armazenados em arquivo físico.
c) Temos uma planilha em excel com os dados.
d) Temos um sistema onde armazenamos as informações.''')
um = input('Resposta 1: ').strip().lower()[0]
while um not in 'abcd':
    print('\033[31mERROR\033[m')
    um = input('Resposta 1: ').strip().lower()[0]
#Pergunta 2
print('2. Como você melhor descreve o processo de recrutamento e seleção na sua empresa?')
print('''a) Não temos um processo, fazemos tudo manual.
b) Quem faz este processo é uma empresa terceirizada.
c) Temos um processo padrão da empresa que é controlado por uma pessoa.
d) Temos um sistema que automatiza este processo.''')
dois = input('Resposta 2: ').strip().lower()[0]
while dois not in 'abcd':
    print('\033[31mERROR\033[m')
    dois = input('Resposta 2: ').strip().lower()[0]
#Pergunta 3
print('3. Qual a melhor maneira que sua empresa encontrou para reforçar a marca empregadora?')
print('''a) Não nos preocupamos com essa área.
b) Realizamos ações que ampliam a satisfação do time.
c) Usamos as redes sociais como aliadas para mostrar o dia a dia da empresa.
d) Procuramos ser certificados como uma das melhores empresa para se trabalhar.''')
tres = input('Resposta 3: ').strip().lower()[0]
while tres not in 'abcd':
    print('\033[31mERROR\033[m')
    tres = input('Resposta 3: ').strip().lower()[0]
#Pergunta 4
print('4. Como você melhor descreve o processo de admissão de funcionários na sua empresa?')
print('''a) Não temos um processo padrão.
b) Quem faz este processo é a contabilidade.
c) Temos um processo padrão da empresa que é controlado por uma pessoa.
d) Temos um sistema que automatiza este processo e comunica com os nossos fornecedores.''')
quatro = input('Resposta 4: ').strip().lower()[0]
while quatro not in 'abcd':
    print('\033[31mERROR\033[m')
    quatro = input('Resposta 4: ').strip().lower()[0]
#Pergunta 5
print('5. Como funciona o processo de pesquisa de clima da sua empresa?')
print('''a) Não realizamos pesquisa de clima.
b) Montamos perguntas em uma planilha e enviamos para os colaboradores preencherem.
c) Fazemos por meio de um formulário online.
d) Realizamos por meio de uma ferramenta de pesquisa de clima.''')
cinco = input('Resposta 5: ').strip().lower()[0]
while cinco not in 'abcd':
    print('\033[31mERROR\033[m')
    cinco = input('Resposta 5: ').strip().lower()[0]
#Pergunta 6
print('6. Como você melhor descreve a gestão de férias em sua empresa?')
print('''a) Não controlamos férias.
b) Controlamos férias em uma planilha de excel.
c) Quem controla é a contabilidade.
d) Temos um sistema online que os funcionários podem solicitar férias e acompanhamos o saldo por lá.''')
seis = input('Resposta 6: ').strip().lower()[0]
while seis not in 'abcd':
    print('\033[31mERROR\033[m')
    seis = input('Resposta 6: ').strip().lower()[0]
print('7. Como sua empresa distribui o manual de cultura, política e normas internas?')
print('''a) Não temos esse material.
b) Imprimimos e distribuímos individualmente.
c) Mandamos por e-mail.
d) Mantemos em um portal interno.''')
sete = input('Resposta 7: ').strip().lower()[0]
while sete not in 'abcd':
    print('\033[31mERROR\033[m')
    sete = input('Resposta 7: ').strip().lower()[0]
print('8. Na sua empresa, como é feita a gestão de benefícios corporativos?')
print('''a) Internamente, temos uma pessoa que faz esta função além de outras funções administrativas.
b) Temos uma pessoa dedicada a fazer este processo.
c) Fazemos a terceirização e gerenciamos os benefícios por uma plataforma.
d) Oferecemos o Beneflex (benefícios flexíveis).''')
oito = input('Resposta 8: ').strip().lower()[0]
while oito not in 'abcd':
    print('\033[31mERROR\033[m')
    oito = input('Resposta 8: ').strip().lower()[0]
print('9. Como a sua empresa aplica a avaliação de desempenho?')
print('''a) Não realizamos avaliação de desempenho.
b) Fazemos por meio de planilhas de Excel.
c) Fazemos por meio de formulários online.
d) Realizamos por meio de uma ferramenta de avaliação de desempenho.''')
nove = input('Resposta 9: ').strip().lower()[0]
while nove not in 'abcd':
    print('\033[31mERROR\033[m')
    nove = input('Resposta 9: ').strip().lower()[0]
print('10. Como você melhor descreve a área de cargos e salários da sua empresa?')
print('''a) Não temos uma política de cargos e salários.
b) Todos os processos são feitos e controlados em uma planilha.
c) Todos os processos são feitos e controlados em uma planilha.
d) Temos um software de cargos e salários que equipara os cargos e a empresa ao mercado.''')
dez = input('Resposta 10: ').strip().lower()[0]
while dez not in 'abcd':
    print('\033[31mERROR\033[m')
    dez = input('Resposta 10: ').strip().lower()[0]
print(list)

if um == 'a':
    um = 2
if um == 'b':
    um = 1
if um == 'c':
    um = 3
if um == 'd':
    um = 4
if dois == 'a':
    dois = 1
if dois == 'b':
    dois = 3
if dois == 'c':
    dois = 2
if dois == 'd':
    dois = 4
if tres == 'a':
    tres = 1
if tres == 'b':
    tres = 3
if tres == 'c':
    tres = 2
if tres == 'd':
    tres = 4

soma = um + dois + tres + quatro + cinco + seis + sete + oito + nove + dez
print(soma)
