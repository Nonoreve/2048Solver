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
        self.innerTile = "EMPTY"
        self.posX = posX
        self.posY = posY
        
    def getTileValue(self):
        if self.innerTile == "EMPTY":
            return 0
        else:
            #print("tileVal = {}".format(self.innerTile.value))
            return self.innerTile.value
    
    def setTileValue(self, tileValue):
        self.innerTile = Tile(tileValue)
        
    def clearTile(self):
        self.innerTile = "EMPTY"
        
    def isEmpty(self):
        if self.innerTile == "EMPTY":
            #print("EMPTY : x= {} y= {}".format(self.posX, self.posY))
            return True
        else:
            #print("NOT empty -> {} : x= {} y= {}".format(self.getTileValue(), self.posX, self.posY))
            return False
