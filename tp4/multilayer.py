import math
class Neuron():

    def __init__(self):
        self.pesos = []
        self.entradas = []
        self.salida = float

    def calculate(self):
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.pesos[i])
        SR = 1/(1+(math.e)**(-x))
        print(SR)
        return SR
    
