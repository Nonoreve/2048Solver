'''
Created on 17 mai 2018

@author: nonoreve
'''
from engine.Game import Game


def printGrid():
    print("grid : ")
    for y in range(0, 4):
        print("        {} {} {} {}".format(game.getTileValue(0, y), game.getTileValue(1, y), game.getTileValue(2, y), game.getTileValue(3, y)))
    print()

# adapte la largeur des colonne fonction de la taille des nombres
def printPrettyGrid():
    print("\ngrid : ")
    for y in range(0, 4):
        for x in range(0, 4):
            y2 = 0
            bigNbFound = False
            # on cherche des nombres à plus d'un digit
            while not bigNbFound and y2 < 4:
                bigNbFound = game.getTileValue(x, y2) > 9
                y2 += 1
            if bigNbFound:
                y3 = 0
                bigNbFound = False
                # on cherche des nombres a plus de 2 digit
                while not bigNbFound and y3 < 4:
                    bigNbFound = game.getTileValue(x, y3) > 99
                    y3 += 1
                if bigNbFound:
                    if game.getTileValue(x, y) > 99:
                        print("{} ".format(game.getTileValue(x, y)), end='')
                    elif game.getTileValue(x, y) > 9:
                        print("{}  ".format(game.getTileValue(x, y)), end='')
                    else:
                        print("{}   ".format(game.getTileValue(x, y)), end='')
                else:
                    if game.getTileValue(x, y) > 9:
                        print("{} ".format(game.getTileValue(x, y)), end='')
                    else:
                        print("{}  ".format(game.getTileValue(x, y)), end='')
            else:
                print("{} ".format(game.getTileValue(x, y)), end='')
        print()
    print()


if __name__ == '__main__':
    game = Game()
    while True:
        printPrettyGrid()
        # printGrid()
        # on recupere input en majuscule
        play = input("please play :").upper()
        if play == "STOP":
            break
        gameState = game.play(play)
        if gameState == 666:
            printPrettyGrid()
            break
        elif gameState == True:
            print("WIN")
