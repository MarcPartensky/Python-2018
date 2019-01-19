#Authored by Grant Slatton on 2013 September 15
#All code is released to the public domain under the terms of [http://unlicense.org]

from random import randint, shuffle, choice
import sys
import pygame
from pygame.locals import *


#needed for DFS...
sys.setrecursionlimit(10000)

#Each maze cell contains a tuple of directions of cells to which it is connected

#Takes a maze and converts it to an array of X's and blanks to represent walls, etc
def convert(maze):
    pretty_maze = [["X"]*(2*len(maze[0])+1) for a in range(2*len(maze)+1)]
    for y,row in enumerate(maze):
        for x,col in enumerate(row):
            pretty_maze[2*y+1][2*x+1] = " "
            for direction in col:
                pretty_maze[2*y+1+direction[0]][2*x+1+direction[1]] = " "
    return pretty_maze

#Takes a converted maze and pretty prints it
def pretty_print(maze):
    for a in convert(maze):
        string = ""
        for b in a:
            string += b
        print(string)
    print("")

def pygame_print(maze):
    maze=convert(maze)
    S=(len(maze[0]),len(maze))
    E=[1440,900]
    t=[E[0]/S[0],E[1]/S[1]]
    RED=(255,0,0)
    GREEN=(0,255,0)
    pygame.init()
    screen = pygame.display.set_mode(E,FULLSCREEN)
    pygame.display.set_caption("Eller's Algorithm")
    for y,w in enumerate(maze):
        for x,v in enumerate(w):
            if v=="X":
                c=(0,0,0)
            else:
                c=(255,255,255)
            pygame.draw.rect(screen, c, (x*t[0],y*t[1],t[0],t[1]), 0)
    pygame.display.flip()
    done=False
    try:
        cdn=(1,1,0)
        while not done:
            cdn=solver(maze,cdn)
            x,y,r=cdn
            pygame.draw.rect(screen, GREEN, (x*t[0],y*t[1],t[0],t[1]), 0)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        done=True
    finally:
        pygame.quit()

    
def mega_pygame_print(maze):
    pygame.init()
    screen = pygame.display.set_mode((1440,900),FULLSCREEN)
    pygame.display.set_caption("Eller's Algorithm")
    for y,w in enumerate(maze):
        for x,v in enumerate(w):
            if v=="X":
                c=(0,0,0)
            else:
                c=(255,255,255)
            pygame.draw.rect(screen, c, (x,y,0,0), 0)
    pygame.display.flip()
    done=False
    try:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        done=True
    finally:
        pygame.quit()       

#Returns an empty maze of given size
def make_empty_maze(width, height):
    maze = [[[] for x in range(width)] for y in range(height)]
    return maze

#Recursive backtracker. 
#Looks at its neighbors randomly, if unvisitied, visit and recurse
def DFS(maze, coords=(0,0)):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    shuffle(directions)
    for direction in directions:
        new_coords = (coords[0] + direction[0], coords[1] + direction[1])
        if (0 <= new_coords[0] < len(maze)) and \
           (0 <= new_coords[1] < len(maze[0])) and \
           not maze[new_coords[0]][new_coords[1]]:
            maze[coords[0]][coords[1]].append(direction)
            maze[new_coords[0]][new_coords[1]].append((-direction[0], -direction[1]))
            DFS(maze, new_coords)
    return maze

#Very simple binary tree. Each node either points down or right.
def binary(maze):
    directions = [(1,0), (0,1)]
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if y == len(maze)-1 and x == len(row)-1:
                maze[y][x] = []
                return maze
            if y == len(maze)-1:
                direction = directions[1]
            elif x == len(row)-1:
                direction = directions[0]
            else:
                direction = choice(directions)
            maze[y][x] = [direction]

#Randomly splits maze vertically or horizontally. Connects the two halves and recurses.
def recursive_division(maze, direction=True):
    if len(maze) == 1 and len(maze[0]) == 1:
        return maze
    if direction:
        if len(maze) == 1:
            return recursive_division(maze, False)
        split = randint(1,len(maze)-1)
        first = maze[:split]
        second = maze[split:]
        recursive_division(first, False)
        recursive_division(second, False)
        connection = randint(0, len(maze[0])-1)
        first[-1][connection].append((1,0))
        second[0][connection].append((-1,0))
        return first+second
    else:
        if len(maze[0]) == 1:
            return recursive_division(maze, True)
        split = randint(1,len(maze[0])-1)
        first = [row[:split] for row in maze]
        second = [row[split:] for row in maze]
        recursive_division(first, True)
        recursive_division(second, True)
        connection = randint(0, len(maze)-1)
        first[connection][-1].append((0,1))
        second[connection][0].append((0,-1))
        return [a+b for a,b in zip(first, second)]

#Complicated but cool set-based algorithm
#Assign each cell to a set
#Loop through all the rows
#For each row, randomly connect neighboring cells if their sets are disjoint
#Union their sets
#For each element on the row, potentially connect to the cell below
#Each set must have at least one downward connection
#On the last row, union any disjoint sets
def eller(maze):
    sets = list(range(len(maze[0])))
    for y, row in enumerate(maze):
        for x, col in enumerate(row[:-1]):
            if ((row == maze[-1] or randint(0,1)) and sets[x] != sets[x+1]):
                sets[x+1] = sets[x]
                maze[y][x].append((0,1))
                maze[y][x+1].append((0,-1))
        if row != maze[-1]:
            next_sets = list(range(y*len(maze[0]), (y+1)*len(maze[0])))
            all_sets = set(sets)
            have_moved = set()
            while all_sets != have_moved:
                for x, col in enumerate(row):
                    if randint(0,1) and sets[x] not in have_moved:
                        have_moved.add(sets[x])
                        next_sets[x] = sets[x]
                        maze[y][x].append((1,0))
                        maze[y+1][x].append((-1,0))
            sets = next_sets
    return maze


def maze_solver(Grille,Coordonnées,Dimensions,screen,t):
    x,y,r=Coordonnées
    Longueur,Hauteur=Dimensions
    i=x
    j=y
    R=(r+1)%4
    Calcul=True
    if Calcul:
        i=x
        j=y
        if R==0:
            i=x-1
        if R==1:
            j=y-1
        if R==2:
            i=x+1
        if R==3:
            j=y+1
        if i>=0 and i<=Longueur-1 and j>=0 and j<=Hauteur-1:
            if Grille[j][i]==1:
                x=i
                y=j
                r=R
                Calcul=False
    if Calcul:
        i=x
        j=y
        if r==0:
            i=x-1
        if r==1:
            j=y-1
        if r==2:
            i=x+1
        if r==3:
            j=y+1
        if i>=0 and i<=Longueur-1 and j>=0 and j<=Hauteur-1:
            if Grille[j][i]==1:
                x=i
                y=j
                Calcul=False
    if Calcul:
        i=x
        j=y
        r=(r+3)%4
        Calcul=False
        
    pygame.draw.rect(screen, (255,0,0), (x*t[0],y*t[1],t[0],t[1]), 0) 
    pygame.display.flip()
    return (x,y,r)


def solver(maze,cdn):
    x,y,r=cdn
    R=(r+3)%4
    ncdn=move((x,y,R))
    if valid(maze,ncdn):
        return ncdn
    else:
        ncdn=(x,y,(r+1)%4)
        return ncdn
    

def move(cdn):
    x,y,r=cdn
    if r==0:
        x=x-1
    if r==1:
        y=y-1
    if r==2:
        x=x+1
    if r==3:
        y=y+1
    return (x,y,r)

def valid(maze,cdn):
    S=(len(maze[0]),len(maze))
    x,y,r=cdn
    if x<0 or x>=S[0] or y<0 or y>=S[1]:
        return False
    if maze[y][x]=="X":
        return False
    return True
    
    

width=720
height=450

width = 360
height = 225

width = 90
height = 56

#pretty_print(DFS(make_empty_maze(size,size)))
#pretty_print(binary(make_empty_maze(size,size)))
#pretty_print(recursive_division(make_empty_maze(size,size)))
#pretty_print(eller(make_empty_maze(size,size)))
pygame_print(eller(make_empty_maze(width,height)))
