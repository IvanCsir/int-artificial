from multilayer import *
import random

def main():
    xor_table = [[1,0,0, 0],
                 [1,0,1, 1],
                 [1,1,0, 1],    
                 [1,1,1, 0]]
                
    number_neurons = int(input("How many neurons do you want in the hidden layer?: "))
    iterations = int(input("How many iterations do you have?: "))
    number_pesos = int(number_neurons*3)
    list_pesos = []
    list_neurons = []
    list_entries = []

    contador = 0
    while contador <= iterations:
        contador += 1
        for i in xor_table:
            peso = random.uniform(-1,1)
            list_pesos.append(peso)
            list_entries.append(j[0])
            list_entries.append(j[1])
            neuron = Neuron()
            list_neurons.append(neuron)




if __name__ == '__main__':
    main() 