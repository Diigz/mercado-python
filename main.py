# Aplicativo em manutenção !!
# Falta estruturar e muito mais...

import os
import time

def menu_principal():
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

    print('Escolha o que deseja fazer agora !\n')

    print('1. Adicionar itens no carrinho.')
    print('2. Visualizar lista de compras.')
    print('3. Deletar item do carrinho.')
    print('4. Finalizar compras.\n')
def retornar_menu():        
    retornar = input('\nPressione qualquer tela para retornar ao menu.')
    if retornar == ' ':
        menu_principal()
    else:
        menu_principal()

carrinho = []
menu_principal()
escolha_menu = int(input('Escolha sua opção aqui: '))

#---------------------- Lógica do Programa -----------------------------#

match escolha_menu:
    case 1:
        os.system('cls')
        print('Você está no carrinho agora...')
        itens = input('Insira o que deseja comprar hoje! Separe os produtos somente com virgulas: ')
        produtos = [i.strip() for i in itens.split(',') if i.strip()]
        carrinho.extend(produtos)

        print('\nPerfeito! Você escolheu os seguintes produtos:')
        for i, p in enumerate(produtos, start=1):
            print(f'{i}. {p}.')
        retornar_menu()


