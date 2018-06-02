'''
Created on 18 mai 2018
@author: willi

'''
from tkinter import *

from graphics.Grille import *

class Fenetre():
    '''
    classdocs
    
    Definition of the graphics for the 2048
    '''
    """fenetre.geometry("600x800+300+0")"""



    def __init__(self):
        #Definition de la police
        self.titre = "-family {DejaVu Sans} -size 32 -weight normal -slant roman -underline 0 -overstrike 0"
        self.texte = "-family {DejaVu Sans} -size 18 -weight normal -slant roman -underline 0 -overstrike 0"
        
        #Declaration de la fenetre
        self.FenetrePrincipale = Tk()

        #Declaration du titre
        lblTitre = Label(self.FenetrePrincipale, text="2048")
        lblTitre.configure(font = self.titre)
        lblTitre.pack()
        
        #Partie statistiques
        self.pnlStats = Frame(self.FenetrePrincipale)
        self.pnlStats.pack()
        
        lblScore = Label(self.pnlStats, text = "Votre Score :", font = self.texte, padx = 10)
        lblScore.grid(row = 0, column = 0)
        
        #lbl A Actualiser a chaque changement de score
        self.lblIntScore = Label(self.pnlStats, text = "0", font = self.texte, padx = 10)
        self.lblIntScore.grid(row = 1, column = 0)
        
        lblMeilleurScore = Label(self.pnlStats, text = "Meilleur Score :", font = self.texte, padx = 10)
        lblMeilleurScore.grid(row = 0, column = 1)
        
        #lbl a actualiser a chaque meilleur score
        lblIntMeil = Label(self.pnlStats, text = "0", font = self.texte, padx = 10)
        lblIntMeil.grid(row = 1, column = 1)

        
        lblIntro = Label(self.FenetrePrincipale, text="Bienvenue dans le Jeu du 2048")
        lblIntro.pack()
        lblIntro.configure(font = self.texte)

        
        #La Grille
        self.pnlArrayTiles = Frame(self.FenetrePrincipale, bg = "Black")
        self.pnlArrayTiles.pack()
        pnlFictif = Frame(self.pnlArrayTiles)
        pnlFictif.grid()
        
        test = []
        for i in range(4):
            test.append([4]*4)
            
            
        self.ArrayTiles = Grille(self.pnlArrayTiles, 4, 4)
        self.ArrayTiles.grid()
        
        self.ArrayTiles.MiseAJour(test)
        
        self.frBtns = Frame(self.FenetrePrincipale, pady = 15)
        self.frBtns.pack()
        
        btnJouer = Button(self.frBtns, text="Jouer", commande=self.FenetrePrincipale.quit())
        btnJouer.grid(row = 0, column = 0)
        btnJouer.configure(font = self.texte)
        
        btnRecommencer = Button(self.frBtns, text ="Recommencer", commande = self.FenetrePrincipale.quit())
        btnRecommencer.grid(row = 0, column = 1)
        btnRecommencer.configure(font = self.texte)
        
        btnResDur = Button(self.frBtns, text ="Algorithme en dur", commande = self.FenetrePrincipale.quit())
        btnResDur.grid(row = 0, column = 2)
        btnResDur.configure(font = self.texte)
        
        btnResLearn = Button(self.frBtns, text ="Algorithme Deep Learning", commande = self.FenetrePrincipale.quit())
        btnResLearn.grid(row = 0, column = 3)
        btnResLearn.configure(font = self.texte)

        lblRegles = Label(self.FenetrePrincipale, text = "Pour jouer : ...")
        lblRegles.pack()
        lblRegles.configure(font = self.texte)

        self.FenetrePrincipale.frame()

    def executeFenetre(self):
        self.FenetrePrincipale.mainloop()