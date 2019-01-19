import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import requests
import re
import math
import random
import numpy
import pickle
import selenium.webdriver as webdriver
import pygame
from pygame.locals import *


#Listes d'Alphabet
Alphabet="abcdefghijklmnopqrstuvwxyz"
Minuscules="abcdefghijklmnopqrstuvwxyz"
Majuscules="ABCDEGHIJKLMNOPQRSTUVWXYZ"
MinusculesComplètes="aàæâbcçdeéèêëfghiîïjklmnoôœpqrstuùûüvwxyÿz"
MajusculesComplètes="AÀÆÂBCÇDEÉÈÊËFGHIÎÏJKLMNOÔŒPQRSTUÙÛÜVWXYŸZ"
AlphabetComplet="aàæâbcçdeéèêëfghiîïjklmnoôœpqrstuùûüvwxyÿzAÀÆÂBCÇDEÉÈÊËFGHIÎÏJKLMNOÔŒPQRSTUÙÛÜVWXYŸZ"
Fin=".!?"
Ponctuation=",.;!?':()-"
CaractèresSpéciaux="#@&°_¨^+-=*$¥€£`\%§/\"<>"
Nombres="0123456789"

Tout=AlphabetComplet+Ponctuation+CaractèresSpéciaux+" "


Consonnes="bcçdfghjklmnpqrstvwxyÿz"
Voyelles=["a","à","æ","e","é","è","ê","ë","i","î","ï","o","ô","œ","u","ù","û","ü"]
SonsVoyelles=[["a","à","æ"],["e","œ"],["é"],["i","î","ï","y"],["o","ô"],["u","ù","û","ü"],["on"],["ou","oo"],["ai","ay","ei","ey","è","ê","ë"],["an","en"],["ain","ein","un","in"]]
SonsConsonnes=[["bb","b"],["qu","ck","cc","c","k","q"],["dd","d"],["ff","ph","f"],["gg","gu","g"]]

PronomsPersonnelsGroupés=[["je"],["tu"],["il,elle,on"],["nous"],["vous"],["ils,elles"]]
PronomsPersonnels=["je","tu","il","nous","vous","ils"]
PronomsPersonnelsComplets=["je","tu","il","elle","on","nous","vous","ils","elles"]

Anglais=["the","be","to","of","and","a","in","that","have","i","it","for"
             ,"not","with","he","as","you","do","at","this","but","his","by",
             "from","they","we","say","her","she","or","an","will","my","one",
             "all","would","there","their","what","so","up","out","if","about",
             "who","get","which","go","when","make","can","like","time",
             "no","just","him","know","take","people","into","year","your",
             "good","some","could","them","see","other","than","then","now",
             "look","only","come","its","over","think","also","back","after",
             "use","two","how","our","work","first","well","way","even","new",
             "want","because","any","these","give","day","most","us"]

rep_programmes=rep="/Users/olivierpartensky/Desktop/Programme/GitHub/python_projects/Bibliothèque/"

BLACK  = (  0,  0,  0)
WHITE  = (255,255,255)
RED    = (255,  0,  0)
GREEN  = (  0,255,  0)
BLUE   = (  0,  0,255)
CYAN   = (  0,255,255)
PURPLE = (255,  0,255)
YELLOW = (255,255,  0)
BROWN  = (150, 75,  0)
ORANGE = (255,140,  0)
RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


#https://www.notrefamille.com/dictionnaire/definition/manger/


#vide,français,autrelangue

#Fonctions

AfficherErreur=False
AffBool=True
Erreurs=[]

def Après(Liste,Contenu):
    l=Liste[:]
    c=Contenu[:]
    après=[]
    for e in l:
        for i in range(len(c)-1):
            if e==c[i]:
                après.append(c[i+1])
    return après

def ExtraDésincanter(Object):
    o=Object[:]
    m=0
    while m!=len(o):
        m=len(o)
        o=DésincanterExcept(o)
    return o

def ListerFréquence(Liste):
    l=Liste
    s=list(set(l))
    d={}
    for i,v in enumerate(s):
        s[i]=[s[i],l.count(v)]
    r=sorted(s,key=lambda a: a[1])
    r.reverse()
    return r



def Aff(Bool=AffBool,*args):
    if Bool:
        print(*args)

def aff(Bool=AffBool,*args):
    if Bool:
        print(*args)

def Show(Texte,Bool=True,taille=1):
    pygame.init()
    fenetre = pygame.display.set_mode((10*len(Texte), 20))
    font=pygame.font.Font(None, 24)
    VERT=(255,255,0)
    text = font.render(Texte,taille,VERT)
    fenetre.blit(text, (0, 0))
    pygame.display.flip()
    if Bool==False:
        pygame.quit()

def TryOut(NameFile,Default=None):
    File=SortirVariable(NameFile)
    try:
        return File[0]
    except:
        return Default

def Découper(Chaine,Liste):
    Tuple=[]
    j=0
    Début=0
    Bool=False
    done=False
    i=0
    while i<len(Chaine)-len(Liste[j])+1 and not done:
        if Chaine[i:i+len(Liste[j])]==Liste[j]:
            if j<len(Liste)-1:
                if Bool:
                    Tuple.append(Chaine[Début:i])
                Début=i+len(Liste[j])
                j+=1
                Bool=True
            else:
                if Bool and len(Chaine[Début:i])>0:
                    Tuple.append(Chaine[Début:i])
                done=True
        i+=1
    return Tuple


def name(var):
    for n,v in globals().items() :
        if v is var :
            return n
    return '?????'

def printv(var):
    print(name(var))


def SoustraireLinéairement(L1,L2):
    n=0
    i=0
    while i<len(L1) and n<len(L2):
        if L1[i]==L2[n]:
            del L1[i]
            n+=1
            i-=1
        i+=1
    return L1

"""-------"""
"""Chaines"""
"""-------"""

def SéquencesCommunes(Chaine1,Chaine2):
    Chaine1.lower()
    Chaine2.lower()
    Séquences=[]
    m=min(len(Chaine1),len(Chaine2))
    for t in range(0,m):
        for i in range(len(Chaine1)-t):
            for j in range(len(Chaine2)-t):
                if Chaine1[i:i+t+1]==Chaine2[j:j+t+1]:
                    Séquences.append(Chaine1[i:i+t+1])
    Séquences.reverse()
    return Séquences

def Ressemblance(Chaine1,Chaine2):
    Séquences=SéquencesCommunes(Chaine1,Chaine2)
    m=min(len(Chaine1),len(Chaine2))
    try:
        Ressemblance=(sum([len(i) for i in Séquences])-1)/len(Séquences)
        return Ressemblance
    except:
        return 0

#Rsb#

def Rsb(c,C):
    c.lower()
    C.lower()
    m=min(len(c),len(C))
    p=float(len(c)+len(C))/2
    for t in range(0,m):
        l=m-1-t
        for i in range(len(c)-l):
            for j in range(len(C)-l):
                if c[i:i+l+1]==C[j:j+l+1]:
                    return l/p
    return 0

def Rsb2(C1,C2):
    l1=len(C1)
    l2=len(C2)
    m=min(l1,l2)
    liste=list(range(m))
    if len(liste)!=0:
        del liste[0]
    liste.reverse()
    for i in liste:
        for f in range(l1-i+1):
            for g in range(l2-i+1):
                if C1[f:f+i+1]==C2[g:g+i+1]:
                    return Rsb2(C1[:f],C2[:g])+i+1+Rsb2(C1[f+i+1:],C2[g+i+1:])
    return 0

def Rsb3(C1,C2):
    i=Rsb2(C1,C2)
    r=2*i/(len(C1)+len(C2))
    return r

def Rsb4(C1,C2):
    l1=len(C1)
    l2=len(C2)
    m=min(l1,l2)
    liste=list(range(m))
    liste.reverse()
    for i in liste:
        for f in range(l1-i+1):
            for g in range(l2-i+1):
                if C1[f:f+i+1]==C2[g:g+i+1]:
                    return Rsb2(C1[:f],C2[:g])+i+Rsb2(C1[f+i+1:],C2[g+i+1:])
    return 0

def Rsb5(C1,C2):
    i=Rsb4(C1,C2)
    r=2*i/(len(C1)+len(C2))
    return r

#Select#

def Select(Elément,Liste):
    l=Liste[:]
    e=Elément
    r=0
    m=0
    for i in range(len(l)):
        n=Rsb5(e,l[i])
        if n>r:
            r=n
            m=i
    return m

def ExpanseSelect(Elément,Liste):
    l=Liste[:]
    e=Elément
    r=0
    m=0
    for i in range(len(l)):
        n=Rsb5(e,l[i])
        if n>r:
            r=n
            m=i
    return l[m]

def SelectListe(Elément,Liste):
    l=Liste[:]
    e=Elément
    m=0
    r=0
    for i,u in enumerate(l):
        p=0
        for j,v in enumerate(l[i]):
            n=Rsb3(e,v)
            p+=n
        if p>m:
            m=p
            r=i
    return r

def Appartenance(Elément,Liste):
    l=Liste[:]
    e=Elément
    r=0
    m=0
    for i in range(len(l)):
        n=Rsb3(e,l[i])
        if n>r:
            r=n
            m=i
    return r

def SelectLangue(Texte,Langues):
    a=[]
    for Langue in Langues:
        a.append(Aptn(Texte,Langue))
    maxi=max(a)
    i=a.index(maxi)
    del a[i]
    pertinence=maxi-max(a)
    return (i,maxi,pertinence)

def Aptn(e,l):
    e=SplitMots(e)
    s=Soustraire(e,l)
    return 1-len(s)/len(e)

def Aptn1(Elément,Liste):
    l=Liste[:]
    e=SplitMots(Elément)
    n=0
    for v in e:
        v=v.lower()
        n+=Appartenance(v,l)
    return n/len(e)

def Aptn2(Elément,Liste,Lambda=10):
    b=Lambda
    l=Liste[:]
    e=SplitMots(Elément)
    n=0
    for v in e:
        v=v.lower()
        a=Appartenance(v,l)
        n+=sig(a,b)
    return n/len(e)

def Aptn3(Elément,Liste,Lambda=10):
    b=Lambda
    l=Liste[:]
    e=SplitMots(Elément)
    n=0
    for v in e:
        v=v.lower()
        a=l.count(v)
        n+=sig(a,b)
    return n/len(e)

def Sigmoide(x):
    e=math.exp(x)
    y=1/(1+e**(-x))
    return y

def sig(x,Lambda=10):
    try:
        x=(x*2-1)
        y=1/(1+math.exp(-x*Lambda))
        return y
    except:
        return 0

def Différent(x):
    r=random.random()
    while r==x:
        r=random.random()
    return r


def PlusOuMoins(Fonction,Recherché,Précision=10,Départ=0,Précision_Départ=10):
    prc=Précision
    x=Départ
    r=Recherché
    p=Précision_Départ
    mouv=[10,11,13]
    y=0
    done=False
    init=True
    while (y!=r or init) and len(mouv)<prc:
        init=False
        mem=x
        y=eval(Fonction)
        x=mem-p
        m=eval(Fonction)
        x=mem+p
        M=eval(Fonction)
        x=mem
        dm=abs(m-r)
        dM=abs(M-r)
        mouv.append(x)
        if mouv[-1]==mouv[-3]:
            p/=10
        if dm<dM:
            d=dm
            x=x-p
        if dM<dm:
            d=dM
            x=x+p
        Aff(False,x,(y,r),(m,M),(dm,dM),p,mouv)
    x=round(x,15)
    return (x,y)

def PlusOuMoins2(Fonction,Recherché,Précision=10,Départ=1):
    prc=Précision
    x=Départ
    r=Recherché
    p=1
    mouv=[10,11,13]
    y=0
    done=False
    init=True
    while (y!=r or init) and len(mouv)<prc:
        init=False
        mem=x
        y=eval(Fonction)
        x=mem-p
        m=eval(Fonction)
        x=mem+p
        M=eval(Fonction)
        x=mem
        dm=abs(m-r)
        dM=abs(M-r)
        mouv.append(x)
        if dm<dM:
            d=dm
            x=x-p
        if dM<dm:
            d=dM
            x=x+p
        drv=mouv[-1]-mouv[-2]
        if drv>0:
            p*=2
        if drv<0:
            p/=2
        Aff(False,x,(y,r),(m,M),(dm,dM),p,mouv)
    x=round(x,15)
    return (x,y)

def PlusOuMoinsRaté(Fonction,Recherché,Départ=1):
    x=Départ
    r=Recherché
    p=1
    mouv=[1,1]
    done=False
    while not done:
        mem=x
        y=eval(Fonction)
        x=x-p
        m=eval(Fontion)
        x=x+p
        M=eval(Fontion)
        x=mem
        dm=abs(m-r)
        dM=abs(M-r)
        mouv.append(x)
        if dm<dM:
            d=dm
            x=x-p
        if dM<dm:
            d=dM
            x=x+p


    return [x,y,mouv]


#Répondre#

def Répondre(Chaine):
    Phrases=SortirVariable("Messenger2")[0]
    return Répondre4(Chaine,Phrases)

def Répondre2(Entrée,Phrases):
    Dico={}
    l=len(Phrases)
    for i in range(l):
        Dico[str(Rsb(Phrases[i],Entrée))]=i
        Progression(i,0,l)
    Ressemblances=list(Dico)
    Ressemblances.sort()
    Ressemblances.reverse()
    Proba=[]
    for i in range(len(Liste)):
        Proba.append(Ressemblances[i]/2**i)
    r=random.randfloat(0,len(sum(Proba)))
    i=0
    n=0
    while i<r:
        i+=Proba[n]
        n+=1
    Sortie=Phrases[Dico[Ressemblances[i]]+1]
    return Sortie

def Répondre3(Entrée,Phrases,Bool=False,Pertinence=0.5):
    e=Entrée
    P=Phrases
    l=len(P)
    v=0
    i=0
    p=0
    while p<l:
        n=Rsb5(P[p],e)
        if n>v:
            i=p
            v=n
        p+=1
    print(v,Pertinence)
    try:
        if Bool:
            if v>Pertinence:
                return Phrases[i+1]
            else:
                #return Phrases[i+1]+"\n Pertinence: "+str(v)
                return Phrases[i+1]
        if v>Pertinence:
            return Phrases[i+1]
        else:
            return None
    except:
        return None

def Répondre4(Entrée,Phrases):
    e=Entrée
    P=Phrases
    v=0
    for i,a in enumerate(P):
        r=Rsb5(a,e)
        if r>v:
            p=i
            v=r
    return P[p+1]

def Répondre5(Entrée,Phrases):
    e=Entrée
    P=Phrases
    v=0
    for i,a in enumerate(P):
        r=Rsb5(a,e)
        if r>v:
            p=i
            v=r
    return [P[p],P[p+1],p,v]


def ChatBox2():
    Structure=SortirVariable("Structure")
    ExterminerNone(Structure)
    #Phrases=Phraser(Structure)
    Historique=SortirVariable("Messenger")
    Phrases=[]
    for Message in Historique:
        if Message[0]=="P":
            Phrases.append(Message[10:])
    Bot="Bonjour"
    print(Bot)
    User=str(input(""))
    while User!=Ressemblance(User,"au revoir")<2:
        Bot=Répondre3(User,Phrases)
        print(Bot)
        User=str(input(""))


def RépondreStructure(Chaine):
    Structure=SortirVariable("Structure")
    ExterminerNone(Structure)
    Phrases=Phraser(Structure)
    if Phrases.count(Chaine)==0:
        return None
    else:
        Réponses=[]
        Indices=RécupérerIndices(Chaine,Phrases)
        for i in Indices:
            Réponses.append(Phrases[i+1])
        Réponse=Réponses[random.randint(0,len(Réponses)-1)]
        return Réponse

#

def Phraser(Structure):
    Phrases=SortirVariable("Phrases")
    if Phrases==None:
        Phrases=Désincanter(Désincanter(Structure))
        i=0
        while i<len(Phrases):
            Phrases[i]="".join(Phrases[i])
            i+=1
    return Phrases




def lenD(Dictionnaire):
    Liste=list(Dictionnaire)
    return len(Liste)

def InverserMatrice(Matrice):
    Inversé=[[None]*len(Matrice) for i in range(len(Matrice[0]))]
    for i in range(len(Matrice)):
        for j in range(len(Matrice[i])):
            Inversé[i][j]=Matrice[j][i]
    return Inversé

def ExterminerNone(l):
    if type(l) != list:
        return
    l[:] = [i for i in l if i is not None]
    for e in l:
       ExterminerNone(e)


def Indexes(Elément,Liste):
    l=Liste[:]
    Indices=[]
    i=0
    while l.count(Elément)>0:
        Indices.append(l.index(Elément)+i)
        l.remove(Elément)
        i+=1
    return Indices

def Dict(Liste):
    Dictionnaire={}
    for i in Liste:
        Dictionnaire[i]=None
    return Dictionnaire

def SplitBalises(Chaine):
    return Extraire(Chaine,Tout,">","<")

def ComparerLangue(Tuple,Langue):
    Nombre=0
    Intrus=[]
    for Mot in Langue:
        if Tuple.count(Mot)>0:
            Intrus.append(Mot*Tuple.count(Mot))
    return Intrus

def AjouterDictionnaire(Tuple,Dictionnaire):
    Réduction=Réduire(Tuple)
    for Mot in Réduction:
        if Dictionnaire.count(Mot)==0:
            Dictionnaire[Mot]=Réduction.count(Mot)
        else:
            Dictionnaire[Mot]=Dictionnaire[Mot]+Réduction.count(Mot)
    return Dictionnaire



def EliminerVide(Tuple):
    while Tuple.count([])>0:
        Tuple.remove([])
    return Tuple

def ExterminerVide(Tuple,Niveau):
    Base=1
    w

def Eliminer(Elément,Liste):
    e=Elément
    l=Liste[:]
    while l.count(e)>0:
        l.remove(e)
    return l



def ValiditéLangue(Tuple,Langue):
    Exceptions=0
    for LangueConsidérée in Langues:
        if LangueConsidérée!=Langue:
            Exceptions+=len(ComparerLangue(Tuple,LangueConsidérée))
    Validité=int(len(ComparerLangue(Tuple,Langue))/len(Tuple)*100)
    if Validité>5 and Exceptions==0:
        return True
    else:
        return False



def Erreur(Fonction):
    global AfficherErreur
    if AfficherErreur:
        print("La fonction",Fonction,"n'a pas pue être exécutée.")
    Erreurs.append(Fonction)
    StockerTexte(Fonction+" ","Erreurs","a")

def Numerer(Mot):
    try:
        Mot=Mot.lower()
        Valeur=float(0)
        for j in range(0,len(Mot)):
            Valeur=AlphabetComplet.index(Mot[j])/len(AlphabetComplet)**(j+1)+Valeur
        return Valeur
    except:
        Erreur("Numerer")

def Classer(Mot,Liste):
    try:
        MV=Numerer(Mot)
        l=0
        Recherche=True
        while Recherche:
            if l<len(Liste):
                if Numerer(Liste[l])>MV:
                    Recherche=False
                else:
                    l=l+1
            else:
                Recherche=False
        if l<len(Liste):
            if Numerer(Liste[l])>MV:
                Sortie=Liste[0:l]
                Sortie.append(Mot)
                Sortie.extend(Liste[l:len(Liste)])
                Liste=Sortie[:]
        else:
            Liste.append(Mot)
        return Liste
    except:
        Erreur("Classer")

def DécomposerEnSyllables(Mot):
    Mot=Mot.lower()
    Tuple=[]
    Début=0
    if Consonnes.count(Mot[0])==1:
        ExceptionBool=True
    else:
        ExceptionBool=False
    for i in range(len(Mot)-1):
        if Consonnes.count(Mot[i])==1:
            if Voyelles.count(Mot[i+1])==1:
                if ExceptionBool==False:
                    Tuple.append(Mot[Début:i])
                    Début=i
                else:
                    ExceptionBool=False
        if Mot[i]==" ":
            Tuple.append(Mot[Début:i])
            Début=i+1
            if Consonnes.count(Mot[i+1])==1:
                ExceptionBool=True
            else:
                ExceptionBool=False
    Tuple.append(Mot[Début:])
    return Tuple



def Voisinage(NuméroLettre,Mot):
    try:
        Voisins=[]
        Nl=NuméroLettre
        if Nl>0:
            Voisins.append(Mot[Nl-1])
        if Nl<len(Mot)-1:
            Voisins.append(Mot[Nl+1])
        return Voyelles
    except:
        Erreur("Voisinage")

def CompterSyllables(Mot):
    try:
        Mot=Mot.lower()
        if Mot[-1]=="e" or Mot[-2:]=="e.":
            Syllables=-1
        else:
            Syllables=0
        NouvelleVoyelle=False
        n=0
        for Lettre in Mot:
            AncienneVoyelle=NouvelleVoyelle
            NouvelleVoyelle=False
            for Voyelle in Voyelles:
                if Lettre==Voyelle:
                    NouvelleVoyelle=True
            if Lettre=="y":
                VoyelleSyllable=0
                for Voisin in Voisinage(n,Mot):
                    for VoyelleY in Voyelles:
                        if Voisin==VoyelleY:
                            VoyelleSyllable=VoyelleSyllable+1
                if VoyelleSyllable==0:
                    Syllables=Syllables+1
            if NouvelleVoyelle==True and AncienneVoyelle==False:
                Syllables=Syllables+1
            n=n+1
        return Syllables
    except:
        Erreur("CompterSyllables")

def Associer(Liste,Tuple):
    try:
        Sequence=[]
        for Element in Liste:
            for i in range(0,len(Tuple)):
                if Tuple[i].count(Element)==1:
                    Sequence.append(i)
        return Sequence
    except:
        Erreur("Associer")

def Réduire(Liste):
    try:
        for i in Liste:
            while Liste.count(i)>1:
                Liste.remove(i)
        return Liste
    except:
        Erreur("Réduire")

def RechercherUrl(search):
    try:
        url = "https://www.startpage.com"
        browser = webdriver.Chrome(executable_path="/Applications/chromedriver")
        browser.get(url)
        search_box=browser.find_element_by_id("query")
        search_box.send_keys(search)
        search_box.submit()
        try:
            links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
        except:
            links = browser.find_elements_by_xpath("//h3//a")
        Urls = []
        for link in links:
            href = link.get_attribute("href")
            Urls.append(href)
        browser.close()
        return Urls
    except:
        Erreur("RechercherUrl")

def StockerSite(Url,FichierTexte,Mode):
    try:
        html = requests.get(Url).content
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("utf8",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        liste=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        y=" ".join(liste)
        print(y)
        file = open(FichierTexte+".txt", Mode)
        file.write(str(y))
        file.close()
    except:
        Erreur("StockerSite")

def RécupérerSite(Url):
    try:
        html = requests.get(Url).content
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("utf8",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        liste=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        y=" ".join(liste)
        return y
    except:
        Erreur("RécupérerSite")

def ConvertirListeEnNombre(Liste):
    try:
        Chaine=""
        for i in Liste:
            Chaine+=str(i)
        return int(Chaine)
    except:
        Erreur("ConvertirListeEnNombre")

def PermuterAléatoirement(Entrée):
    Sortie=[]
    while Entrée!=[]:
        i=random.randint(0,len(Entrée)-1)
        Sortie.append(Entrée[i])
        del Entrée[i]
    return Sortie


def DésincanterExcept(Tuple):
    Sortie=[]
    for i in Tuple:
        if type(i) is list or type(i) is tuple:
            for j in i:
                Sortie.append(j)
        else:
            Sortie.append(i)
    return Sortie

def Désincanter(Tuple):
    Sortie=[]
    for i in Tuple:
        for j in i:
            Sortie.append(j)
    return Sortie

def StockerTexte(Chaine,NomFichier,Mode):
    try:
        with open(NomFichier+".txt", Mode, encoding="utf-8") as Fichier:
            Fichier.write(Chaine)
    except:
        Erreur("StockerTexte")

def Soustraire(Dictionnaire1,Dictionnaire2):
    try:
        NouveauDico=[]
        for Mot in Dictionnaire1:
            if Dictionnaire2.count(Mot)==0:
                NouveauDico.append(Mot)
        return NouveauDico
    except:
        Erreur("Soustraire")

def TraduireTexteEnTuple(Nom,Mode):
    try:
        with open(Nom+".txt", 'r', encoding="utf-8") as FichierDicoTexte:
             ChaineDicoTexte=FichierDicoTexte.read()
             Dico=ChaineDicoTexte.split(" ")
        try:
            with open(Nom, Mode+'b') as FichierDicoTuple:
                DicoTuplePickler = pickle.Pickler(FichierDicoTuple)
                DicoTuplePickler.dump(Dico)
        except:
            print("Ecriture impossible.")
    except:
        Erreur("ConvertirTexteEnTuple")

def TraduieTupleEnTexte(Nom,Mode):
    try:
        with open(Nom, 'rb') as FichierDicoTuple:
            DicoTupleDepickler = pickle.Unpickler(FichierDicoTuple)
            DicoTuple = DicoTupleDepickler.load()
            Dico=" ".join(DicoTuple)
        with open(Nom+".txt", Mode, encoding="utf-8") as FichierDicoTexte:
             ChaineDicoTexte=FichierDicoTexte.write(Dico)
    except:
        Erreur("ConvertirTupleEnTexte")

def SplitParagraphes(Chaine):
    try:
        return [Chaine]
    except:
        Erreur("SplitParagraphes")

def SplitPhrases(Chaine):
    try:
        Tuple=[]
        PhraseBool=False
        DebutBool=False
        for i in range(len(Chaine)):
            PhraseBool=False
            if AlphabetComplet.count(Chaine[i])==1 or Ponctuation.count(Chaine[i])==1 or Chaine[i]==" " or Nombres.count(Chaine[i])==1:
                PhraseBool=True
            else:
                PhraseBool=False
                DebutBool=False
            if i<len(Chaine)-2:
                if CaractèresSpéciaux.count(Chaine[i])==1 and CaractèresSpéciaux.count(Chaine[i+1])==1:
                    PhraseBool=False
                    DebutBool=False
            if MajusculesComplètes.count(Chaine[i])==1:
                DebutBool=True
                PhraseBool=True
                Phrase=""
            if PhraseBool:
                Phrase+=Chaine[i]
            if DebutBool and PhraseBool and Fin.count(Chaine[i])==1:
                if len(Phrase)>=3:
                    Tuple.append(Phrase)
                DebutBool=False
                PhraseBool=False
        return Tuple
    except:
        Erreur("SplitPhrases")

def AssocierCaractère(Caractère):
    if AlphabetComplet.count(Caractère)==1:
        return "AlphabetComplet"
    elif CaractèresSpéciaux.count(Caractère):
        return "CaractèresSpéciaux"
    else:
        return "Autre"

def SplitEléments(Chaine):
    try:
        Début=0
        Tuple=[]
        for i in range(len(Chaine)-1):
            if AssocierCaractère(Chaine[i])!=AssocierCaractère(Chaine[i+1]):
                Tuple.append(Chaine[Début:i+1])
                Début=i+1
        Tuple.append(Chaine[-1])
        return Tuple
    except:
        Erreur("SplitEléments")


def SplitMotsRaté(Chaine):
    try:
        Chaine=Chaine.lower()
        for i in CaractèresSpéciaux:
            Chaine=Chaine.replace(i," ")
        for i in Nombres:
            Chaine=Chaine.replace(i," ")
        Chaine=Chaine.replace("'"," ")
        return Chaine[0:len(Chaine)-1].split(" ")
    except:
        Erreur("SplitMotsRaté")

def SplitMots(Chaine):
    try:
        Chaine=Chaine.lower()
        Tuple=[]
        MotBool=False
        DébutBool=False
        for i in range(len(Chaine)):
            MotBool=False
            if MinusculesComplètes.count(Chaine[i])==1:
                MotBool=True
                if DébutBool==False:
                    DébutBool=True
                    Mot=""
            else:
                MotBool=False
            if MotBool:
                Mot+=Chaine[i]
            if DébutBool and MotBool==False:
                if len(Mot)>=2 and CompterSyllables(Mot)>0:
                    Tuple.append(Mot)
                DébutBool=False
                MotBool=False
        return Tuple
    except:
        Erreur("SplitMots")

def DicoDesSynos(Chaine):
    Tuple=[]
    MotBool=False
    for i in range(len(Chaine)-5):
        if Chaine[i:i+1]=="\">":
            MotBool=True
            Début=i+2
        if MotBool and AlphabetComplet.count(Chaine[i])==0:
            MotBool=False
        if Chaine[i:i+3]=="</a>" and MotBool:
            Tuple.append(Chaine[Début:i-1])
            MotBool=False
    print(Tuple)



def GénérerConditions():
    Conditions=[]
    return Condtions


def ExtraireRaté(Chaine,Groupe,Début,Fin):
    Chaine=str(Chaine)
    Extraits=[]
    Bool=False
    DébutBool=True
    début=0
    Elément=""
    Groupe=str(Groupe)
    for i in range(len(Chaine)):
        if i+len(Début)<len(Chaine):
            if Chaine[i:i+len(Début)]==Début and Bool==False:
                début=i+len(Début)
                DébutBool=True
        if DébutBool==True and i>=début:
            Bool=True
        if Bool==True:
            if Groupe.count(Chaine[i])>0:
                Elément+=Chaine[i]
            else:
                Bool=False
                DébutBool=False
                Elément=""
        if i+1+len(Fin)<len(Chaine):
            if Chaine[i+1:i+1+len(Fin)]==Fin and Bool==True:
                if len(Elément)>1:
                    Extraits.append(Elément)
                DébutBool=False
                Bool=False
                Elément=""
    return Extraits

def Extraire(Chaine,Groupe,Début,Fin):
    début=False
    Tuple=[]
    Elément=""
    for i in range(len(Chaine)-len(Fin)+1):
        if Chaine[i:i+len(Fin)]==Fin:
            début=False
            if len(Elément)>0:
                Tuple.append(Elément)
        if Chaine[i:i+len(Début)]==Début:
            début=True
            Elément=""
            Mémoire=i
        if Groupe.count(Chaine[i])>0 and début:
            if i>=Mémoire+len(Début):
                Elément+=Chaine[i]
        else:
            début=False
            Elément=""
    return Tuple

def Synonymes(Mot):
    try:
        Synonymes=[]
        Mot=Mot.lower()
        Dictionnaires=["http://www.synonymes.com/synonyme.php?mot="+Mot+"&x=0&y=0",
                       "http://www.crisco.unicaen.fr/des/synonymes/"+Mot,
                       "www.synonymo.fr/synonyme/"+Mot]
        for Url in Dictionnaires:
            CodeSource=RécupérerCodeSource(Url)
            Synonymes.extend(Extraire(CodeSource,MinusculesComplètes+" ","\">","</a>"))
        Synonymes.sort()
        Synonymes=Réduire(Synonymes)
        Synonymes=Soustraire(Synonymes,["user","avertissement"])
        return Synonymes
    except:
        Erreur("Synonymes")

def Définitions(Mot):
    try:
        Définitions=[]
        Mot=Mot.lower()
        Dictionnaires=["http://www.le-dictionnaire.com/definition.php?mot="+Mot]
        for Url in Dictionnaires:
            CodeSource=RécupérerCodeSource(Url)
            Définitions.extend(Extraire(CodeSource,AlphabetComplet+Ponctuation+" ","\">","</a>"))
        Définitions=Soustraire(SplitPhrases(" ".join(Définitions)),["Conjugaison.","Calculatrice.","Définition manquante ou compléter."])
        Définitions=Réduire(Définitions)
        return Définitions
    except:
        Erreur("Définition")

def RécupérerCodeSource(Url):
    try:
        uClient = uReq(Url)
        page_html = uClient.read()
        uClient.close()
        return str(BeautifulSoup(page_html, "html.parser"))
    except:
        Erreur("RécupérerCodeSource")


def TrouverDansChaine(SousChaine,Chaine):
    try:
        Len=len(Chaine)-len(SousChaine)
        for i in range(Len):
            if Chaine[i:i+len(SousChaine)]==SousChaine:
                return i
        return None
    except:
        Erreur("TrouverDansChaine")


def StockerVariable(Tuple,NomFichierTuple,Mode):
    try:
        with open(NomFichierTuple, Mode+'b') as FichierTuple:
            FichierTuplePickler = pickle.Pickler(FichierTuple)
            FichierTuplePickler.dump(Tuple)
    except:
        Erreur("StockerTuple")

def SortirVariable(NomFichierTuple):
    try:
        with open(NomFichierTuple, 'rb') as FichierTuple:
            FichierTupleDepickler = pickle.Unpickler(FichierTuple)
            try:
               Tuple=[]
               while True:
                   Tuple.append(FichierTupleDepickler.load())
            except:
                return Tuple
    except:
        Erreur("SortirTuple")


def SortirTexte(Fichier):
    try:
        with open(Fichier+".txt", "r",encoding="utf-8") as FichierTexte:
            texte=FichierTexte.read()
        return texte
    except:
        Erreur("SortirTexte")

def Sortir(Fichier):
    try:
        with open(Fichier, "r",encoding="utf-8") as FichierTexte:
            texte=FichierTexte.read()
        return texte
    except:
        Erreur("Sortir")

def TempsRestant(Position,Début,Fin,InstantDébut,InstantPosition):
    p=Position
    d=Début
    f=Fin
    td=int(InstantDébut)
    tp=int(InstantPosition)
    return ((f-p)*(tp-td))/(p-d+1)

def Progression(V,D,F,Stop=False):
    pygame.init()
    done=False
    Width=500
    Height=20
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)
    BLUE     = (   0,   0, 255)
    COULEUR=GREEN
    FOND=BLACK
    size=(Width,Height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Progression")
    clock = pygame.time.Clock()
    screen.fill(FOND)
    E=(Width*V)//(F-D)
    pygame.draw.rect(screen, COULEUR, (0,0,E,Height),0)
    pygame.display.flip()
    clock.tick(1000000)
    if V>=F or done or Stop:
        pygame.quit()


#Permutation

def prod(Liste):
    Nombre=1
    for i in Liste:
        Nombre*=i
    return Nombre

def sum(Liste):
    Nombre=1
    for i in Liste:
        Nombre+=i
    return Nombre

def size(Liste):
    Nombre=1
    Coefficient=1
    for i in Liste:
        Nombre+=i*Coefficient
        Coefficient*=i
    return Nombre

def AjouterSystème(Progression,Système,Ajout):
    Nombre=SortirSystème(Progression,Système)
    Nombre=(Nombre+Ajout)%size(Système)
    Progression=EntrerSystème(Nombre,Système)
    return Progression

def SortirSystème(Progression,Système):
    Nombre=0
    Coefficient=1
    for i in range(len(Système)):
        Nombre+=Progression[-i-1]*Coefficient
        Coefficient*=Système[-i-1]
    return Nombre

def EntrerSystème(Nombre,Système):
    Progression=[]
    Coefficient=prod(Système)
    for i in range(len(Système)):
        Coefficient//=Système[i]
        Progression.append(Nombre//Coefficient)
        Nombre=Nombre%Coefficient
    return Progression

#IA#

def MoyenneParagraphes(Structure):
    Nombre=0
    for i in Structure:
        Nombre+=len(i)
    return Nombre/len(Structure)

#Installations#

def InstallerBeautifulSoup():
    return "moche"


#Statistiques#

def Statistiques(Liste):
    Liste.sort()
    Indice1erQuartile=len(Liste)//4
    IndiceMédianne=len(Liste)//2
    Indice3eQuartile=(3*len(Liste))//4
    Statistiques={}
    Moyenne=0
    v1erQuartile=0
    Médianne=0
    v3eQuartile=0
    for i in range(len(Liste)):
        Moyenne+=Liste[i]
        if i==Indice1erQuartile:
            v1erQuartile=Liste[i]
        if i==IndiceMédianne:
            Médianne=Liste[i]
        if i==Indice3eQuartile:
            v3eQuartile=Liste[i]
    Moyenne=Moyenne/len(Liste)
    Réduite=Réduire(Liste)
    Maximum=0
    Majorité=0
    for i in Réduite:
        if Liste.count(i)>Maximum:
            Maximum=Liste.count(i)
            Majorité=i
    Statistiques["Moyenne"]=Moyenne
    Statistiques["Médianne"]=Médianne
    Statistiques["Majorité"]=Majorité
    Statistiques["1er Quartile"]=v1erQuartile
    Statistiques["3e Quartile"]=v3eQuartile
    Statistiques["Ecart-Type"]=v3eQuartile-v1erQuartile
    Statistiques["Minimum"]=Liste[0]
    Statistiques["Maximum"]=Liste[-1]
    Statistiques["Etendu"]=Liste[-1]-Liste[0]

    return Statistiques

def StatsParagraphes(Structure):
    Liste=[]
    for i in Structure:
        Liste.append(len(i))
    return Liste





#Ancien

def GenererDictionnaire(Fichier,Dictionnaire):
    try:
        with open(Dictionnaire, 'rb') as FichierDico:
            DicoDepickler = pickle.Unpickler(FichierDico)
            Dico = DicoDepickler.load()
    except:
        with open(Dictionnaire, 'wb') as FichierDico:
            Dico=["je"]
            DicoPickler = pickle.Pickler(FichierDico)
            DicoPickler.dump(Dico)
        with open(Dictionnaire, 'rb') as FichierDico:
            DicoDepickler = pickle.Unpickler(FichierDico)
            Dico = DicoDepickler.load()
    FichierTexte = open(Fichier+".txt", "r",encoding="utf-8")
    Texte=FichierTexte.read()
    TexteMn=Texte.lower()
    LettreNew=False
    NouveauMot=False
    m=0
    Dico=[]
    for i in range(0,len(TexteMn)):
        LettreOld=LettreNew
        LettreNew=False
        for Lettre in AlphaBP:
            if TexteMn[i]==Lettre:
                LettreNew=True
        if LettreNew==True and LettreOld==False:
            MotD=i
        if LettreNew==False and LettreOld==True:
            MotF=i
            NouveauMot=True
        if NouveauMot==True:
            Mot=TexteMn[MotD:MotF]
            if TesterClassement(Mot,Dico):
                Dico=Classer(Mot,Dico)
            NouveauMot=False
    FichierTexte.close()
    DicoChaine=" ".join(Dico)
    with open(Dictionnaire+".txt", 'w', encoding="utf-8") as FichierDicotxt:
         FichierDicotxt.write(DicoChaine)
    with open(Dictionnaire, 'wb') as FichierDico:
        DicoPickler = pickle.Pickler(FichierDico)
        DicoPickler.dump(Dico)
