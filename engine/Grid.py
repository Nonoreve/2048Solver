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

    def __init__(self, nbColumn, nbRow):
        ''' Constructor '''
        self.gridContent = []  # la liste principale
        self.nbColumn = nbColumn
        self.nbRow = nbRow
        for x in nbColumn:
            self.gridContent[x] = []  # on remplit chaque colonne par une liste vide
            for y in nbRow:
                self.gridContent[x][y] = Square()  # on remplit chaque case par une nouvelle instance de case

    def update(self, moveDirection):
        ''' update '''

    def spawnOneRandom(self, tileValue=2):
        ''' spawn a tile of the given value in a free square '''
        done = False
        while not done:
            randX = randrange(self.nbColumn)
            randY = randrange(self.nbRow)
            if self.isSquareEmpty(randX, randY):
                self.gridContent[randX][randY] = tileValue
                done = True
        
    def getSquareAt(self, posX, posY):
        return self.gridContent[posX][posY]
    
    def isSquareEmpty(self, xPos, yPos):
        return self.getSquareAt(xPos, yPos).isEmpty
