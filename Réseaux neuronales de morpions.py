#------#
#Import#
#------#

from Fonctions import *
import random

#---------#
#Variables#
#---------#


board=[None]*9


#---------#
#Fonctions#
#---------#

def neural_board(board):
    neural_board=[[0]*3]*9
    for i,v in enumerate(board):
        if v==None:
            neural_board[i][0]=1
        if v=="X":
            neural_board[i][1]=1
        if v=="O":
            neural_board[i][2]=1
    return neural_board

def print(Grille,Bool=False):
    g=Grille[:]
    pygame.init()
    s=(500,500)
    screen = pygame.display.set_mode(s)
    pygame.display.set_caption("Morpions")
    screen.fill((0,0,0))
    tx,ty=(s[0]/3,s[1]/3)
    p=5
    q=[tx//3,ty//3]
    for i in range(9):
        x=i%3*tx
        y=i//3*ty
        pygame.draw.rect(screen, (255,255,255), (x+p,y+p,tx-p,ty-p), 0)
        if g[i]==None:
            pygame.draw.rect(screen, (255,255,255), (x+q[0],y+q[1],q[0],q[1]), 0)
        if g[i]==0:
            pygame.draw.rect(screen, (0,0,255), (x+q[0],y+q[1],q[0],q[1]), 0)
        if g[i]==1:
            pygame.draw.rect(screen, (255,0,0), (x+q[0],y+q[1],q[0],q[1]), 0)
    pygame.display.flip()
    done=False
    while not done and Bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
    if Bool:
        pygame.quit() 

class neural_network:
    def __init__(self):
        self.neural_network=[[random.random()]*27]*27
    def save():
        StockerVariable(self.neural_network,"Morpions neural_network","w")
    def get():
        self.neural_network=SortirVariable("Morpions neural_network")[0]
    def process():
        neural_network=self.neural_network
        for i,layer in enumerate(neural_network):
            
            
    
    

#-------#
#Actions#
#-------#
