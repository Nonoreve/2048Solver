'''
Created on 18 mai 2018

@author: willi
'''
from graphics.Fenetre import Fenetre
from engine.Game import *

game = Game()
FormPrincipale = Fenetre(game)




def printGrid():
    print("grid : ")
    for y in range(0, 4):
        print("{} {} {} {}".format(game.getTileValue(0, y), game.getTileValue(1, y), game.getTileValue(2, y), game.getTileValue(3, y)))
    print()

def gestionInput(event):
    touche = event.keysym
    print(touche)
    if touche == "Up":
        game.play("UP")
    if touche == "Down":
        game.play("DOWN")
    if touche == "Right":
        game.play("RIGHT")
    if touche == "Left":
        game.play("LEFT")
    FormPrincipale.miseAJour(game)
    printGrid()

FormPrincipale.FenetrePrincipale.bind("<Key>", gestionInput)
FormPrincipale.FenetrePrincipale.mainloop()
input('Appuyez sur ENTREE pour continuer...')
