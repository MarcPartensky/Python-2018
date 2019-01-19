#------#
#Import#
#------#

import os
from Fonctions import *
import time
import copy

#---------#
#Variables#
#---------#

Pions=["X","O"]
Premier=0
Joueur=0

Système=[9,8,7,6,5,4,3,2,1]
Partie=[0]*9

possibilités="103905"

#---------#
#Fonctions#
#---------#

def Win(Grille):
    g=Grille[:]
    v=0
    for i in range(0,9,3):
        if g[i]==g[i+1] and g[i+1]==g[i+2] and g[i]!=None:
            v=1
    for i in range(0,3):
        if g[i]==g[i+3] and g[i+3]==g[i+6] and g[i]!=None:
            v=1
    if g[0]==g[4]==g[8]!=None:
        v=1
    if g[2]==g[4]==g[6]!=None:
        v=1
    return v

def Griller(Partie):
    p=Partie[:]
    n=len(Partie)
    g=[None]*9
    j=0
    while not Win(g) and j<n:
        v=j%2
        #print(g)
        l=Indexes(None,g)
        #print(j)
        #print(p[j])
        #print(l[p[j]])
        #print(g[l[p[j]]])
        g[l[p[j]]]=v
        j+=1
    return g
    


def Gain(Partie):
    p=Partie[:]
    n=len(Partie)
    g=[None]*9
    j=0
    while not Win(g) and j<n:
        v=j%2
        l=Indexes(None,g)
        g[l[p[j]]]=v
        j+=1
    if j==n:
        return [0,0]
    return [int(v==0),int(v==1)]


def Implémenter1(Array,Arguments,Value):
    if len(Arguments)>0:
        a=Arguments[0]
        del Arguments[0]
        return Implémenter(Array[a],Arguments,Value)
    Array=Value
    print(len(Array))



def Implémenter(Arbre,Arguments,Value):
    l=[0]*(len(Arguments)+1)
    l[0]=Arbre
    print(len(l))
    for i,g in enumerate(Arguments):
        l[i+1]=l[i][g]
        print(len(l[i+1]))
    l[i+1]=Value
    print(l[i+1])
    print(Arbre[0][0][0][0][0][0][0][0])
    return Arbre
    
def niv(Object):
    n=0
    while type(Object) is list:
        n+=1
        if len(Object)==0:
            return n
        Object=Object[0]
    return n

def Arbrer(n,a=None,v=0):
    l=[]
    for i in range(v):
        l.append(a)
    v+=1
    if v<=n:
        return Arbrer(n,l,v)
    return l


def AffMorpion(Grille,Bool=False):
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


def extra_sum(Object):
    m=0
    while len(Object)!=m:
        m=len(Object)
        Object=DésincanterExcept(Object)
    return sum(Object)

def DésincanterMaxm(Object):
    m=0
    if type(Object) is list:
        while len(Object)!=m:
            m=len(Object)
            Object=DésincanterExcept(Object)
    return Object

#AffMorpion([])

def JouerHumain():
    done=False
    s=(500,500)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
                quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x=int(event.pos[0]/s[0]*3)
                y=int(event.pos[1]/s[1]*3)
                done=True
    print(x+y*3)
    return x+y*3


def ImplémenterBrute(Arbre,Partie):
    b=Arbre[:]
    p=Partie[:]
    l=len(p)
    if l==0:
        t=b
    if l==1:
        t=b[p[0]]
    if l==2:
        t=b[p[0]][p[1]]
    if l==3:
        t=b[p[0]][p[1]][p[2]]
    if l==4:
        t=b[p[0]][p[1]][p[2]][p[3]]
    if l==5:
        t=b[p[0]][p[1]][p[2]][p[3]][p[4]]
    if l==6:
        t=b[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]]
    if l==7:
        t=b[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]]
    if l==8:
        t=b[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]]
    if l==9:
        t=b[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]][p[8]]
    return t

def Jouer(Joueurs=[0,1]):
    g=[None]*9
    j=0
    Partie=[]
    Arbre=SortirVariable("Arbre de Morpions 1")[0]
    while not Win(g):
        AffMorpion(g)
        v=j%2
        if v==0:
            continuer=True
            while continuer:
                n=JouerHumain()
                if g[n]==None:
                    l=Indexes(None,g)
                    pi=l.index(n)
                    Partie.append(pi)
                    continuer=False
            g=Griller(Partie)
        if v==1:
            o=[]
            a=ImplémenterBrute(Arbre,Partie)
            mr=0
            mb=10*10
            mir=0
            if type(a) is int:
                print(a)
            for i in range(len(a)):
                if type(a[i]) is int:
                    print(a[i])
                e=DésincanterMaxm(a[i])
                s=extra_sum(a[i])
                sr=sum([e[k] for k in range(0,len(e),2)])
                sb=s-sr
                o.append([sr,sb])
                #print(sr,sb)
                if sr<mr:
                    sr=mr
                    mir=i
                if sb>mb:
                    sb=mb
                    mib=i
            print(o)
            Partie.append(mir)
            g=Griller(Partie)
        j+=1
    pygame.quit()
    if v==0:
        print("Le joueur gagne")
    if v==1:
        print("Le robot gagne")
    

def CréerArbre():
    #Progression(p[0],0,9)
    Options=[[0,0]]*9
    p=[0]
    r=0
    b=0
    a=Arbrer(9)
    #Possibilités=844146
    m=0
    while p[0]<9:
        try:
            w=Gain(p)
            #AffMorpion(Griller(p))
            if w==[0,0] and len(p)<9:
                p.append(0)
            else:
                """
                #Ajout#
                if p[0]==m:
                    r+=w[0]
                    b+=w[1]
                    Options[p[0]]=[r,b]
                else:
                    r,b=(0,0)
                m=p[0]
                #Ajout#"""
            
                #Implémentation Pratique#
                l=len(p)
                n=2**(9-l)
                r=w[0]
                b=w[1]
                if l==5:
                    a[p[0]][p[1]][p[2]][p[3]][p[4]]=[r*n,b*n]
                if l==6:
                    a[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]]=[r*n,b*n]
                if l==7:
                    a[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]]=[r*n,b*n]
                if l==8:
                    a[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]]=[r*n,b*n]
                if l==9:
                    a[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]][p[8]]=[r*n,b*n]
                #Implémentation Pratique#
                
                del p[-1]
                p[-1]+=1
        except:
            del p[-1]
            p[-1]+=1

    #Progression(p[0],0,9,True)
    print("fini")
            

"""

b=0
r=0
t=time.time()
s=0

while s<362880:
    gain=Gain(Partie)
    b+=gain[0]
    r+=gain[1]
    #Implémenter(Arbre,Partie,gain)
    Partie=AjouterSystème(Partie,Système,1)
    s=SortirSystème(Partie,Système)
    Progression(s,0,362880)
    #Show(str(int(TempsRestant(s,0,362880,t,time.time()))))
    #Show(str(Partie))


"""


#-------#
#Actions#
#-------#

Jouer([0,0])
