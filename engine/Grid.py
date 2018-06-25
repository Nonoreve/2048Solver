'''
Created on 11 mai 2018

@author: nonoreve
'''
from engine.Square import Square
from random import randrange
import sys


class Grid():
    '''
    class Grid represents the play arena.
    '''

    UP = "UP"
    DOWN = "DOWN"
    RIGHT = "RIGHT"
    LEFT = "LEFT"

    def __init__(self, nbColumn, nbRow):
        ''' Constructor '''
        self.gridContent = []  # la liste principale
        self.nbColumn = nbColumn
        self.nbRow = nbRow
        for y in range(0, nbRow):
            self.gridContent.append([])  # on remplit chaque colonne par une liste vide
            for x in range(0, nbColumn):
                self.gridContent[y].append(Square(x , y))  # on remplit chaque case par une nouvelle instance de case

    def update(self, moveDirection):
        ''' update '''
        bonus = 0
        if moveDirection == Grid.UP:
            # on parcourt la grille de haut en bas
            for y in range(0, self.nbRow - 1):
                # print("next row")
                for x in range(0, self.nbColumn):
                    y2 = y
                    tileFound = False
                    # on cherche la premiere tuile dans la colonne
                    while not tileFound and y2 < self.nbRow:
                        tileFound = not self.isSquareEmpty(x, y2)
                        y2 += 1
                    if tileFound:
                        # print("found")
                        y2 -= 1
                        y3 = y2
                        tileFound = False
                        # on cherche une deuxiemme
                        while not tileFound and y3 < self.nbRow - 1:
                            y3 += 1
                            tileFound = not self.isSquareEmpty(x, y3)
                            # print("{} {} {} {} {}".format(tileFound, y2, y3, self.getSquareAt(x, y2).getTileValue(), self.getSquareAt(x, y3).getTileValue()))
                        if tileFound:
                            # si la deuxiemme est de meme valeur
                            if self.getSquareAt(x, y2).getTileValue() == self.getSquareAt(x, y3).getTileValue():
                                #print("merge : {}, {}".format(x, y2))
                                self.getSquareAt(x, y2).setTileValue(self.getSquareAt(x, y2).getTileValue() * 2)
                                self.getSquareAt(x, y3).clearTile()
                                bonus = self.getSquareAt(x, y2).getTileValue()
                        if self.isSquareEmpty(x, y):
                            #print("move")
                            # si la case est vide, on cherche des tuiles a décaler
                            self.moveTileTo(self.getSquareAt(x, y2), x, y)
            return bonus
        elif moveDirection == Grid.DOWN:
            # on parcourt la grille de bas en haut
            for y in range(self.nbRow - 1, 0, -1):
                for x in range(0, self.nbColumn):
                    y2 = y
                    tileFound = False
                    while not tileFound and y2 >= 0:
                        tileFound = not self.isSquareEmpty(x, y2)
                        y2 -= 1
                    if tileFound:
                        y2 += 1
                        y3 = y2
                        tileFound = False
                        # on cherche une deuxiemme de meme valeur
                        while not tileFound and y3 > 0:
                            y3 -= 1
                            tileFound = not self.isSquareEmpty(x, y3)
                        if tileFound:
                            if self.getSquareAt(x, y2).getTileValue() == self.getSquareAt(x, y3).getTileValue():
                                self.getSquareAt(x, y2).setTileValue(self.getSquareAt(x, y2).getTileValue() * 2)
                                self.getSquareAt(x, y3).clearTile()
                                bonus = self.getSquareAt(x, y2).getTileValue()
                        if self.isSquareEmpty(x, y):
                            # si la case est vide, on cherche des tuiles a décaler
                            self.moveTileTo(self.getSquareAt(x, y2), x, y)
            return bonus
        elif moveDirection == Grid.LEFT:
            # on parcourt la grille de gauche à droite
            for x in range(0, self.nbColumn - 1):
                for y in range(0, self.nbRow):
                    x2 = x
                    tileFound = False
                    while not tileFound and x2 < self.nbColumn:
                        tileFound = not self.isSquareEmpty(x2, y)
                        x2 += 1
                    if tileFound:
                        x2 -= 1
                        x3 = x2
                        tileFound = False
                        while not tileFound and x3 < self.nbColumn - 1:
                            x3 += 1
                            tileFound = not self.isSquareEmpty(x3, y)
                        if tileFound:
                            if self.getSquareAt(x2, y).getTileValue() == self.getSquareAt(x3, y).getTileValue():
                                self.getSquareAt(x2, y).setTileValue(self.getSquareAt(x2, y).getTileValue() * 2)
                                self.getSquareAt(x3, y).clearTile()
                                bonus = self.getSquareAt(x2, y).getTileValue()
                        if self.isSquareEmpty(x, y):
                            self.moveTileTo(self.getSquareAt(x2, y), x, y)
            return bonus
        elif moveDirection == Grid.RIGHT:
            # on parcourt la grille de droite à gauche
            for x in range(self.nbColumn - 1, 0, -1):
                for y in range(0, self.nbRow):
                    x2 = x
                    tileFound = False
                    while not tileFound and x2 >= 0:
                        tileFound = not self.isSquareEmpty(x2, y)
                        x2 -= 1
                    if tileFound:
                        x2 += 1
                        x3 = x2
                        tileFound = False
                        while not tileFound and x3 > 0:
                            x3 -= 1
                            tileFound = not self.isSquareEmpty(x3, y)
                        if tileFound:
                            if self.getSquareAt(x2, y).getTileValue() == self.getSquareAt(x3, y).getTileValue():
                                self.getSquareAt(x2, y).setTileValue(self.getSquareAt(x2, y).getTileValue() * 2)
                                self.getSquareAt(x3, y).clearTile()
                                bonus = self.getSquareAt(x2, y).getTileValue()
                        if self.isSquareEmpty(x, y):
                            self.moveTileTo(self.getSquareAt(x2, y), x, y)
            return bonus
        else:
            sys.exit("Error : wrong moveDirection value")

    def spawnOneRandom(self, tileValue=2):
        ''' spawn a tile of the given value in a free square '''
        done = False
        while not done:
            randX = randrange(self.nbColumn)
            randY = randrange(self.nbRow)
            #print("try to spawn at : x= {} y= {}".format(randX, randY))
            if self.isSquareEmpty(randX, randY):
                self.gridContent[randY][randX].setTileValue(tileValue)
                done = True
        
    def getSquareAt(self, posX, posY):
        return self.gridContent[posY][posX]
    
    def moveTileTo(self, squareOrigin, newX, newY):
        """ place the tile in the given square at his new coordinates DO NOT CHECK IF EMPTY"""
        self.getSquareAt(newX, newY).setTileValue(squareOrigin.getTileValue())
        squareOrigin.clearTile()
    
    def isSquareEmpty(self, xPos, yPos):
        return self.getSquareAt(xPos, yPos).isEmpty()
    
    def isGridFull(self):
        y = 0
        emptyFound = False
        while not emptyFound and y < self.nbRow:
            x = 0
            while not emptyFound and x < self.nbRow:
                emptyFound = self.isSquareEmpty(x, y)
                x += 1
            y += 1
        return not emptyFound
