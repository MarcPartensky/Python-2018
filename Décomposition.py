from math import sqrt
import sys

Nombre = int(input("Nombre = "))                            #Nombre à tester
Début = "Vrai"
Puissance = 0
AncienDiviseur = 0

if Nombre <= 1:                                             #J'ai forcé...
    print("Le nombre entré est invalide")
else:
    for Diviseur in range(2,4):                             #Initialisation pour 2 et 3 (le 4 c'est à cause de leur langage...)
        Puissance = 0
        while Nombre%Diviseur == 0:                         #Bonne chance pour comprendre... sans explication=mission impossible
            Puissance = Puissance + 1
            if Début == "Vrai":
                print(Diviseur,end="")
                Début = "Faux"
            else:
                if Puissance == 1:
                    print('*',end="")
                    print(Diviseur,end="")
                if Puissance == 2:
                    print('^',end="")
            Nombre = Nombre/Diviseur
            AncienDiviseur = Diviseur
        if Puissance >= 2 and AncienDiviseur == Diviseur:
            print(Puissance,end="")

    Puissance = 0

    while Nombre != 1:                                      #Tant qu'il existe des diviseurs ...
        if Puissance >= 2 and AncienDiviseur == Diviseur:
            print(Puissance,end="")
        Puissance = 0
        while Nombre%Diviseur != 0:                         #Tant que les diviseurs ne sont pas valides ...
            Diviseur = Diviseur+2                           #Remarque: j'ai eu la flemme des 6k-1 et 6k+1 => prochaine mise à jour
        Puissance = Puissance + 1
        if Début == "Vrai":
            print(Diviseur,end="")
            Début = "Faux"
        else:
            if Puissance == 1:
                print('*',end="")
                print(Diviseur,end="")
            if Puissance == 2:
                print('^',end="")
        Nombre = Nombre/Diviseur
        AncienDiviseur = Diviseur
