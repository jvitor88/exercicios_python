from mysql.connector import connect
from classes_e_funcoes import *
import random


cabeca()
alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ltipo = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
ltipo2 = ['None', 'Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
lgen = [1, 2, 3, 4, 5, 6]
levo = ['Bebe', 'Basico', 'Estagio 1', 'Estagio 2']
# Variáveis de testes lógicos
respondeuLetra = False
respondeuTipo = False
respondeuGeracao = False
respondeuLendario = False
respondeuEvolucao = False
# Condição principal
while True:
    if respondeuGeracao == False:
        geracao = random.choice(lgen) #3
        resposta = input(f'Seu pokemon é da {geracao}ª geração? [S/N]: ').strip().lower()[0]
        if resposta == 's':
            respondeuGeracao = True
        if resposta == 'n':
            lgen.remove(geracao)
    if respondeuLetra == False:
        letra = random.choice(alfa)
        resposta = input(f'Seu pokemon começa com a letra {letra}? [S/N]:  ').strip().lower()[0]
        if resposta == 's':
            respondeuLetra = True
        if resposta == 'n':
            alfa.remove(letra)
    if respondeuTipo == False:
        tipo = random.choice(ltipo)
        resposta = input(f'O tipo principal do seu pokemon é {tipo}? [S/N]: ').strip().lower()[0]
        if resposta == 's':
            respondeuTipo = True
        if resposta == 'n':
            ltipo.remove(tipo)
    if respondeuLendario == False:
        resposta = input(f'Seu Pokemon é Lendário? [S/N]: ').strip().lower()[0]
        if resposta == 's':
            lend = 1
        if resposta == 'n':
            lend = 0
        respondeuLendario = True
    if respondeuEvolucao == False:
        evo = random.choice(levo)
        resposta = input(f'A evolução seu Pokemon está no {evo}? [S/N]: ').strip().lower()[0]
        if resposta == 's':
            respondeuEvolucao = True
        if resposta == 'n':
            levo.remove(evo)
    if respondeuLetra == True and respondeuTipo == True and respondeuEvolucao == True and respondeuGeracao == True and respondeuLendario == True:
        break

def respondeu(resposta, lista, escolha):
    if resposta == 'n':
        lista.remove(escolha)
        return False
    return True

# Conexão ao banco
conexao = connect(
    passwd='root',
    port=3306,
    user='root',
    host='localhost',
    database='mundo_pokemon'
)

# Query
sql = f'''select * from base_pokemons
where P_LETRA = '{letra}' and
TYPE_1 = '{tipo}' and
GERACAO = '{geracao}' and
EST_EVOL = '{evo}' and
LENDARIO = '{lend}';
'''

cursor = conexao.cursor()
cursor.execute(sql)

# Resultado da query
pokemon = cursor.fetchall()[0]

conexao.close()

linha()
# Selecionando a informação a ser mostrada na tela
nome = pokemon[1]

print(f'Você está pensando no {nome}?')
# Finalização
final = input('SIM OU NÃO? ').strip().lower()[0]
if final == 's':
    print('OBRIGADO VOLTE SEMPRE!')
else:
    print('DESCULPE, TENTE NOVAMENTE...')