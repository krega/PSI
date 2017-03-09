import numpy as np

class neuron:
    def __init__(self, inputs_nr, outputs_nr):
        self.inputs_nr = inputs_nr
        self.wages = list()
        for i in range(inputs_nr):
            self.wages.append(0)
        self.out = list()
        self.signal = list()
        for i in range(outputs_nr):
            self.out.append(0)
            self.signal.append(0)
        self.bias = 0
        self.sum = 0
        self.signal_out = 0
        self.out_value = 0
        self.error = 0

    def initialize_wages(self, wages, bias):
        if self.inputs_nr != len(wages):
            print "Input list has wrong size"
            return -1
        else:
            for i in range(len(wages)):
                self.wages[i] = wages[i]
        self.bias = bias

    def print_info(self):
        print '{}: {}'.format("Number of inputs", self.inputs_nr)
        print '{}: {}, bias: {}'.format("Wagi perceptronu", self.wages, self.bias)

    def calculate_output(self, input_array):
        mul = self.wages * input_array
        self.sum = np.sum(mul)
        self.sum += self.bias
        print '{}: {}, {}: {}, {}: {}'.format("Mul ", mul, "w0", self.bias, "sum", self.sum)
        return self.sum
