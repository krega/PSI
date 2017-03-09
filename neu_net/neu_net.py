from perceptron import neuron
import math


class neu_net:
    def __init__(self, layers, samples, values, coeff, epo):
        self.samples = samples
        self.values = values
        self.layers_nr = layers
        self.n = coeff # wspolczynnik uczenia
        self.epoch = epo
        self.layers = list()
        self.error = 0
        self.out_teached = list()
        self.error_teached = list()
        self.epoch_n = list()
        self.err_ep = list()
        for i in range(layers):
            self.layers.append(list())

    def initialize_layer(self, which, number_per, inputs_per_perceptron, outputs_per_perceptron):
        self.layers[which] = list()
        for i in range(number_per):
            self.layers[which].append(neuron.neuron(inputs_per_perceptron, outputs_per_perceptron))

    def print_info(self, layer):
        for i in range(len(self.layers[layer])):
            print 'perceptron[{}]'.format(i)
            self.layers[layer][i].print_info()

    def initialize_perceptron(self, layer, percep, wages, bias):
        self.layers[layer][percep].initialize_wages(wages, bias)

    def calculate_perceptron_output(self, per, inp):
        signal_out = 0.0
        if len(per.wages) != len(inp):
            return -1
        #obliczenie sumy (wejscia*wagi)
        for i in range(per.inputs_nr):
            signal_out += per.wages[i] * inp[i]

        signal_out += per.bias
        per.signal_out = signal_out
        #przejscie sumy przez funkcje aktywacji
        per.out_value = 1.0 / (1.0 + math.exp(-per.signal_out))
        return per.out_value

    def teach_network(self):
        teached = 0
        epoch = 0
        while teached == 0:
            # uczenie sieci
            index_count = 0
            for element in self.samples:
                #obliczenie wyjscia pierwszej warstwy (neuronu N1)
                self.calculate_perceptron_output(self.layers[0][0], [element])
                #obliczenie wyjscia drugiej warstwy
                #obliczenie wyjscia neuronu N2
                self.calculate_perceptron_output(self.layers[1][0], [self.layers[0][0].out_value])
                #obliczenie wyjscia neuronu N3
                self.calculate_perceptron_output(self.layers[1][1], [self.layers[0][0].out_value])
                #obliczenie wyjscia neuronu N4
                self.calculate_perceptron_output(self.layers[1][2], [self.layers[0][0].out_value])
                #obliczenie wyjscia warstwy trzeciej
                #obliczenie wyjscia neuronu N5
                self.calculate_perceptron_output(self.layers[2][0], [self.layers[1][0].out_value,
                                                                     self.layers[1][1].out_value,
                                                                     self.layers[1][2].out_value])
                #obliczenie bledu
                e = self.values[index_count] - self.layers[2][0].signal_out
                #wsteczna propagacja bledu
                #blad neuronu N5
                self.layers[2][0].error = e
                #propagacja bledu do warstwy drugiej
                #blad neuronu N2
                self.layers[1][0].error = ((self.layers[1][0].out_value * (1.0 - self.layers[1][0].out_value)) *
                                           self.layers[2][0].wages[0] * self.layers[2][0].error)
                #blad neuronu N3
                self.layers[1][1].error = ((self.layers[1][1].out_value * (1.0 - self.layers[1][1].out_value)) *
                                           self.layers[2][0].wages[1] * self.layers[2][0].error)
                #blad neuronu N4
                self.layers[1][2].error = ((self.layers[1][2].out_value * (1.0 - self.layers[1][2].out_value)) *
                                           self.layers[2][0].wages[2] * self.layers[2][0].error)
                #propagacja bledu do warstwy pierwszej
                # blad neuronu N1
                self.layers[0][0].error = ((self.layers[0][0].out_value * (1.0 - self.layers[0][0].out_value)) *
                                           ((self.layers[1][0].wages[0] * self.layers[1][0].error) +
                                            (self.layers[1][1].wages[0] * self.layers[1][1].error) +
                                            (self.layers[1][2].wages[0] * self.layers[1][2].error)))

                #obliczenie biasu neuronu N5 do kolejnego cyklu
                self.layers[2][0].bias += self.layers[2][0].error * self.n
                #obliczenie wagi1 neuronu N5 do kolejnego cyklu
                self.layers[2][0].wages[0] = (self.layers[2][0].wages[0] +
                                              (self.n * self.layers[2][0].error * self.layers[1][0].out_value))
                #obliczenie wagi2 neuronu N5 do kolejnego cyklu
                self.layers[2][0].wages[1] = (self.layers[2][0].wages[1] +
                                              (self.n * self.layers[2][0].error * self.layers[1][1].out_value))
                #obliczenie wagi3 neuronu N5 do kolejnego cyklu
                self.layers[2][0].wages[2] = (self.layers[2][0].wages[2] +
                                              (self.n * self.layers[2][0].error * self.layers[1][2].out_value))
                #obliczenie biasu neuronu N2 do kolejnego cyklu
                self.layers[1][0].bias += self.layers[1][0].error * self.n
                #obliczenie biasu neuronu N3 do kolejnego cyklu
                self.layers[1][1].bias += self.layers[1][1].error * self.n
                #obliczenie biasu neuronu N4 do kolejnego cyklu
                self.layers[1][2].bias += self.layers[1][2].error * self.n
                #obliczenie wagi neuronu N2 do kolejnego cyklu
                self.layers[1][0].wages[0] = (self.layers[1][0].wages[0] +
                                              (self.n * self.layers[1][0].error * self.layers[0][0].out_value))
                #obliczenie wagi neuronu N3 do kolejnego cyklu
                self.layers[1][1].wages[0] = (self.layers[1][1].wages[0] +
                                              (self.n * self.layers[1][1].error * self.layers[0][0].out_value))
                #obliczenie wagi neuronu N4 do kolejnego cyklu
                self.layers[1][2].wages[0] = (self.layers[1][2].wages[0] +
                                              (self.n * self.layers[1][2].error * self.layers[0][0].out_value))
                #obliczenie wagi neuronu N1 do kolejnego cyklu
                self.layers[0][0].wages[0] = (self.layers[0][0].wages[0] +
                                              (self.n * self.layers[0][0].error * element))
                #obliczenie biasu neuronu N1 do kolejnego cyklu
                self.layers[0][0].bias += self.layers[0][0].error * self.n
                index_count += 1
            #po zadanej ilosci epok uznajemy, ze siec jest nauczona
            if (epoch == self.epoch):
                print "teaching was finished"
                teached = 1
            #zapisanie bledu i epoki (wykres blad vs epoka)
            self.err_ep.append(float(self.layers[2][0].error))
            self.epoch_n.append(float(epoch))
            epoch += 1

    def start_net(self, input_vec):
        print 'Startujemy siec'
        for x in input_vec:
            #obliczenie sumy neuronu N1
            self.layers[0][0].signal_out = x * self.layers[0][0].wages[0] + self.layers[0][0].bias
            #suma neuronu N1 podana na funkcje aktywacji (obliczenie wyjscia neuronu)
            self.layers[0][0].out_value = 1.0 / (1.0 + math.exp(-self.layers[0][0].signal_out))
            # obliczenie sumy neuronu N2
            self.layers[1][0].signal_out = (self.layers[0][0].out_value *
                                            self.layers[1][0].wages[0] + self.layers[1][0].bias)
            #suma neuronu N2 podana na funkcje aktywacji (obliczenie wyjscia neuronu)
            self.layers[1][0].out_value = 1.0 / (1.0 + math.exp(-self.layers[1][0].signal_out))
            #obliczenie sumy neuronu N3
            self.layers[1][1].signal_out = (self.layers[0][0].out_value *
                                            self.layers[1][1].wages[0] + self.layers[1][1].bias)
            #suma neuronu N3 podana na funkcje aktywacji (obliczenie wyjscia neuronu)
            self.layers[1][1].out_value = 1.0 / (1.0 + math.exp(-self.layers[1][1].signal_out))
            #obliczenie sumy neuronu N4
            self.layers[1][2].signal_out = (self.layers[0][0].out_value *
                                            self.layers[1][2].wages[0] + self.layers[1][2].bias)
            #suma neuronu N4 podana na funkcje aktywacji (obliczenie wyjscia neuronu)
            self.layers[1][2].out_value = 1.0 / (1.0 + math.exp(-self.layers[1][2].signal_out))
            #obliczenie sumy neuronu N5
            self.layers[2][0].signal_out = (self.layers[1][0].out_value * self.layers[2][0].wages[0] +
                                            self.layers[1][1].out_value * self.layers[2][0].wages[1] +
                                            self.layers[1][2].out_value * self.layers[2][0].wages[2] +
                                            self.layers[2][0].bias)
            #neuron N5 posiada liniowa funkcje aktywacji wyjscie z sumatora jest wyjsciem sieci
            #zapisanie wyjscia z sieci do wektora (potrzebne do wygenerowania wykresu)
            self.out_teached.append(self.layers[2][0].signal_out)
            self.error_teached.append(self.layers[2][0].signal_out - math.cos(x))
