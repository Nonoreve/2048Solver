import itertools
import math
from random import *

from pip._vendor.urllib3.connectionpool import xrange

from logic import *
from puzzle import *


class IA:
    
#Pour deplacer dans un sens, utiliser la procedure maFen.key_downSim(KEY_DIRECTION)
    def simulation(self, matrix, maFen):
        self.aiplay(maFen, matrix)
        print('Fin du programme')
    
    def aimove(self, matrix , maFen) :
        def fitness(matrix):
            """
            Returns the heuristic value of b
            Snake refers to the "snake line pattern" (http://tinyurl.com/l9bstk6)
            Here we only evaluate one direction; we award more points if high valued tiles
            occur along this path. We penalize t he board for not having
            the highest valued tile in the lower left corner
            """
            if game_state(matrix) == 'lose' :
                print("rate")
                return -float("inf")
            

            snake = [] 
            sortedSnake = []           
            """Mise de toutes les valeurs de la grille dans une liste d'entiers 1D """
            for i, col in enumerate(zip(*matrix)):
                snake.extend(reversed(col) if i % 2 == 0 else col)
                #sortedSnake.extend(reversed(col) if i % 2 == 0 else col)
            """m prend la valeur maximale de la liste"""
            m = max(snake)
            #sortedSnake.sort(reverse = True)
            #print(sortedSnake)
            print(snake)
            #smooth = - self.eval_smoothness(matrix)
            #valeurs = []
            #print(max(snake))
            
            #valeurARetourner = 0
            #for i in range(0,15) :
            #    valeurARetourner += snake[i] * valeurs[i]
            #return (valeurARetourner) #- \
                #math.pow((matrix[3][0] != m)*abs(matrix[3][0] - m), 2))
             
             
            #def mulArr(arr1, arr2):
                #return sum([arr1[i][j]*arr2[i][j] for i in xrange(len(arr1)) for j in xrange(len(arr1))])
            
            #return mulArr(matrix, valeurs) - \ b  
                #math.pow((matrix[3][0] != m)*abs(matrix[3][0] - m), 2)

            return ( sum(x/10**n for n, x in enumerate(snake)) - \
                math.pow((matrix[3][0] != m)*abs(matrix[3][0] - m), 2))
            
            #valuation = 0
            #for i in range(0,15):
            #    if snake[i] == sortedSnake[i]:
             #       valuation += math.pow(sortedSnake[i],10/10**(i+1))
             #   else :
            #        valuation -= math.pow(sortedSnake[i],10/10**(i+1))**2
            #print(valuation)
            #return valuation
            #return smooth

                   
                   
        def search(matrix, d, move=False):
            """
            Performs expectimax search on a given configuration to
            specified depth (d).
            Algorithm details:
               - if the AI needs to move, make each child move,
                 recurse, return the maximum fitness value
               - if it is not the AI's turn, form all
                 possible child spawns, and return their weighted average 
                 as that node's evaluation   
            """
            if d == 0 or (move and game_state(matrix) == 'lose'):
                return fitness(matrix)
                                
            alpha = fitness(matrix)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
            if move:
                for _, child in maFen.actions():
                    return max(alpha, search(child[0], d-1, False))
            else:
                alpha = 0
                zeros = [(i,j) for i,j in itertools.product(range(4), range(4)) if matrix[i][j] == 0]
                #print("z : ")
                #print(zeros)
                for i, j in zeros:
                    c1 = [[x for x in row] for row in matrix]
                    #c2 = [[x for x in row] for row in matrix]
                    c1[i][j] = 2
                    #c2[i][j] = 4
                    #le 0.9 et le 0.1 sont pour les proportions de 2 ou de 4
                    #alpha += .9*search(c1, d-1, True)/len(zeros) + \
                              #.1*search(c2, d-1, True)/len(zeros)
                    alpha += search(c1, d-1, True)/len(zeros)

            return alpha
        
        return [(action, search(child[0], d=5)) for action ,child in (maFen.actions())]
            #Prochaine intervention : cette procedure TESTE les valeurs possibles, ainsi, il faut envoyer dans le return une grille de test
            #On doit donc ecrire une procedure qui genere une fausse grille
    def aiplay(self, maFen, matrix):
        """
        Runs the game playing the move that determined
        by aimove.
        """
        while game_state(maFen.matrix) != 'lose':


            action = max(self.aimove(maFen = maFen, matrix = maFen.matrix), key = lambda x: x[1])[0]
            if action == "left" : 
                maFen.key_downSim(KEY_LEFT)
                print("left")
            if action == "right": 
                maFen.key_downSim(KEY_RIGHT)
                print("right")
            if action == "up"   :
                maFen.key_downSim(KEY_UP)
                print("up")
            if action == "down" : 
                maFen.key_downSim(KEY_DOWN)
                print("down")
            #print(maFen.matrix)

        return maFen.matrix
        
        