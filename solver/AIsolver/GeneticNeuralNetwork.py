import math

BIAS = -1

"""
To view the structure of the Neural Network, type
print network_name
"""


class Neuron:

    def __init__(self, nbInputs, weights):
        """ last case of weights is the bias (so weights's length is nb_inputs + 1) """
        self.n_inputs = nbInputs
        # a tab of weights
        self.weights = weights

    def sum(self, outputs):
        # Does not include the bias
        return sum(val * self.weights[i] for i, val in enumerate(outputs))

    def set_weights(self, weights):
        self.weights = weights

    def __str__(self):
        return 'Weights: %s, Bias: %s' % (str([round(x, 3) for x in self.weights[:-1]]), str(round(self.weights[-1], 3)))


class NeuronLayer:

    def __init__(self, n_neurons, nbInputs, allWeights):
        self.n_neurons = n_neurons
        self.neurons = [Neuron(nbInputs, allWeights[x]) for x in range(0, self.n_neurons)]

    def __str__(self):
        return 'Layer:\n\t' + '\n\t'.join([str(neuron) for neuron in self.neurons]) + ''


class NeuralNetwork:

    def __init__(self, nbInputs, nbOutputs, nbNeuronPerHL, nbHiddenLayers, network_weights):
        self.n_inputs = nbInputs
        self.n_outputs = nbOutputs
        self.n_hidden_layers = nbHiddenLayers
        self.n_neurons_to_hl = nbNeuronPerHL
        # tab of tab of tab
        self.network_weights = network_weights
        self._create_network()
        # end

    def _create_network(self):
        if self.n_hidden_layers > 0:
            # create the first HIDDEN layer
            self.layers = [NeuronLayer(self.n_neurons_to_hl, self.n_inputs, [[ 1 for _ in range(0, self.n_inputs)] for _ in range(0, self.n_neurons_to_hl)])]

            # create hidden layers
            self.layers += [NeuronLayer(self.n_neurons_to_hl, self.n_neurons_to_hl, self.network_weights[i]) for i in range(0, self.n_hidden_layers)]

            # hidden-to-output layer
            self.layers += [NeuronLayer(self.n_outputs, self.n_neurons_to_hl, self.network_weights[self.n_hidden_layers])]
        else:
            # If we don't require hidden layers
            self.layers = [NeuronLayer(self.n_outputs, self.n_inputs, self.network_weights)]

    def get_weights(self):
        """ table of tables of tables of weights   """
        weights = []

        for layer in self.layers:
            layerWeights = []
            for neuron in layer.neurons:
                layerWeights.append(neuron.weights)
            weights.append(layerWeights)
        return weights

    def nb_weights(self, weights):
        """ how many weights in this tab of tab of tab"""
        n_weights = 0
        for layerW in weights:
            for neuronW in layerW:
                n_weights += neuronW.length # +1 for bias weight -- no need anymore --
        return n_weights

    def set_weights(self, weights):
        assert self.nb_weights(weights) == self.nb_weights(self.get_weights()), "Incorrect amount of weights."

        iLayer = 0
        for layer in self.layers:
            iNeuron = 0
            for neuron in layer.neurons:
                neuron.set_weights(weights[iLayer][iNeuron])
                iNeuron += 1
            iLayer += 1
        return self

    def update(self, inputs):
        assert len(inputs) == self.n_inputs, "Incorrect amount of inputs."

        for layer in self.layers:
            outputs = []
            for neuron in layer.neurons:
                tot = neuron.sum(inputs) + neuron.weights[-1] * BIAS
                outputs.append(self.sigmoid(tot))
            inputs = outputs
        return outputs

    def sigmoid(self, activation, response=1):
        # the activation function
        try:
            return 1 / (1 + math.e ** (-activation / response))
        except OverflowError:
            return float("inf")

    def __str__(self):
        return '\n'.join([str(i + 1) + ' ' + str(layer) for i, layer in enumerate(self.layers)])
