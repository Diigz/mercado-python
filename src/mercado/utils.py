import os
import time
import re

carrinho = []


def home():
    os.system('cls')

    print('''
    ██████╗░███████╗███╗░░░███╗  ██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░  ░█████╗░░█████╗░
    ██╔══██╗██╔════╝████╗░████║  ██║░░░██║██║████╗░██║██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗
    ██████╦╝█████╗░░██╔████╔██║  ╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║  ███████║██║░░██║
    ██╔══██╗██╔══╝░░██║╚██╔╝██║  ░╚████╔╝░██║██║╚████║██║░░██║██║░░██║  ██╔══██║██║░░██║
    ██████╦╝███████╗██║░╚═╝░██║  ░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝  ██║░░██║╚█████╔╝
    ╚═════╝░╚══════╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░  ╚═╝░░╚═╝░╚════╝░

    ███╗░░░███╗███████╗██████╗░░█████╗░░█████╗░██████╗░░█████╗░  ██╗
    ████╗░████║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██║
    ██╔████╔██║█████╗░░██████╔╝██║░░╚═╝███████║██║░░██║██║░░██║  ██║
    ██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██╗██╔══██║██║░░██║██║░░██║  ╚═╝
    ██║░╚═╝░██║███████╗██║░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝  ██╗
    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░  ╚═╝\n''')

    print('1. Adicionar itens no carrinho.')
    print('2. Visualizar carrinho de compras.')
    print('3. Deletar itens do carrinho.')
    print('4. Finalizar compras.\n')

    try_selector()


def try_selector():
    while True:
        try:
            selecionador = int(input('O que deseja realizar hoje: '))
            match selecionador:
                case 1:
                    cleaner()
                    add_cart()
                    break
                case 2:
                    cleaner()
                    view_cart()
                    break
                case 4:
                    print('\nObrigado por utilizar o aplicativo ^-^')
                    time.sleep(1.0)
                    break
        except:
            print('\nPor favor, preencha o campo corretamente !')
            time.sleep(2.0)
            home()
            break


def clean_home():
    input('\nPressione qualquer tecla para limpar a tela...')
    os.system('cls' if os.name == "nt" else "clear")
    home()


def cleaner():
    os.system('cls' if os.name == "nt" else "clear")


def add_cart():
    print('''
░█████╗░░█████╗░██████╗░██████╗░██╗███╗░░██╗██╗░░██╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██║░░██║██╔══██╗
██║░░╚═╝███████║██████╔╝██████╔╝██║██╔██╗██║███████║██║░░██║
██║░░██╗██╔══██║██╔══██╗██╔══██╗██║██║╚████║██╔══██║██║░░██║
╚█████╔╝██║░░██║██║░░██║██║░░██║██║██║░╚███║██║░░██║╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░\n''')
    print('Bem vindo(a)! Você está no carrinho agora.\n')
    while True:
        try:
            itens = input(
                'Insira o seu(s) produto(s): ')
            if not itens:
                print(
                    'Você inseriu nada no carrinho, portanto será redirecionado ao menu principal.')
                home()
                break
            else:
                lista = re.split(r',\s*|\s+e\s+', itens)
                lista = [l.strip() for l in lista if l.strip()]
                carrinho.extend(lista)
                print('\n Carrinho preenchido com sucesso...')
                time.sleep(2.0)
                home()
                break
        except Exception as e:
            print(
                f'Foi encontrado um erro inesperado: {e}, iremos trabalhar para que isso não ocorra novamente.')
            time.sleep(2.0)


def view_cart():
    print('''
░█████╗░░█████╗░██████╗░██████╗░██╗███╗░░██╗██╗░░██╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██║░░██║██╔══██╗
██║░░╚═╝███████║██████╔╝██████╔╝██║██╔██╗██║███████║██║░░██║
██║░░██╗██╔══██║██╔══██╗██╔══██╗██║██║╚████║██╔══██║██║░░██║
╚█████╔╝██║░░██║██║░░██║██║░░██║██║██║░╚███║██║░░██║╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░\n''')

    print('Visualização do carrinho: \n')

    contagem = 0
    for c in carrinho:
        contagem += 1
        print(f'{contagem}° {c}.\n')
        clean_home()
