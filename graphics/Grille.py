'''
Created on 18 mai 2018

@author: willi
'''

from graphics import UsefulVariables
from tkinter import *
class Grille(Frame):
    '''
    classdocs
    definition of the graphic array of tiles
    '''
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master=master, cnf=cnf, **kw)
        iniGrille()
        
        
    def iniGrille(self):
        i = 0
        while (i < UsefulVariables.nbTiles):
            self.append(Frame(self, bg = "red", height = 20, width = 20))
            self.pack()
            
            i += 1
