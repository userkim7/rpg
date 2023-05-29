import random
import copy
import os
import time
import msvcrt

#□■▣▩▦◈⊙Ξ▤▥▧▨⬚⛋⚿
#☒⌧◆◇◎●▲△▼▽☖☗⛉⛊☰☱☲☳☴☵☶☷▀▁▂▃▄▅▆▇█▉▊▋▌▍▎✪
#┻┣┫┏┓╋┃

#############

#□■▣▩▦◈⊙Ξ▤▥▧▨⬚⛋⚿
''' #asdf
b'\xe0'
b'H'
b'\xe0'
b'K'
b'\xe0'
b'P'
b'\xe0'
b'M'
'''

#############

class Function:
    def __init__(self):
        pass

    def roll(self,dice):
        dice=list(map(int,dice.split('d')))
        return [random.randint(1,dice[0]) for i in range(dice[1])]

    def move(self,direction):
        pass

    def set_bar(self,stat,Num):
        if False: pass
        else:
            return '█'*(Num//7)+['','▎','▍','▌','▋','▊','▉'][Num%7]

class Setting:
    def __init__(self):
        pass

    def random_stat(self):
        pass

class Main:
    def __init__(self):
        pass

    def get_movement(self):
        if key=='\xe0':
            key=msvsct.getch()
        funtion.move(['up','left','down','right'][[b'H',b'K',b'P',b'M'].index(key)])
        

class Game:
    def __init__(self):
        pass

class Event:
    def __init__(self):
        pass

class Player:
    def __init__(self):
        self.hp=100
        self.mp=50

        self.strength=3
        self.defence=3
        self.agility=3
        self.wisdom=3
        self.dexterity=3
        self.luck=3
        
        self.critical=150
        self.critical_rate=5
        self.resistance=1

        self.fame=0
        self.credit=50

        self.level=1
        self.exp=0
        self.gold=1000


#############
function=Function()
main=Main()

setting=Setting()
game=Game()
event=Event()
player=Player()
