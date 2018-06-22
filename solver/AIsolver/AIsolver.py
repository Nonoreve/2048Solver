'''
Created on 5 juin 2018

@author: nonoreve
'''

from random import choice
import random
import time

from engine.Game import Game
from solver.AIsolver.GeneticNeuralNetwork import NeuralNetwork


def getKey(item):
    return item[1]


def error(outputs, expectedResults):
    """ compute the error of the givn outputs """
    assert len(outputs) == len(expectedResults), "Incorrect amount of outputs."
    error = 0
    for i in range(0, len(outputs)):
        error += (outputs[i] - expectedResults[i]) ** 2
    return error


def flatTab(tabOfTabOfTab):
    return [item for sublist in tabOfTabOfTab for subsublist in sublist for item in subsublist]


def sliceTab(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, tab):
    tabOfTabOfTab = []
    # tabOfTabOfTab = [[[1 for _ in range(0, nbInputs)] for _ in range(0, nbNeuronPerHL)]]
    tab = tab[nbInputs * nbNeuronPerHL:]
    # print(tab)
    i = 0
    for _ in range(0, nbHiddenLayers):
        neuronsTab = []
        for _ in range(0, nbNeuronPerHL):
            weightsTab = []
            for _ in range(0, nbNeuronPerHL + 1):
                weightsTab.append(tab[i])
                i += 1
            neuronsTab.append(weightsTab)
        tabOfTabOfTab.append(neuronsTab)
    subtab = []
    for _ in range(0, nbOutputs):
        subsubtab = []
        for _ in range(0, nbNeuronPerHL + 1):
            subsubtab.append(tab[i])
            i += 1
        subtab.append(subsubtab)
    tabOfTabOfTab.append(subtab)
    return tabOfTabOfTab


MOVES = ["UP", "DOWN", "RIGHT", "LEFT"]
# 06 84 23 07 13


def playTest(neuralNet):
    game = Game()
    while True:
        gridInput = [game.getTileValue(x, y) for y in range(0, 4) for x in range(0, 4)]
        # print("input " + str(gridInput))
        tabOut = neuralNet.update(gridInput)
        # print("output " + str(tabOut))
        tupOut = [(i, tabOut[i]) for i in range(0, len(tabOut))]
        # print("tuples " + str(tupOut))
        tupOut.sort(key=getKey, reverse=True)
        prior = 0
        play = MOVES[tupOut[prior][0]]
        while not game.canPlay(play):
            prior += 1
            play = MOVES[tupOut[prior][0]]
        # print(play)
        if play == "STOP":
            break
        gameState = game.play(play)
        if type(gameState) == int:
            # print("final grid " + str(gridInput))
            return gameState
        elif gameState == True:
            print("\n ! ! ! ! ! WIN ! ! ! ! ! \n")


if __name__ == '__main__':
    # the save files
    fitnessFile = open("fitnessFile.save", "a")
    fitnessFile.write(time.strftime('%d/%m/%y %H:%M', time.localtime()) + '\n')
    fitnessFile.flush()
    weightsFile = open("weightsFile.save", "a")
    weightsFile.write(time.strftime('%d/%m/%y %H:%M', time.localtime()) + '\n')
    weightsFile.flush()
    # the current living network population
    population = []
    # create the original ancestors
    POPULATION_SIZE = 600
    nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers = 16, 4, 10, 3
    nbWeights = nbInputs * (nbNeuronPerHL + 1) + (nbNeuronPerHL ** 2 + nbNeuronPerHL) * nbHiddenLayers + (nbNeuronPerHL + 1) * nbOutputs
    # print("ORIGINAL ANCESTORS\n")
    for i in range(0, POPULATION_SIZE):
        # makes a flat tab with enough values
        weightsTab = []
        for _ in range(0, nbWeights):
            weightsTab.append(random.random())
        population.append(NeuralNetwork(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, sliceTab(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, weightsTab)))
        # print(str(population[i]) + '\n')
    
    for generation in range(0, 100):
        print("GENERATION {}".format(generation + 1))
        weightsFile.write("GENERATION {}".format(generation + 1) + '\n')
        weightsFile.flush()
        # compute and sort the results
        results = []
        #for i in range(0, POPULATION_SIZE):
        #    fitness = playTest(population[i])
        #    results.append((i, fitness))
        #    print("fitness of num°{} = {}".format(i, fitness))
        #    fitnessFile.write(str(fitness) + '\n')
        #    fitnessFile.flush()
        
        # test all the network using multiprocessing
        
        # # print(results)
        results.sort(key=getKey, reverse=True)
        # # print(results)
        
        # kill the bad ones (the bottom half)
        results = results[:POPULATION_SIZE // 2]
        # print("selected ones " + str(results))
        survivors = []
        generationLoss = 0
        for i, x in results:
            survivors.append(population[i])
            generationLoss += x
        generationLoss /= len(results)
        print("average fitness = " + str(generationLoss))
        fitnessFile.write("G" + str(generationLoss) + '\n')
        fitnessFile.flush()
        # print(population)
        # print(survivors)
        
        # now reproduce the survivors
        nextgen = survivors
        for i in range(0, POPULATION_SIZE - len(survivors)):
            newWeights = []
            # for each new network we pick a random survivor
            chosen = choice(survivors)
            survivorGenes = flatTab(chosen.get_weights())
            weightsFile.write("s" + str(survivorGenes[nbInputs * (nbNeuronPerHL + 1):]) + '\n')
            weightsFile.flush()
            for weight in survivorGenes:
                newWeights.append(weight + ((random.random() - 0.5) * (100 / generationLoss)))
            weightsFile.write("n" + str(newWeights[nbInputs * (nbNeuronPerHL + 1):]) + '\n')
            weightsFile.flush()
            slicedTab = sliceTab(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, newWeights)
            nextgen.append(NeuralNetwork(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, slicedTab))
            # print(nextgen[-1])
        population = nextgen
    print("OVER " + str(generationLoss))
    fitnessFile.close()
    weightsFile.close()
