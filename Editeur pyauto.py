#------#
#Import#
#------#

from pygame.locals import *
import pygame
#import autogui

#---------#
#Variables#
#---------#

BLACK   = (  0,  0,  0)
BLUE    = (  0,  0,255)
RED     = (255,  0,  0)
YELLOW  = (255,255,  0)
WHITE   = (255,255,255)
import pyautogui
screenWidth, screenHeight = pyautogui.size()

def edit(board=[[BLACK for i in range(50)] for j in range(50)]):
    v,b,n=WHITE
    COLOR=[v,b,n]
    x,y=(0,0)
    coordonates=[x,y]
    pygame.init()
    size=(500,500)
    tx,ty=(10,10)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Puissance 4")
    done=False
    try:
        while not done:
            for _x in range(len(board)):
                for _y in range(len(board[_x])):
                    pygame.draw.rect(screen, board[_y][_x], (_x*tx,_y*ty,tx-1,ty-1), 0)

            pygame.draw.rect(screen, COLOR, (x*tx,y*ty,tx-1,ty-1), 0)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x=int(event.pos[0]//tx)
                    y=int(event.pos[1]//ty)
    
                if event.type == KEYDOWN:
                    if event.key == pygame.K_DOWN and y<size[1]:
                        y+=10
                    if event.key == pygame.K_UP and y>0:
                        y-=10
                    if event.key == pygame.K_LEFT and x>0:
                        x-=10
                    if event.key == pygame.K_RIGHT and x<size[0]:
                        x+=10
                    if event.key == pygame.K_v:
                        v=(v+10)%256
                    if event.key == pygame.K_v:
                        b=(b+10)%256
                    if event.key == pygame.K_n:
                        n=(n+10)%256
                            
 
    finally:
        pygame.quit()

#-------#
#Actions#
#-------#

edit()
