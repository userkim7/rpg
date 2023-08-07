import random
import copy
import os
import time
import msvcrt
import re
import pickle

#□■▣▩▦◈⊙Ξ▤▥▧▨⬚⛋⚿
#☒⌧◆◇◎●▲△▼▽☖☗⛉⛊☰☱☲☳☴☵☶☷▀▁▂▃▄▅▆▇█▉▊▋▌▍▎✪
#┻┣┫┏┓╋┃
#┏┳┓
#┣╋┫
#┗┻┛

#□■▣▩▦◈⊙Ξ▤▥▧▨⬚⛋⚿
''' #0 wasd
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

    def roll(self,dice): #0 [face]d[num]
        dice=list(map(int,dice.split('d')))
        return [random.randint(1,dice[0]) for i in range(dice[1])]

    def move(self,direction): #1 in map movement by direction
        pass

    def set_bar(self,stat,Num):
        if Num<0: pass #1 return ?
        else:
            return '█'*(Num//7)+['','▎','▍','▌','▋','▊','▉'][Num%7]

    def select_option(self,options,descriptions):
        buttons=['▣']+['□']*(len(options)-1)
        Num=0
        while True:
            key=msvcrt.getch()
            if key=='\xe0':
                key=msvcrt.getch()
            elif key==b'\r':
                break
        if key==b'H': 
            if Num>0:
                Num-=1
        elif key==b'P':
            if Num<len(options):
                Num+=1
        buttons.remove('▣')
        buttons.insert(Num,'▣')
        
        for Index,button in enumerate(buttons):
            if descriptions:
                print(button+self.print_option(options[Index],descriptions[Index]))
            else:
                print(button+self.print_option(options[Index],False))
    
    def print_option(self,option,description):
        if description:
            return option+'\n┗'+description
        else:
            return option

class Setting: #0 game set
    def __init__(self):
        self.saved_datas=[] #0 [[name],[lv nickname]]

    def before_start(self):
        while True:
            user=input('Load Save?...(Y/N)')
            if re.match('(?i)y|n',user) and len(user)==1:
                if re.match('(?i)y',user):
                    self.load_data()
                    break
            else:
                print('Incorrect Input')

    def load_data(self):
        if self.saved_datas:
            file_name=funtion.select_option(self.saved_datas[0],self.saved_datas[1]) #0 option:name description:lv,nickname
            try:
                with open(f'{file_name}.pickle','rb') as f:
                    self.loaded_data=pickle.load(f) #1 input loaded data
            except:
                print(f"No Save Named '{file_name}' Founded")
                self.delete_save(file_name)
                self.load_data()
        else:
            print('No Save Founded')
            self.loaded_data={}

    def delete_save(self,name):
        Index=self.saved_datas[0].index(name)
        del self.saved_datas[0][Index]
        del self.saved_datas[1][Index]

    def random_stat(self): #0 if first: set character_stat #1 randclass randstats on square probability distribution
        pass

class Main: #0 game backend
    def __init__(self):
        pass

    def get_movement(self): #0 
        if key=='\xe0':
            key=msvcrt.getch()
        funtion.move(['up','left','down','right'][[b'H',b'K',b'P',b'M'].index(key)])
        

class Game: #0 game frontend
    def __init__(self):
        pass

class Event: #0 game event
    def __init__(self):
        pass

class Player: #0 character overall
    def __init__(self): #0 stats
        self.hp=100
        self.mp=50

        self.strength=3 #0 sp True
        self.defence=3
        self.agility=3
        self.wisdom=3
        self.dexterity=3
        self.luck=3
        
        self.critical=150 #0 sp False
        self.critical_rate=5

        self.attack_resistance=0
        self.fire_resistance=0
        self.poison_resistance=0
        self.magic_resistance=0

        self.fame=0
        self.credit=50

        self.level=1
        self.exp=0
        self.gold=1000


#############
function=Function() #0 set
main=Main()

setting=Setting()
game=Game()
event=Event()
player=Player()
