import math
import cv2

class Neuron():

    def __init__(self):
        self.entradas = []
        self.list_pesos = []
        self.salida = 0
        self.LR = 0.5

    def calculate(self):
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.list_pesos[i])
        SR = 1/(1+(math.e)**(-x))
        return SR
    
    def calculate_final_neuron(self,row):
        lista_pesos_fn = []
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.list_pesos[i])
        SR = 1/(1+(math.e)**(-x))
        error = row[3] - SR
        epsilon = SR*(1-(SR))*error

        for i in range(len(self.entradas)):
            gen_delta = self.LR*self.entradas[i]*epsilon
            w_gen = self.list_pesos[i] + gen_delta
            lista_pesos_fn.append(w_gen)

        return SR, epsilon, lista_pesos_fn, error
    
    def calculate_pesos(self, df):
        lista_pesos_nuevos = []
        for i in range(len(self.list_pesos)):
                gen_soc = self.salida * (1 - (self.salida)) * df
                delta_gen_soc = self.LR * self.entradas[i] * gen_soc
                peso = delta_gen_soc + self.list_pesos[i]
                lista_pesos_nuevos.append(peso)
        return lista_pesos_nuevos

        
        

                



    
