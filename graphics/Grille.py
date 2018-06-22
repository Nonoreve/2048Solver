'''
Created on 18 mai 2018

@author: willi
'''



from graphics.Fenetre import *
from graphics.Tuile import *
from tkinter import *
from engine.Game import *
class Grille(Frame):
    '''
    classdocs
    definition of the graphic array of tiles
    '''
    '''
    def __init__(self, fenetre, height, width): 
        Frame.__init__(self, fenetre) 
        self.numberLines = height 
        self.numberColumns = width 
        self.data = list() 
        for i in range(self.numberLines): 
            line = list() 
            for j in range(self.numberColumns): 
                cell = Entry(self, height = 20, width = 20) 
                cell.insert(0, 0) 
                line.append(cell) 
                cell.grid(row = i, column = j) 
            self.data.append(line) 
  
    '''
    
    def __init__(self, fenetre, height, width):
        self.texte = "-family {DejaVu Sans} -size 40 -weight normal -slant roman -underline 0 -overstrike 0 "

        Frame.__init__(self, fenetre)
        self.nbLines = height
        self.nbColumns = width
        self.data = list()

        for i in range(self.nbLines):
            line = list()
            for j in range(self.nbColumns):
                cell = Tuile(self, valeur = "0", height = 150, width = 150, bg = 'white', bd = 10, highlightcolor="grey", highlightbackground="grey",highlightthickness=10, font = self.texte,row = i, column = j)
                cell.grid(row = i, column = j)
                line.append(cell.valeur)
            self.data.append(line)
                
    def MiseAJour(self, game):
        #self.data = grilleJeu
        for w in self.winfo_children():
            w.destroy()
        for j in range(self.nbLines):
            for i in range(self.nbColumns):
                cell = Tuile(self, valeur = game.getTileValue(i,j), height = 150, width = 150, bg = 'white', bd = 10, highlightcolor="grey", highlightbackground="grey",highlightthickness=10, font = self.texte,row = i, column = j)
                cell.grid(row = j, column = i)
                