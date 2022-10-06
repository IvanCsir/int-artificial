import math


class Multi_layer_perceptron():

    def __init__(self,e1, e2):
        self.e1 = e1
        self.e2 = e2
        self.LR = 0.5

    def neuron_1(self,w0, w1, w2, iteracion):

        x = (1*w0 + self.e1*w1 + self.e2*w2)
        SR = 1/(1+(math.e)**(-x))
        print(f"---Neuron 1 Iteracion:{iteracion}---")
        print(f"SR: {SR}\n")
        
        return SR

    def neuron_2(self, w3, w4, w5, iteracion):
        
        x = (1*w3 + self.e1*w4 + self.e2*w5)
        SR = 1/(1+(math.e)**(-x))
        print(f"---Neuron 2 Iteracion:{iteracion}---")
        print(f"SR: {SR}\n")
        return SR
    
    def neuron_3(self, w6, w7, w8,iteracion):

        x = (1*w6 + self.e1*w7 + self.e2*w8)
        SR = 1/(1+(math.e)**(-x))
        # error = self.xor_table[0][2] - SR
        # epsilon = SR*(1-(SR))*error

        # delta_w6 = self.LR*1*epsilon
        # w6 = w6 + delta_w6

        # delta_w7 = self.LR*self.e1*epsilon
        # w7 = w7 + delta_w7

        # delta_w8 = self.LR*self.e2*epsilon
        # w8 = w8 + delta_w8

        print(f"---Neuron 3 Iteracion:{iteracion}---")
        # print(f"W6: {w6}")
        # print(f"W7: {w7}")
        # print(f"W8: {w8}")
        print(f"SR: {SR}\n")
        # print(f"Error: {error} \n")
        return SR
    
    def neuron_4(self,row,e3,w9,w10,w11,w12, iteracion):
        self.e3 = e3
        x = (1*w9 + self.e1*w10 + self.e2*w11 + self.e3*w12)
        
        SR = 1/(1+(math.e)**(-x))
        error = row[2] - SR
        epsilon = SR*(1-(SR))*error

        delta_w9 = self.LR*1*epsilon
        w9 = w9 + delta_w9

        delta_w10 = self.LR*self.e1*epsilon
        w10 = w10 + delta_w10

        delta_w11 = self.LR*self.e2*epsilon
        w11 = w11 + delta_w11

        delta_w12 = self.LR*self.e3*epsilon
        w12 = w12 + delta_w12

        print(f"---Neuron 4 Iteracion:{iteracion}---")
        print(f"w9: {w9}")
        print(f"w10: {w10}")
        print(f"W11: {w11}")
        print(f"W12: {w12}")
        print(f"SR: {SR}")
        print(f"x = {x}")
        print(f"Error: {error} \n")

        return SR, epsilon, w9, w10, w11,w12, error