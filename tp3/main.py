from mlp import *

def main():
    SR1 = Multi_layer_perceptron(0,0).neuron_1()
    SR2 = Multi_layer_perceptron(0,0).neuron_2()
    SR3 = Multi_layer_perceptron(SR1,SR2).neuron_3()
    SR4 = Multi_layer_perceptron(SR1,SR2).neuron_4()
    SR5 = Multi_layer_perceptron(SR1,SR2).neuron_5()
    SR6 = Multi_layer_perceptron(SR3,SR4).neuron_6(SR5)





if __name__ == '__main__':
    main() 