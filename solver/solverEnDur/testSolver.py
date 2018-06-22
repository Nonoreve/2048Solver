from solver.solverEnDur.puzzle import *
from solver.solverEnDur.solver import *
from solver.solverEnDurHeusisticAligned.solver import *
from graphics import *

class Testeur():
    def __init__(self, maFen):
        self.maFenetreAModifier = maFen
        self.Demarrage = True
        
        
    def TestAlgorithmeSnake(self):
        if self.Demarrage :
            maFen = GameGrid()
            Solver = IA()
            
            perdu = False
            while not perdu:
                perdu = Solver.simulation(matrix = maFen.matrix, maFen = maFen) == 'lose'
                self.maFenetreAModifier.miseAJour(maFen)
            
            Demarrage = False
        
    def TestAlgorithmeWaves(self):
        if self.Demarrage :
            maFen = GameGrid()
            Solver = IAWaves()
            
            perdu = False
            while not perdu:
                perdu = Solver.simulation(matrix = maFen.matrix, maFen = maFen) == 'lose'
                self.maFenetreAModifier.miseAJour(maFen)
                
            Demarrage = False
            
    def RedemarrageTesteur(self):
        self.Demarrage = True
        
#Test()