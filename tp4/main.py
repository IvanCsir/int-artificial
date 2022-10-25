from multilayer import *
import random

def main():
    xor_table = [[0, 0, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]]
                
    number_neurons = int(input("How many neurons do you want in the hidden layer?: "))
    number_pesos = int(number_neurons*3)
    list_pesos = []
        
    for i in number_pesos:
        
        peso = random.uniform(-1,1)
        list_pesos.append(peso)

    
        hidden_list = []
        list_dividida = [list_pesos[i:i + 3] for i in range(0, len(list_pesos), 3)]
        for xor in xor_table:
            for i in range(number_neurons):
                for j in list_dividida:
                    for k in j:
                        neuron = Multi_layer_perceptron(xor[0], xor[1],k[0],k[1], k[2])
                        neuron.calculate()


if __name__ == '__main__':
    main() 