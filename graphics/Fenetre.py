'''
Created on 18 mai 2018
@author: willi

'''
from tkinter import *
from graphics import *
class Fenetre(Tk):
    '''
    classdocs
    
    Definition of the graphics for the 2048
    '''
    """fenetre.geometry("600x800+300+0")"""
    
    ArrayTiles = Grille()

    def initialisationFenetre(self):
        lblTitre = Label(self, text="2048")
        lblTitre.pack()
        lblIntro = Label(self, text="Bienvenue dans le Jeu du 2048")
        lblIntro.pack()
        lblRegles = Label(self, text = "Pour jouer : ...")
        lblRegles.pack()
        
        ArrayTiles.pack()
        self.frame()
        

