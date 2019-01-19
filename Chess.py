#------#
#Import#
#------#

import os
import pygame
from pygame.locals import *
from Fonctions import *


#---------#
#Variables#
#---------#

rep=rep_programme+"Chess"+"/"

#---------#
#Fonctions#
#---------#


class App:
    def __init__(self,new=False):
        if new:
            os.chdir(rep"Settings")
            self.settings={"background":BROWN,"computer":False,"intelligence":0}
            StockerVariable(Settings,"Settings","w")
        
        
            
            
            
        
        
            

class Game:
    def __init__(self):
        pawns=["knight","horse","bishop","tower","queen","king"]
        default_quick_board = [["tb","hb","bb","kb","qb","bb","hb","tb"],
                               ["wb","wb","wb","wb","wb","wb","wb","wb"],
                               [None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None],
                               ["ww","ww","ww","ww","ww","ww","ww","ww"],
                               ["tw","hw","bw","kw","qw","bw","hw","tw"]]
        

class Pawn:
    def __init__(self,type,color,position):
        self.color=color
        self.type=type
        self.position=position
    def move(board):
        self.move(self.board,self.position)
    def kill():
        a=1
    def die():
        a=1
        
class Warrior(Pawn):
    def __init__(self,color,position):
        moves="

        
    def show_moves(board):
        px,py=self.position
        b=board
        for y in range(8):
            for x in range(8):
                if self.color==BLACK and y==py : 
                    pygame.draw.rect(screen, GREEN, (x*cx,y*cy,cx-1,cy-1), 0)
        pygame.display.flip()
            
            
        

class Horse(Pawn):
    def __init__(self,position,board):
        do_stuff=1
        

class Player:
    def __init__(self,color):
        pawns=dict(pawns)
        deads=1
        

class board:
    def __init__(self,difficulty=0,window_size=(500,500),board_size=(8,8)):
        pygame.init()
        self.window_size=window_size
        self.board_size=board_size
        wz=window_size
        bz=board_size
        cx=wz[0]/bz[0]
        cy=wz[1]/bz[1]
        cz=(cx,cy)
        case_size=cz
        self.case_size=cz
        position=(0,0)
        px,py=position
        screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Chess")
        pygame.draw.rect(screen, BLACK, (0,0,wz[0],wz[1]), 0)
        self.board=[[None]*8]*8
        for y in range(bz[1]):
            for x in range(bz[0]):
                pygame.draw.rect(screen, (20, 10,  0), (x*cx,y*cy,cx-1,cy-1), 0)
        pygame.display.flip()

        quick_board = [["tb","hb","bb","kb","qb","bb","hb","tb"],
                       ["wb","wb","wb","wb","wb","wb","wb","wb"],
                       [None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None],
                       ["ww","ww","ww","ww","ww","ww","ww","ww"],
                       ["tw","hw","bw","kw","qw","bw","hw","tw"]]
        board=Chess.convert(quick_board)

    def convert(quick_board):
        quick_pawns = ["w","h","b","t","q","k"]
        quick_colors= ["b","w"]
        board=[[None]*bz[0]]*bz[1]
        qb=quick_board
        for y in range(bz[1]):
            for x in range(bz[0]):
                v=qb[y][x]
                if v!==None:
                    type=quick_pawns.index(v[0])
                    side=quick_colors.index(v[1])
                    board[y][x]=Pawn(type,side,(x,y))
        return board
                
    def print(self):
        for y in range(8):
            for x in range(8):
                pygame.draw.rect(screen, BROWN, (x*cx,y*cy,cx-1,cy-1), 0)
        pygame.draw.rect(screen, BLUE, (px*cx,py*cy,cx,cy), 0)
        pygame.display.flip()
        
        for column in self.board:
            for line in column:
                if self.board!=None:
                    print(self.board.print)
    def leave(self):
        pygame.quit()

#-------#
#Actions#
#-------#

Chess=Chess(True)
    
