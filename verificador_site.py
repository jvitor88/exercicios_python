from time import sleep
import urllib.request

site = input('Digite uma url: ')
while True:
    if 'https://' in site:
        try:
            site1 = urllib.request.urlopen(site)
            print('\033[32mO site está acessível\033[m')
            sleep(3)
        except urllib.request.URLError:
            print('\033[31mO site NÃO está acessível\033[m')
            sleep(3)
        except KeyboardInterrupt:
            print('Obrigado! Volte Sempre')
            break
    else:
        try:
            site2 = urllib.request.urlopen(f'https://{site}')
            print('\033[32mO site está acessível\033[m')
            sleep(3)
        except urllib.request.URLError:
            print('\033[31mO site NÃO está acessível\033[m')
            sleep(3)
        except KeyboardInterrupt:
            print('Obrigado! Volte Sempre')
            break
