def validador(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! {entrada} é um preço inválido')
        else:
            ok = True
            return float(entrada)


def leiaint(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! Digite um numero inteiro válido\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada Interrompida\033[m')
            return ''
        else:
            return f'Você digitou o inteiro {inteiro}'


def leiafloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! Digite um numero real válido\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada Interrompida\033[m')
            return ''
        else:
            return f'Você digitou o inteiro {real}'


def menu(msg):
        print('~' * 50)
        print(f'{"MENU PRINCIPAL" : ^50}')
        print('~' * 50)
        print('1 - Cadastrar Pesooas')
        print('2 - Ver Pesooas Cadastradas')
        print('1 - Sair do Sistema')
        print('~' * 50)
        opc = leiaint(msg)
        return opc
            if msg.isnumeric():

        except (TypeError, ValueError):
            print(f'ERRO! Digite uma das opções')