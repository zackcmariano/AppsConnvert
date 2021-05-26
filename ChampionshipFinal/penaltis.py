from random import randint
from time import sleep

class Time:
    def __init__(self, time, chute=False, defesa=False):
        self.time = time
        self.chute = chute
        self.defesa = defesa
    
    def chutar(self):
        if self.chute:
            print(f'{self.time} já chutou, agora é a vez do outro time!')
            return
        print(f'============ APITA O JUIZ, O {self.time} VAI CHUTAR ============')
        sleep(1)
        print(f'{self.time} Chutooooou...')
        self.chute = True
    

    def defender(self):
        if not self.chute:
            print(f'============ JUIZ APITOU AUTORIZANDO O {self.time} ============')
            sleep(1)
            print(f'{self.time} Chutooooou...')
            return

        print(f'Goleiro do {self.time} a caminho do gol para tentar essa defesa...')
        self.chute = False

