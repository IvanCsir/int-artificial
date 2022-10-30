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
    list_outputs = []
    inicio = 0
    final = 3
    for i in range(number_pesos):
            peso = random.uniform(-1,1)
            list_pesos.append(peso)
    contador = 0
    while contador <= iterations:
        contador += 1
        for i in xor_table:
            for j in range(number_neurons):
                inicio += 3
                final += 3
                neuron = Neuron()
                neuron.entradas.append(i[0])
                neuron.entradas.append(i[1])
                neuron.entradas.append(i[2])         
                neuron.pesos.append(list_pesos)       
                sr = neuron.calculate()
                list_outputs.append(sr)
    print(list_outputs)
    print(len(list_outputs))




if __name__ == '__main__':
    main() 