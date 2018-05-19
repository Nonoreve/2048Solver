'''
Created on 11 mai 2018

@author: nonoreve
'''
from engine.Grid import Grid
from random import randrange


class Game:
    '''
    class Game represents a single play (a try) not the game itself.
    -> french : une partie
    '''

    def __init__(self, nbColumn=4, nbRow=4):
        ''' Constructor. By default nbColumn and nbRow equals 4'''
        self.score = 0
        self.nbMoves = 0
        self.grid = Grid(nbColumn, nbRow)
        self.grid.spawnOneRandom()
        self.grid.spawnOneRandom()

    def play(self, moveDirection):
        ''' To call when a move is played. moveDirection is one of the constants defined in Grid (UP, DOWN...) '''
        self.grid.update(moveDirection)
        if randrange(10) >= 9:
            tileValue = 4
        else:
            tileValue = 2
        self.grid.spawnOneRandom(tileValue)
        
    def getTileValue(self, xCoord, yCoord):
        ''' To get the value of any tile on the grid '''
        return self.grid.getSquareAt(xCoord, yCoord).getTileValue()
