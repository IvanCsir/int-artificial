import math
class Neuron():

    def __init__(self):
        self.entradas = []
        self.list_pesos = list
        self.LR = 0.1

    def calculate(self):
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.list_pesos[i])
        SR = 1/(1+(math.e)**(-x))
        print(SR)
        return SR
    
    def final_neuron(self,row):
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.list_pesos[i])
        SR = 1/(1+(math.e)**(-x))
        error = row[3] - SR
        epsilon = SR*(1-(SR))*error

        for i in range(self.entradas+1):
            gen_delta = self.LR*self.entradas[i]
            gen_w = gen_w + gen_delta

        return SR, epsilon
    
    def calculate_pesos(self, list_outputs, list_pesos, df):
        contador = 0
        for i in range(list_pesos):
            contador += 1
            if contador < 3:
                gen_soc = list_outputs[0] * (1 - (list_outputs[0])) * df
                delta_gen_soc = self.LR * list_outputs[0] * gen_soc
                gen_peso = delta_gen_soc + list_pesos[0]
            

    
