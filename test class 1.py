from Fonctions import*
import os

def save(Object,Name):
    StockerVariable(Object.__dict__,Name,"w")

def take(Object,Name):
    Object.__dict__=SortirVariable(Name)[0]

class manger():
    def __init__(self):
        self.coca=True
        self.poulet=False


    def __setstate__(self,Attributs):
        #self.dict=SortirVariable("Attributs manger")[0]
        self.dict==Attributs

        
        
