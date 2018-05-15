'''
Created on 11 mai 2018

@author: nonoreve
'''
from engine.Tile import Tile


class Square:
    '''
    class Square represents a part of the Grid.
    -> french : une case
    '''

    def __init__(self, posX, posY):
        '''  Constructor '''
        self.tileValue = "EMPTY"
        self.posX = posX
        self.posY = posY
        
    def getTileValue(self):
        if self.tileValue == "EMPTY":
            return 0
        else:
            return self.tileValue.value
    
    def setTileValue(self, tileValue):
        self.tileValue = Tile(tileValue)
        
    def clearTile(self):
        self.tileValue = "EMPTY"
        
    def isEmpty(self):
        if self.tileValue == "EMPTY":
            return True
        else:
            return False