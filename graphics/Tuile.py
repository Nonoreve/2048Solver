'''
Created on 18 mai 2018

@author: willi
'''
from tkinter import *
from turtledemo.nim import COLOR
class Tuile(Frame):
    '''
    classdocs
    '
    '''
    def __init__(self, panelDessus, valeur, height, width, bg, bd, highlightcolor, highlightbackground,highlightthickness,font, row , column):
        Frame.__init__(self, panelDessus,  height = height, width  = width, bg = bg, bd = 10, highlightcolor= highlightcolor, highlightbackground= highlightbackground ,highlightthickness = highlightthickness)
        self.valeur = int(valeur)
        self.grid()
        self.lblAffichage = Label(self, text=self.valeur)
        self.lblAffichage.grid()