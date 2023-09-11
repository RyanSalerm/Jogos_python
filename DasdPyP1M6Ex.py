from random import choice
from os import system, name
from ValidarOpcoes import continuar

print('Bem vindo ao jogo: Pedra, Papel, Tesoura')
computador = 0
usuario = 0

while True:
    pro = [0, 1, 2]
    print(f'Computador: {computador}')
    print(f'Usuario: {usuario}')
    print('0 - Pedra, 1 - Papel, 2 - Tesoura')
    usu = continuar('=>', '012')
    com = choice(pro)

    if com == 0:
        print('O computador jogou Pedra.')
        if usu in '1':
            print('Você GANHOU!')
            usuario += 1
        if usu in '2':
            print('Você PERDEU!')
            computador += 1
    if com == 1:
        print('O computador jogou Papel.')
        if usu in '0':
            print('Você PERDEU!')
            computador += 1
        if usu in '2':
            print('Você GANHOU!')
            usuario += 1
    if com == 2:
        print('O computador jogou Tesoura')
        if usu in '0':
            print('Você GANHOU!')
            usuario += 1
        if usu in '1':
            print('Você PERDEU!')
            computador += 1

    cont = continuar('Deseja continuar [S/N]? ', 'SsNn')
    if cont in 'Nn':
        break
    else:
        system("cls" if name == "nt" else "clear")
