#-----------#
#Importation#
#-----------#

from Fonctions import *
import pygame
from pygame.locals import *
import pickle

#-------#
#Mémoire#
#-------#

rep="/Users/olivierpartensky/Desktop/Programme/GitHub/python_projects/Expanse/Version 1.1"

def Init():
    
    #COLORS#
    COLORS=SortirVariable(rep+"COLORS")
    try:
        COLORS=COLORS[0]
    except:
        COLORS={"made":0,
                "colors":{
                            "BLACK":  (  0,  0,  0),
                            "WHITE":  (255,255,255),
                            "RED":    (255,  0,  0),
                            "GREEN":  (  0,255,  0),
                            "BLUE":   (  0,  0,255),
                            "CYAN":   (  0,255,255),
                            "PURPLE": (255,  0,255),
                            "YELLOW": (255,255,  0),
                            "BROWN":  (150, 75,  0),
                            "ORANGE": (255,140,  0),
                            "CRANDOM":(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                            }
                }
        CLS=[value for value in COLORS["colors"].values()]
        print("COLORS initialisé")

    #BLOCKS#
    BLOCKS=SortirVariable(rep+"BLOCKS")
    try:
        BLOCKS=BLOCKS[0]
    except:
        BLOCKS={"made":0,
                "blocks":{}
                }
        print("BLOCKS initialisé")

    #MAPS#
    MAPS=SortirVariable(rep+"MAPS")
    try:
        MAPS=MAPS[0]
    except:
        MAPS={"made":0,
              "maps":{}
              }
        print("MAPS initialisé")
        

def Save():
    StockerVariable(BLOCKS,rep+"BLOCKS","w")
    StockerVariable(COLORS,rep+"COLORS","w")            

def Quit():
    Save()
    quit()

#------------#
#Organisation#
#------------#

"""

Organisation={"Name":None,
              "Author":"Marc Partensky",
              "Windows":
                  {"Menu":None,
                   "Maps":
                       {"Name":None,
                        "Square":"Pixels"
                        }
                   "Credits":None
                   }
              }

"""

#--------------------#
#Classes et Fonctions#
#--------------------#

class Editing:
    def __init__(self,ci=0,mx=100,my=50,bx=5,by=5):
        self.mci=ci
        self.mx=mx
        self.my=my
        self.bci=ci
        self.bx=bx
        self.by=by

class Map:
    made = 0
    def __init__(self,name,typ=0,value=None,tx=200,ty=100,size=5):
        self.version=1
        self.map=[[Square(typ,value) for x in range(tx)] for y in range(ty)]
        self.id=Map.made
        self.tx=tx
        self.ty=ty
        self.size=size
        self.value=value
        self.name=str(input("Nom: "))
        Map.made+=1
        

    def show(self):
        pygame.init()
        screen_size=(self.tx*self.size,self.ty*self.size)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Showing Mode")
        s=self.size
        print(s)
        for y in range(self.ty):
                for x in range(self.tx):
                    if self.map[y][x].typ==0:
                        pygame.draw.rect(screen, self.map[y][x].color, (x*s,y*s,s,s), 0)
                    if self.map[y][x].typ==1:
                        for yi in range(self.size):
                            for xi in range(self.size):
                                pygame.draw.rect(screen, BLOCKS[str(s)][self.value].block[yi][xi], (x*s+xi,y*s+yi,1,1), 0)

        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == KEYDOWN:
                    done = True
        pygame.quit()

        
    def edit(self):
        pygame.init()
        screen_size=(self.tx*self.size,self.ty*self.size)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Editing Mode")
        s=self.size
        for y in range(self.ty):
                for x in range(self.tx):
                    if self.map[y][x].typ==0:
                        pygame.draw.rect(screen, self.map[y][x].color, (x*s,y*s,s,s), 0)
                    if self.map[y][x].typ==1:
                        for yi in range(self.size):
                            for xi in range(self.size):
                                pygame.draw.rect(screen, BLOCKS[str(s)][self.value].block[yi][xi], (x*s+xi,y*s+yi,1,1), 0)
        pygame.display.flip()
        
        e=Editing()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    e.mx=event.pos[0]//s
                    e.my=event.pos[1]//s
                if event.type == pygame.K_UP and my<s-1:
                    e.my+=1
                if event.type == pygame.K_DOWN and my>0:
                    e.my-=1
                if event.type == pygame.K_LEFT and mx>0:
                    e.mx-=1
                if event.type == pygame.K_RIGHT and mx<s-1:
                    e.mx+=1
                if event.type == K_RETURN:
                    e.mci=(e.mci+1)%len(COLORS)
                if self.map[e.my][e.mx].typ==0:
                    self.map[e.my][e.mx]=Square(0,e.mci)
                    pygame.draw.rect(screen, COLORS[e.mci], (e.mx*s,e.my*s,s,s), 0)
            pygame.display.flip()
        pygame.quit()

    def save(self):
        StockerVariable(self,"Carte"+" "+self.name+" "+str(self.id),"w")
                

class Square:
    made=0
    def __init__(self,typ=0,value=0,size=5):
        self.value=value
        self.version=1
        self.typ=typ
        self.id=Square.made
        Square.made+=1
        if typ==0:
            self.color=COLORS[value]
        if typ==1:
            self.block=BLOCKS[str(size)][value]
        
        
class Block:
    made=0
    def __init__(self,name=str(BLOCKS["made"]),size=5,color=WHITE):
        BLOCKS["made"]+=1
        self.id=Block.made
        self.size=size
        self.name=name
        self.block=[[color for x in range(size)] for y in range(size)]
        Block.made+=1

    def show(self,sx=700,sy=700):
        size=self.size
        tx=sx//size
        ty=sy//size
        pygame.init()
        screen_size=(tx*size,ty*size)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Showing Mode")
        for y in range(size):
            for x in range(size):
                pygame.draw.rect(screen, self.block[y][x], (x*tx,y*ty,tx,ty), 0)
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                if event.type == KEYDOWN:
                    done = True
        pygame.quit()
                
    def edit(self,sx=700,sy=700):
        size=self.size
        tx=sx//size
        ty=sy//size
        pygame.init()
        screen_size=(tx*size,ty*size)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Editing Mode")
        for y in range(size):
            for x in range(size):
                pygame.draw.rect(screen, self.block[y][x], (x*tx,y*ty,tx,ty), 0)
        e=Editing()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    e.bx=event.pos[0]//tx
                    e.by=event.pos[1]//ty
                    
                if event.type == KEYDOWN:
                    if event.key == pygame.K_DOWN and e.by<size-1:
                        e.by+=1
                    if event.key == pygame.K_UP and e.by>0:
                        e.by-=1
                    if event.key == pygame.K_LEFT and e.bx>0:
                        e.bx-=1
                    if event.key == pygame.K_RIGHT and e.bx<size-1:
                        e.bx+=1
                    if event.key == pygame.K_n:
                        e.bci=(e.bci+1)%len(COLORS)
                    if event.key == K_RETURN:
                        self.block[e.by][e.bx]=COLORS[e.bci]
            for y in range(size):
                for x in range(size):
                    pygame.draw.rect(screen, self.block[y][x], (x*tx,y*ty,tx,ty), 0)
            pygame.draw.rect(screen, COLORS[e.bci], (e.bx*tx,e.by*ty,tx,ty), 0)
            pygame.display.flip()
        pygame.quit()
        
    def write(self,size,value):
        return Blocks.BLOCKS[str(size)][value]

    def save(self,size=5):
        BLOCKS[str(size)][self.name]=self.__dict__
        
    def saveappart(self):
        StockerVariable(self,rep+"Block: "+self.name,"w")


#-------#
#Actions#
#-------#



