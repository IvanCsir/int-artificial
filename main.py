from multilayer import *

def main():
    w0 = 0.9
    w1 = 0.7
    w2 = 0.5
    w3 = 0.3
    w4 = -0.9
    w5 = -1
    w6 = 0.8
    w7 = 0.35
    w8 = 0.1
    w9 = -0.23
    w10 = -0.79
    w11 = 0.56
    w12 = 0.6
    number_neurons = input("How many neurons do you want in the hidden layer?: ")
    number_pesos = int(number_neurons*3)
    list_pesos = []
    for i in number_pesos:
        peso = input(f"Ingrese el valor del peso w_")
        list_pesos.append(peso)
    w_0 = 0
    w_1 = 0
    w_2 = 0

    for i in range():
    neuron1 = Multi_layer_perceptron(1,1,0.99,0.33,1)
    neuron1.caculate()


if __name__ == '__main__':
    main() 