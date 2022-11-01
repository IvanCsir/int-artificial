import math
class Neuron():

    def __init__(self):
        self.entradas = []
        self.list_pesos = []
        self.salida = 0
        self.LR = 0.1

    def calculate(self):
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.list_pesos[i])
        SR = 1/(1+(math.e)**(-x))
        return SR
    
    def final_neuron(self,row):
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.list_pesos[i])
        SR = 1/(1+(math.e)**(-x))
        error = row[3] - SR
        epsilon = SR*(1-(SR))*error

        for i in range(len(self.entradas)):
            gen_delta = self.LR*self.entradas[i]
            self.list_pesos[i] = self.list_pesos[i] + gen_delta

        return SR, epsilon
    
    def calculate_pesos(self, df):
        for i in range(self.list_pesos):
                gen_soc = self.salida * (1 - (self.salida)) * df
                delta_gen_soc = self.LR * self.entradas[i] * gen_soc
                self.list_pesos[i] = delta_gen_soc + self.list_pesos[i]
        

                



    
