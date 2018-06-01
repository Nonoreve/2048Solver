import math
import itertools
from random import *

from logic import *
from puzzle import *


class IA:
    
#Pour déplacer dans un sens, utiliser la procedure maFen.key_downSim(KEY_<DIRECTION>)
    def simulation(self, maFen):
        self.aiplay(maFen)
    
    def aimove(self, maFen) :
        def fitness(self, maFen):
            """
            Returns the heuristic value of b
            Snake refers to the "snake line pattern" (http://tinyurl.com/l9bstk6)
            Here we only evaluate one direction; we award more points if high valued tiles
            occur along this path. We penalize the board for not having
            the highest valued tile in the lower left corner
            """
            if game_state == 'lose' :
                return -float("inf")
            
            snake = []
            for i, col in enumerate(zip(*maFen.grid_cells)):
                snake.extend(reversed(col) if i % 2 == 0 else col)
    
            m = max(snake)
            return sum(x/10**n for n, x in enumerate(snake)) - \
                   math.pow((maFen.grid_cells[3][0] != m)*abs(maFen.grid_cells[3][0] - m), 2)
                   
                
        
        
        def search(self, maFen, d, move=False):
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
            if d == 0 or (move and game_state == 'lose'):
                return fitness(maFen)
    
            alpha = fitness(maFen)
            if move:
                for _, child in maFen.commands:
                    return max(alpha, search(child, d-1, False))
            else:
                alpha = 0
                zeros = [(i,j) for i,j in itertools.product(range(4), range(4)) if maFen.grid_cells[i][j] == 0]
                for i, j in zeros:
                    c1 = [[x for x in row] for row in maFen.grid_cells]
                    c2 = [[x for x in row] for row in maFen.grid_cells]
                    c1[i][j] = 2
                    c2[i][j] = 4
                    alpha += .9*search(c1, d-1, True)/len(zeros) + \
                             .1*search(c2, d-1, True)/len(zeros)
            return alpha
        return [(action, search(child, 5)) for action ,child in maFen.commands]
            #Prochaine intervention : cette procedure TESTE les valeurs possibles, ainsi, il faut envoyer dans le return une grille de test
            #On doit donc ecrire une procedure qui genere une fausse grille
    def aiplay(self, maFen):
        """
        Runs the game playing the move that determined
        by aimove.
        """
        while True:
            #print(Game.string(b) + "\n")
            action = max(self.aimove(maFen), key = lambda x: x[1])[0]
            
            if action == "left" : maFen.key_downSim(KEY_LEFT)
            if action == "right": maFen.key_downSim(KEY_RIGHT)
            if action == "up"   : maFen.key_downSim(KEY_UP)
            if action == "down" : maFen.key_downSim(KEY_DOWN)    
            break 
           # b = Game.spawn(b, 1)
            #if Game.over(b):
             #   m = max(x for row in b for x in row)
               # print("game over...best was %s" %m)
               # print(Game.string(b))

    
        
        
        