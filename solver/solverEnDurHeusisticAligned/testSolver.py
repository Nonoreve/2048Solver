from solver import *

maFen = GameGrid()
Solver = IAWaves()


maFen.after(2000, Solver.simulation(matrix = maFen.matrix, maFen = maFen))


maFen.mainloop()

