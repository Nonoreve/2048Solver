'''
Created on 5 juin 2018

@author: nonoreve

test of the working of the neural network (completly abstract from the game)
'''
import random

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


if __name__ == '__main__':
    # the current living network population
    population = []
    # create the original ancestors
    POPULATION_SIZE = 8
    nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers = 2, 2, 2, 1
    for i in range(0, POPULATION_SIZE):
        population.append(NeuralNetwork(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, [ [[random.random(), random.random(), random.random()], [random.random(), random.random(), random.random()]], [[random.random(), random.random(), random.random()], [random.random(), random.random(), random.random()]] ]))
        print("ORIGINAL ANCESTORS\n" + str(population[i]) + '\n')
    
    expectedResults = [0.1, 0.9]
    inputs = [0.5, 0.5]
    
    for _ in range(0, 1000):
        # compute and sort the results
        results = []
        for i in range(0, POPULATION_SIZE):
            outputs = population[i].update(inputs)
            err = error(outputs, expectedResults)
            results.append((i, err))
            print("outputs and error " + str([round(x, 3) for x in outputs]) + " = " + str(round(err, 3)))
        # print(results)
        results.sort(key=getKey, reverse=False)
        # print(results)
        
        # kill the bad ones (the bottom half)
        results = results[:POPULATION_SIZE // 2]
        print("selected ones " + str(results))
        survivors = []
        generationLoss = 0
        for i, x in results:
            survivors.append(population[i])
            generationLoss += x
        generationLoss /= len(results)
        print("generation loss = " + str(generationLoss))
        # print(population)
        # print(survivors)
        
        # compute the average weights of each survivor
        averageWeights = flatTab(survivors[0].get_weights())
        for nn in survivors[1:]:
            nnWeights = nn.get_weights()
            averageWeights = [x + y for x, y in zip(averageWeights, flatTab(nnWeights))]
        for i, val in enumerate(averageWeights):
            averageWeights[i] = val / len(survivors)
        # averageWeights = sliceTab(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, averageWeights)
        print("average " + str(averageWeights))
        
        # now reproduce the survivors
        nextgen = survivors
        for i in range(0, POPULATION_SIZE - len(survivors)):
            newWeights = []
            for weight in averageWeights:
                newWeights.append(weight + ((random.random() - 0.5) * generationLoss))
            nextgen.append(NeuralNetwork(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, sliceTab(nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, newWeights)))
            print(nextgen[-1])
        population = nextgen
