'''
Created on 11 mai 2018

@author: nonoreve
'''
import copy
from random import randrange

from engine.Grid import Grid
from pygame.examples.aliens import Score
import sys


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
        ''' To call when a move is played. 
        moveDirection is one of the constants defined in Grid (UP, DOWN...)
        return negative number in case of error (wrong moveDirection)
        if lose (grid full) return the score
        if win return True
        return False in other cases '''
        if self.canPlay(moveDirection):
            gameState = self.grid.update(moveDirection)
            self.score += gameState
            if randrange(10) >= 9:
                tileValue = 4
            else:
                tileValue = 2
            self.grid.spawnOneRandom(tileValue)
            if self.grid.isGridFull() and not self.canMove():
                #print("LOSE")
                return self.score
            else:
                y = 0
                winTileFound = False
                while not winTileFound and y < self.grid.nbRow:
                    x = 0
                    while not winTileFound and x < self.grid.nbRow:
                        winTileFound = self.getTileValue(x, y) == 2048
                        x += 1
                    y += 1
                return winTileFound
        else:
            sys.exit("Can't move that way")
        
    def getTileValue(self, xCoord, yCoord):
        ''' To get the value of any tile on the grid '''
        return self.grid.getSquareAt(xCoord, yCoord).getTileValue()
    
    def getScore(self):
        return self.score
    
    def getMaxTile(self):
        maxT = self.getTileValue(0, 0)
        for y in range(0, self.grid.nbColumn):
            for x in range(0, self.grid.nbRow):
                val = self.getTileValue(x, y)
                maxT = val if val > maxT else maxT
        return maxT
    def canPlay(self, moveDirection):
        ''' test if the move in the given direction will change something '''
        gridCopy = copy.deepcopy(self.grid)
        gridCopy.update(moveDirection)
        y = 0
        changeFound = False
        while not changeFound and y < self.grid.nbRow:
            x = 0
            while not changeFound and x < self.grid.nbRow:
                changeFound = gridCopy.getSquareAt(x, y).getTileValue() != self.grid.getSquareAt(x, y).getTileValue()
                x += 1
            y += 1
        return changeFound
    
    def canMove(self):
        ''' test if we can play in any direction '''
        return self.canPlay("UP") or self.canPlay("DOWN") or self.canPlay("LEFT")or self.canPlay("RIGHT")
