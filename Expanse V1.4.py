#-----------#
#Importation#
#-----------#

import numpy as np
import pygame
from pygame.locals import *
import os
import random
import tkinter

#os.chdir("/Users/olivierpartensky/Desktop/Base De Données Perso/")

from Fonctions import *


#--------#
#Stockage#
#--------#


rep="/Users/olivierpartensky/Desktop/Expanse/Versions/1.4/"
os.chdir(rep+"General")

#Couleurs#

DefaultColors={"BLACK":  (  0,  0,  0),
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

cl=TryOut("Colors",DefaultColors)
cll=[value for value in cl.values()]

#Boite#

pygame.init()
info = pygame.display.Info()
w=info.current_w
h=info.current_h
pygame.quit()

DefaultBoite={"session":0,"screen size":(w,h),
              "block made":0,"block edited":0,"block saved":0,
              "map made":0,"map edited":0,"map saved":0,
              "player made":0,"player edited":0,"player saved":0,
              "map made":0
              }

b=TryOut("Boite",DefaultBoite)
b["session"]+=1






#--------------------#
#Classes et Fonctions#
#--------------------#

#---------#
#Fonctions#
#---------#

def Save():
    os.chdir(rep+"General")
    StockerVariable(b,"Boite","w")

def Quit():
    Save()
    quit()

def Out(nom_objet,type_objet):
    n=nom_objet
    t=type_objet
    t=t.lower()
    t=ExpanseSelect(t,["block","map","player"])
    t=t[0].upper()+t[1:]
    nrep=rep+t+"s"
    os.chdir(nrep)
    n=ExpanseSelect(n,os.listdir(nrep))
    att=SortirVariable(n)[0]
    if t=="Block":
        ob=Block()
    if t=="Map":
        ob=Map()
    if t=="Player":
        ob=Player()
    ob.__dict__=att
    return ob

def fit(map_position,view_field,map_field):
    p=map_position
    v=view_field
    m=map_field
    view=(p-v//2,p+v//2)
    if p-v//2<0:
        view=(0,v-1)
    if p+v//2>m:
        view=(m-v,m)
    return view
    


#-------#
#Classes#
#-------#

#Block#

class Block:
    def __init__(self,name="Unknown",size=(10,10)):
        b["block made"]+=1
        self.made=b["block made"]
        self.name=name
        self.size=size
        self.block=[[None for i in range(size[0])] for j in range(size[1])]

    def edit1(self):
        b["block edited"]+=1
        self.edited=b["block edited"]
        m=min(list(b["screen size"]))
        S=b["screen size"]
        s=self.size
        tx=S[0]/s[0]
        ty=S[1]/s[0]
        bx=int(s[0]//2)
        by=int(s[1]//2)
        bcl=0
        t=False
        pygame.init()
        screen = pygame.display.set_mode(S,FULLSCREEN)
        pygame.display.set_caption("Editing - "+self.name)
        
        done = False
        try:
            while not done:
                for y in range(s[1]):
                    for x in range(s[0]):
                        pygame.draw.rect(screen, self.block[y][x], (x*tx,y*ty,tx,ty), 0)
                pygame.draw.rect(screen, cll[bcl], (bx*tx,by*ty,tx,ty), 0)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done=True
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        bx=int(event.pos[0]//tx)
                        by=int(event.pos[1]//ty)
                        
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_DOWN and by<s[1]:
                            by+=1
                        if event.key == pygame.K_UP and by>0:
                            by-=1
                        if event.key == pygame.K_LEFT and bx>0:
                            bx-=1
                        if event.key == pygame.K_RIGHT and bx<s[0]:
                            bx+=1
                        if event.key == pygame.K_x:
                            bcl=(bcl+1)%len(cll)
                        if event.key == pygame.K_w:
                            bcl=(bcl+len(cll)-1)%len(cll)
                        if event.key == pygame.K_c:
                            bcl=cll.index(self.block[by][bx])
                        if event.key == K_SPACE:
                            self.block[by][bx]=cll[bcl]
                        if event.key == K_RETURN:
                            if t==False:
                                t=True
                                bxm=bx
                                bym=by
                                self.block[by][bx]=cll[bcl]
                            else:
                                t=False
                                bxi=min(bxm,bx)
                                bxf=max(bxm,bx)
                                byi=min(bym,by)
                                byf=max(bym,by)
                                for y in range(byi,byf+1):
                                    for x in range(bxi,bxf+1):
                                        self.block[y][x]=cll[bcl]
                        if event.key == K_ESCAPE:
                            done=True
        finally:
            pygame.quit()

    def edit(self):
        b["block edited"]+=1
        self.edited=b["block edited"]
        m=min(list(b["screen size"]))
        S=b["screen size"]
        s=self.size
        tx=S[0]/s[0]
        ty=S[1]/s[0]
        bx=int(s[0]//2)
        by=int(s[1]//2)
        c=[0,0,0]
        p=32
        t=False
        event_liste=[]
        pygame.init()
        screen = pygame.display.set_mode(S,FULLSCREEN)
        pygame.display.set_caption("Editing - "+self.name)
        
        done = False
        try:
            while not done:
                for y in range(s[1]):
                    for x in range(s[0]):
                        cb=self.block[y][x]
                        if cb!=None:
                            pygame.draw.rect(screen, cb, (x*tx,y*ty,tx,ty), 0)
                        else:
                            pygame.draw.rect(screen, (30,30,30), (x*tx,y*ty,tx,ty), 0)
                            pygame.draw.rect(screen, (0,0,0), (x*tx+2,y*ty+2,tx-4,ty-4), 0)
                if c!=None:
                    pygame.draw.rect(screen, (255,255,255), (bx*tx,by*ty,tx,ty), 0)
                    pygame.draw.rect(screen, c, (bx*tx+2,by*ty+2,tx-4,ty-4), 0)
                else:
                    pygame.draw.rect(screen, (255,255,255), (bx*tx,by*ty,tx,ty), 0)
                    pygame.draw.rect(screen, (0,0,0), (bx*tx+2,by*ty+2,tx-4,ty-4), 0)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done=True
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        bx=int(event.pos[0]//tx)
                        by=int(event.pos[1]//ty)
                        
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_DOWN and by<s[1]:
                            by+=1
                        if event.key == pygame.K_UP and by>0:
                            by-=1
                        if event.key == pygame.K_LEFT and bx>0:
                            bx-=1
                        if event.key == pygame.K_RIGHT and bx<s[0]:
                            bx+=1
                        if c!=None:
                            if event.key == pygame.K_q:
                                c[0]=(c[0]+p)%256
                            if event.key == pygame.K_s:
                                c[1]=(c[1]+p)%256
                            if event.key == pygame.K_d:
                                c[2]=(c[2]+p)%256
                            if event.key == pygame.K_a:
                                c[0]=(c[0]+256-p)%256
                            if event.key == pygame.K_z:
                                c[1]=(c[1]+256-p)%256
                            if event.key == pygame.K_e:
                                c[2]=(c[2]+256-p)%256
                        if event.key == K_w:
                            c=[0,0,0]
                        if event.key == K_x:
                            c=[255,255,255]
                        if event.key == pygame.K_c:
                            c=self.block[by][bx]
                        if event.key == K_SPACE:
                            if c!=None:
                                self.block[by][bx]=c[:]
                            else:
                                self.block[by][bx]=None
                        if event.key == 303:
                            c=None
                        if event.key == K_RETURN:
                            if t==False:
                                t=True
                                bxm=bx
                                bym=by
                                if c!=None:
                                    self.block[by][bx]=c[:]
                                else:
                                    self.block[by][bx]=None
                            else:
                                t=False
                                bxi=min(bxm,bx)
                                bxf=max(bxm,bx)
                                byi=min(bym,by)
                                byf=max(bym,by)
                                for y in range(byi,byf+1):
                                    for x in range(bxi,bxf+1):
                                        if c!=None:
                                            self.block[y][x]=c[:]
                                        else:
                                            self.block[y][x]=None
                        if event.key == K_ESCAPE:
                            done=True
                        event_liste.append(event.key)
        finally:
            pygame.quit()

    def save(self):
        b["block saved"]+=1
        os.chdir(rep+"Blocks")
        StockerVariable(self.__dict__,"id:"+str(b["block edited"])+" "+self.name,"w")
        Save()

#Map#

class Map():
    def __init__(self,block=Out("id:8","block"),name="Unknown",size=[500,500]):
        b["map made"]+=1
        self.made=b["map made"]
        self.name=name
        self.size=size
        self.edit_position=[0,0]
        self.play_position=[0,0]
        z=b["screen size"]
        r=z[0]/z[1]
        self.view_field=(int(20*r),20)
        s=size
        self.map=[[block for x in range(s[0])] for y in range(s[1])]
        t=Out("Maison","block")
        ts=t.size[:]
        for y in range(s[1]):
            for x in range(s[0]):
                r=random.randint(0,10)
                if r==0:
                    for yb in range(ts[1]):
                        for xb in range(ts[0]):
                            if t.block[yb][xb]!=None:
                                self.map[y][x].block[yb][xb]=t.block[yb][xb][:]

    def edit(self):
        b["map edited"]+=1
        self.edited=b["map edited"]
        s=self.size
        p=self.edit_position
        v=self.view_field
        vx=fit(p[0],v[0],s[0])
        vy=fit(p[1],v[1],s[1])
        z=b["screen size"]
        bs=self.map[0][0].size
        tx=z[0]/v[0]/bs[0]
        ty=z[1]/v[1]/bs[1]
        mb=self.map[p[1]][p[0]]
        m=[0,0]
        a=2
        #print(p,v,s)
        #print(tx,ty)

        pygame.init()
        screen = pygame.display.set_mode(z) #,FULLSCREEN
        pygame.display.set_caption("Editing - "+self.name)
        Perso=Out("Silouette","block")

        done=False        
        try:
            while not done:
                for y in range(v[1]):
                    for x in range(v[0]):
                        Y=int((vy[1]+vy[0])/2+(y-v[1]//2)/v[1]*(vy[1]-vy[0]))
                        X=int((vx[1]+vx[0])/2+(x-v[0]//2)/v[0]*(vx[1]-vx[0]))
                        Block=self.map[Y][X]
                        bs=Block.size
                        for yb in range(bs[1]):
                            for xb in range(bs[0]):
                                nx=x*bs[0]+xb
                                ny=y*bs[1]+yb
                                pygame.draw.rect(screen, self.map[Y][X].block[yb][xb], (nx*tx,ny*ty,tx+1,ty+1), 0)
                for yb in range(bs[1]):
                    for xb in range(bs[0]):
                        nx=m[0]+xb-vx[0] #+ p[0]
                        ny=m[1]+yb-vy[0] #+ p[1]
                        c=Perso.block[yb][xb]
                        if c!=None:
                            pygame.draw.rect(screen, c, (nx*tx,ny*ty,tx+1,ty+1), 0)
    
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done=True
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            done=True
                        if event.key == K_DOWN and p[1]<s[1]:
                            m[1]+=a
                        if event.key == K_UP and p[1]>0:
                            m[1]-=a
                        if event.key == K_LEFT and p[0]>0:
                            m[0]-=a
                        if event.key == K_RIGHT and p[0]<s[0]:
                            m[0]+=a
                        if event.key == K_w:
                            a=a+1
                        if event.key == K_x:
                            a=a-1
                    p=[int(m[0]/bs[0]),int(m[1]/bs[1])]
                    #print(m,p)
                    vx=fit(p[0],v[0],s[0])
                    vy=fit(p[1],v[1],s[1])
                    #self.map[p[1]][p[0]]=Out("tete petee","block")
                    #m=[p[0]-vx[0],p[1]-vy[0]]
                    #print(m,p,vx)
                    
                        #print(p,vx,vy)
        finally:
            pygame.quit()
                               
        
    def save(self):
        b["map saved"]+=1
        os.chdir(rep+"Maps")
        StockerVariable(self.__dict__,"id:"+str(b["map edited"])+" "+self.name,"w")
        Save()
    







        
#-------#
#Actions#
#-------#
map=Map()
map.edit()
