'''
Created on 17 mai 2018

@author: nonoreve
'''
from engine.Game import Game

def printGrid():
    print("grid : ")
    for y in range(0, 4):
        print("{} {} {} {}".format(game.getTileValue(0, y), game.getTileValue(1, y), game.getTileValue(2, y), game.getTileValue(3, y)))
    print()

if __name__ == '__main__':
    game = Game()
    printGrid()
    game.play("RIGHT")
    printGrid()
    game.play("UP")
    printGrid()
    game.play("LEFT")
    printGrid()
    game.play("DOWN")
    printGrid()
    game.play("RIGHT")
    printGrid()