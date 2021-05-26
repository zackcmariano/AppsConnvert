from random import randint
from penaltis import Time
from time import sleep

print('============== FINAL NOS PENALTIS ==============')
TIME = (input(str('ESCOLHA O PRIMEIRO TIME A BATER OS PÊNALTIS: ')))
print('================================================')
TIME2 = (input(str('ESCOLHA O SEGUNDO TIME A BATER OS PÊNALTIS: ')))
print('================================================')
CHUTES = {TIME: randint(1, 6)}


def cobrancas():
    tot4 = 0
    for TIME, CHUTE in CHUTES.items():
        if CHUTE == 1:
            print('Gooooool... Que Golaço no canto esquerdo')
            print('=*'*30)
        if CHUTE == 2:
            print('Que Golaaaaaaço inacreditável')
            print('=*'*30)
        if CHUTE == 3:
            print('É Gooooool... debaixo das pernas do goleiro')
            print('=*'*30)
        if CHUTE == 4:
            print('Gooool, que golaço no angulo')
            print('=*'*30)
        if CHUTE <= 4:
           tot4 += 1

def cobrancas_2():
    for TIME, CHUTE in CHUTES.items():
        if CHUTE == 5:
            print('Praaa foooora... Agora a situação do Time está complicada!')
            print('=-'*30)
        if CHUTE == 6:
            print('Peeeerdeu o penaulti, o Goleiro defendeeeu!')
            print('=-'*30)

def execut():
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('.....')
    sleep(0.5)
    cobrancas()
    cobrancas_2()

def main():
    while True:
        TIMES = TIME
        TIMED = TIME2
        TIME_1 = Time(TIME)
        TIME_2 = Time(TIME2)
        print('==========================================================')
        jogador = int(input('Escolha um Time para Chutar: [ 1 ] {} [ 2 ] {} : '.format(TIMES, TIMED)))
        sleep(0.5)
        if jogador == 1:
            TIMEC = TIME_1.chutar()
            return TIMEC
        if jogador == 2:
           TIMEV = TIME_2.chutar()
           return TIMEV


'''A FINAL DO CAMPEONATO É DISPUTADA COM MUITA GARRA, MAS AMBOS OS TIMES TEM A CHANCE DE SER CAMPEÃO. 
A PROBABILIDADE DE FAZER GOL É DE 66% AGORA É TORCER PARA O ADVERSÁRIO TER A MAIOR TAXA DOS 44%'''



if __name__=='__main__':
    main()
    sleep(0.5)
    execut()