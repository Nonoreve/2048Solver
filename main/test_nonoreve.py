'''
Created on 17 mai 2018

@author: nonoreve
'''
from engine.Game import Game

def printGrid():
    print("grid : ")
    for x in range(0, 4):
        print("{} {} {} {}".format(game.getTileValue(x, 0), game.getTileValue(x, 1), game.getTileValue(x, 2), game.getTileValue(x, 3)))
        

if __name__ == '__main__':
    game = Game()
    printGrid()
    game.play("UP")
    printGrid()