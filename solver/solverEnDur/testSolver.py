from solver import *

maFen = GameGrid()
Solver = IA()

#i = 0
#while (i < 10) :

print(maFen.after(2000, Solver.simulation(matrix = maFen.matrix, maFen = maFen)))
    #i += 1

maFen.mainloop()
