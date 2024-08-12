import random

def p1():
    get == random.randint(1,3)
    print(get)
    
def escolha():
    p1()
    escolha_player = int(input('escolha uma opção: '))
    if p2 == escolha_player:
        print('voce acertou, parabens')
    else:
        print('voce errou, tente novamente')

print('Bem vindo ao jogo do pedra, papel e tesoura')
print('escolha uma opção')
print('1 = pedra')
print('2 = tesoura')
print('3 = papel')

p1()
escolha()
