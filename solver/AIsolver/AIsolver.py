'''
Created on 5 juin 2018

@author: nonoreve
'''

import math
from multiprocessing import Queue, Process
import pdb
import random
import time

from engine.Game import Game
from solver.AIsolver.GeneticNeuralNetwork import NeuralNetwork


def getKey(item):
    return item[1]


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


def translatedSigmoid(self, activation):
        # the activation function
        try:
            return 1 / (1 + math.e ** (-activation + 9))
        except OverflowError:
            return float("inf")


MOVES = ["UP", "DOWN", "RIGHT", "LEFT"]
# 06 84 23 07 13


def playTest(queue, neuralNet):
    game = Game()
    while True:
        gridVal = [game.getTileValue(x, y) for y in range(0, 4) for x in range(0, 4)]
        # print("input " + str(gridInput) + str(os.getpid()))
        # normalizing the inputs
        gridInput = []
        for val in gridVal:
            # we search the power of two
            n = 0
            while 2 ** n < val:
                n += 1
            gridInput.append(n)
        gridInput = [gridInput[i] / 11 for i in range(0, len(gridInput))]
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
        gameState = game.play(play)
        if type(gameState) == int:
            print("final grid " + str(gridVal))
            gameState += game.getMaxTile() ** 2
            queue.put(gameState)
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
    firstGenFitness = None
    # the current living network population
    population = []
    # create the original ancestors
    POPULATION_SIZE = 700
    NB_GENERATIONS = 500
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
    
    for generation in range(0, NB_GENERATIONS):
        print("GENERATION {}".format(generation + 1))
        weightsFile.write("GENERATION {}".format(generation + 1) + '\n')
        weightsFile.flush()
        # compute and sort the results
        results = []
        queue = Queue()
        processes = []
        # pdb.set_trace()
        for i in range(0, POPULATION_SIZE):
        #    fitness = playTest(population[i])
            # test all the networks using multiprocessing
            p = Process(target=playTest, args=(queue, population[i]))
            p.start()
            processes.append(p)
        for i in range(0, POPULATION_SIZE):
            processes[i].join()
            fitness = queue.get(block=False)
            results.append((i, fitness))
            print("fitness of num°{} = {}".format(i, fitness))
            fitnessFile.write(str(fitness) + '\n')
            fitnessFile.flush()
        
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
        firstGenFitness = generationLoss if firstGenFitness == None else firstGenFitness
        print("average fitness = " + str(generationLoss))
        fitnessFile.write("G" + str(generationLoss) + '\n')
        fitnessFile.flush()
        # print(population)
        # print(survivors)
        if generation == NB_GENERATIONS:
            break
        # now reproduce the survivors
        population = survivors
        for i in range(0, POPULATION_SIZE - len(survivors)):
            newWeights = []
            # for each new network we pick a random survivor
            chosenId = [random.randint(-1, POPULATION_SIZE // 2 - 1), random.randint(-1, POPULATION_SIZE // 2 - 1)]
            # print(chosenId)
            # print(results[chosenId])
            chosen = [survivors[chosenId[0]], survivors[chosenId[1]]]
            momGenes = flatTab(chosen[0].get_weights())
            dadGenes = flatTab(chosen[1].get_weights())
            weightsFile.write("s1" + str(momGenes[nbInputs * (nbNeuronPerHL + 1):]) + '\n')
            weightsFile.flush()
            weightsFile.write("s2" + str(dadGenes[nbInputs * (nbNeuronPerHL + 1):]) + '\n')
            weightsFile.flush()
            for i in range(0, len(momGenes)):
                # newWeights.append(weight + ((random.random() - 0.5) * (100 / results[chosenId][1])))
                weight = (momGenes[i] + dadGenes[i]) / 2
                mutation = (random.random() - 0.5) * 1000 / ((results[chosenId[0]][1] + results[chosenId[1]][1]) / 2)
                newWeights.append(weight + mutation)
            weightsFile.write("n" + str(newWeights[nbInputs * (nbNeuronPerHL + 1):]) + '\n')
            weightsFile.flush()
            slicedTab = sliceTab(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, newWeights)
            population.append(NeuralNetwork(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, slicedTab))
            # print(nextgen[-1])
    print("OVER\nfirst gen fitness=" + str(firstGenFitness) + " difference=" + str(generationLoss - firstGenFitness))
    print("best network of last gen : ")
    print(survivors[0])
    print(time.strftime('%d/%m/%y %H:%M', time.localtime()))
    fitnessFile.close()
    weightsFile.close()
