'''
Created on 11 mai 2018

@author: nonoreve
'''
from engine.Square import Square
from random import randrange


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
        if moveDirection == Grid.UP:
            # on parcourt la grille de haut en bas
            for y in range(0, self.nbRow - 1):
                # print("next row")
                for x in range(0, self.nbColumn):
                    if self.isSquareEmpty(x, y):
                        # si la case est vide, on cherche des tuiles a décaler
                        tileFound = False
                        y2 = y
                        while not tileFound and y2 < self.nbRow - 1:
                            y2 += 1
                            tileFound = not self.isSquareEmpty(x, y2)
                        if tileFound:
                            # print("found")
                            self.moveSquareTo(self.getSquareAt(x, y2), x, y)
                            
        elif moveDirection == Grid.DOWN:
            # on parcourt la grille de bas en haut
            for y in range(self.nbRow - 1, 0, -1):
                # print("next row")
                for x in range(0, self.nbColumn):
                    if self.isSquareEmpty(x, y):
                        # si la case est vide, on cherche des tuiles a décaler
                        tileFound = False
                        y2 = y
                        while not tileFound and y2 > 0:
                            y2 -= 1
                            tileFound = not self.isSquareEmpty(x, y2)
                        if tileFound:
                            # print("found")
                            self.moveSquareTo(self.getSquareAt(x, y2), x, y)
                            
        elif moveDirection == Grid.LEFT:
            # on parcourt la grille de gauche à droite
            for x in range(0, self.nbColumn - 1):
                # print("next row")
                for y in range(0, self.nbRow):
                    if self.isSquareEmpty(x, y):
                        # si la case est vide, on cherche des tuiles a décaler
                        tileFound = False
                        x2 = x
                        while not tileFound and x2 < self.nbColumn - 1:
                            x2 += 1
                            tileFound = not self.isSquareEmpty(x2, y)
                        if tileFound:
                            # print("found")
                            self.moveSquareTo(self.getSquareAt(x2, y), x, y)
                            
        elif moveDirection == Grid.RIGHT:
            # on parcourt la grille de droite à gauche
            for x in range(self.nbColumn - 1, 0, -1):
                # print("next row")
                for y in range(0, self.nbRow):
                    if self.isSquareEmpty(x, y):
                        # si la case est vide, on cherche des tuiles a décaler
                        tileFound = False
                        x2 = x
                        while not tileFound and x2 > 0:
                            x2 -= 1
                            tileFound = not self.isSquareEmpty(x2, y)
                        if tileFound:
                            # print("found")
                            self.moveSquareTo(self.getSquareAt(x2, y), x, y)
            
        else:
            print("Error : wrong moveDirection value")

    def spawnOneRandom(self, tileValue=2):
        ''' spawn a tile of the given value in a free square '''
        done = False
        while not done:
            randX = randrange(self.nbColumn)
            randY = randrange(self.nbRow)
            print("try to spawn at : x= {} y= {}".format(randX, randY))
            if self.isSquareEmpty(randX, randY):
                self.gridContent[randY][randX].setTileValue(tileValue)
                done = True
        
    def getSquareAt(self, posX, posY):
        return self.gridContent[posY][posX]
    
    def moveSquareTo(self, squareOrigin, newX, newY):
        """ place the tile in the given square at his new coordinates DO NOT CHECK IF EMPTY"""
        self.getSquareAt(newX, newY).setTileValue(squareOrigin.getTileValue())
        squareOrigin.clearTile()
    
    def isSquareEmpty(self, xPos, yPos):
        # print("x= {} y= {}".format(xPos, yPos))
        return self.getSquareAt(xPos, yPos).isEmpty()
    
    def isGridFull(self):
        y = 0
        while y < self.nbRow:
            pass
