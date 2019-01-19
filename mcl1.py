import numpy as np
from scipy.misc import imread, imsave, imresize
import pygame
from pygame.locals import *
from Fonctions import *

#import image


rep="/Users/olivierpartensky/Desktop/Image considérée/"
ele="Marc avec un casque.jpg"

img=imread(rep+ele)
shape=list(img.shape)
shapem=list(img.shape)
shapem=tuple(shapem[:2])
shaper=list(shapem)
shaper.reverse()
shaper=tuple(shaper)
#shaper.reverse()
#print(np.s.randint(0,3,(2,2)))

layer1=np.full(shapem,None)
#print(layer1.shape)

for x in range(shaper[0]):
    for y in range(shaper[1]):
        layer1[y][x]=img[y][x][0]*255**2+img[y][x][1]*255+img[y][x][2]
        Progression(x,0,shaper[0])
        
        
#print(len(layer1))
weight1=np.random.random(shaper)
layer2=layer1.dot(weight1)
result=np.full(shape)

for x in range(shaper[0]):
    for y in range(shaper[1]):
        result[y][x][0]=layer2[y][x]%256
        result[y][x][1]=layer2[y][x]%(256**2)//256
        result[y][x][0]=layer2[y][x]//256

def show(img):
    pygame.init()
    size=list(img.shape[:2])
    size.reverse()
    screen = pygame.display.set_mode(tuple(size))
    pygame.display.set_caption("Picture")
    for y in range(shape[0]):
        for x in range(shape[1]):
            pygame.draw.rect(screen, img[y][x], (x,y,1,1), 0)
    pygame.display.flip()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == KEYDOWN:
                done = True
    pygame.quit()

            
show(result)
