import numpy as np
from scipy.misc import imread, imsave, imresize
import pygame
from pygame.locals import *

class Player:
    made=0
    def __init__(self,name=str(made),Map):
        self.name=name
        self.map=Map
        self.position=Map.spawn
        self.screen=(1000,700)
        self.minssize=(5,5)

    def locate(self):
        pygame.init()
        s=self.size

        screen = pygame.display.set_mode(s)
        pygame.display.flip()
        sm=self.map.size
        sb=self.map.bsize

        bssize=((self.minssize[1]*2)*bsize[1],(self.minssize[0]*2)*bsize[0])

        p=self.position
        pym=self.screen[1]//bssize[1]
        pxm=self.screen[0]//bssize[0]
        bsize=
        
        for ym in range(p-pym,p+pym):
            for xm in range(p-pxm,p+pxm):
                for yb in range(b-):
                    for xb in range(sb[0]):
                        
                        
    

class Box:
    made=0
    def __init__(self,size=(5,5),sub=(0,0,0),name=str(made)):
        self.name=name
        self.sub=sub
        self.made=Box.made
        self.size=size
        form=list(size)+[len(sub)]
        self.box=np.full(form,sub)
        #def show():

    def show(self):
        pygame.init()
        s=self.size
        screen = pygame.display.set_mode(s)

        pygame.display.flip()
        done=False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == KEYDOWN:
                    done = True
        pygame.quit()
    

def shows(box,t,p):
    if box.type==Pixel:
    for y in range(t[0]):
        for x in range(t[1]):
            pygame.draw.rect(screen, self.box[y][x], (p[0]+x*t[0],p[1]+y*t[1],1,1), 0)
    
