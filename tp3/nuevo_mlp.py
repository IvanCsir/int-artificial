import math


class Multi_layer_perceptron():

    def __init__(self,e1, e2):
        self.e1 = e1
        self.e2 = e2
        self.LR = 0.1
        self.xor_table = [[0, 0, 0],
                         [0, 1, 1],
                         [1, 0, 1],
                         [1, 1, 0]]
    def neuron_1(self):
        
        w0 = 0.9
        w1 = 0.7
        w2 = 0.5


        self.e1 = self.xor_table[0][0]
        self.e2 = self.xor_table[0][1]

        x = (1*w0 + self.e1*w1 + self.e2*w2)
        SR = 1/(1+(math.e)**(-x))
        # error = self.xor_table[0][2] - SR
        # epsilon = SR*(1-(SR))*error

        # delta_w0 = self.LR*1*epsilon
        # w0 = w0 + delta_w0

        # delta_w1 = self.LR*self.e1*epsilon
        # w1 = w1 + delta_w1

        # delta_w2 = self.LR*self.e2*epsilon
        # w2 = w2 + delta_w2
        
        print("---Neuron 1---\n")
        # print(f"W0: {w0}")
        # print(f"W1: {w1}")
        # print(f"W2: {w2}")
        print(f"SR: {SR}")
        # print(f"Error: {error} \n")
        return SR, w0, w1, w2

    def neuron_2(self):
        w3 = 0.3
        w4 = -0.9
        w5 = -1
        x = (1*w3 + self.e1*w4 + self.e2*w5)
        SR = 1/(1+(math.e)**(-x))
        # error = self.xor_table[0][2] - SR
        # epsilon = SR*(1-(SR))*error

        # delta_w3 = self.LR*1*epsilon
        # w3 = w3 + delta_w3

        # delta_w4 = self.LR*self.e1*epsilon
        # w4 = w4 + delta_w4

        # delta_w5 = self.LR*self.e2*epsilon
        # w5 = w5 + delta_w5
        print("---Neuron 2---\n")
        # print(f"W3: {w3}")
        # print(f"W4: {w4}")
        # print(f"W5: {w5}")
        print(f"SR: {SR}")
        # print(f"Error: {error} \n")
        return SR, w3, w4, w5
    
    def neuron_3(self):
        w6 = 0.8
        w7 = 0.35
        w8 = 0.1
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

        print("---Neuron 3---\n")
        # print(f"W6: {w6}")
        # print(f"W7: {w7}")
        # print(f"W8: {w8}")
        print(f"SR: {SR}")
        # print(f"Error: {error} \n")
        return SR, w6, w7, w8
    
    def neuron_4(self,e3):
        self.e3 = e3
        w9 = -0.23
        w10 = -0.79
        w11 = 0.56
        w12 = 0.6
        x = (1*w9 + self.e1*w10 + self.e2*w11 + self.e3*w12)
        
        SR = 1/(1+(math.e)**(-x))
        error = self.xor_table[0][2] - SR
        epsilon = SR*(1-(SR))*error

        delta_w9 = self.LR*1*epsilon
        w9 = w9 + delta_w9

        delta_w10 = self.LR*self.e1*epsilon
        w10 = w10 + delta_w10

        delta_w11 = self.LR*self.e2*epsilon
        w11 = w11 + delta_w11

        delta_w12 = self.LR*self.e3*epsilon
        w12 = w12 + delta_w12

        print("---Neuron 4---\n")
        print(f"w9: {w9}")
        print(f"w10: {w10}")
        print(f"W11: {w11}")
        print(f"W12: {w12}")
        print(f"SR: {SR}")
        print(f"x = {x}")
        print(f"Error: {error} \n")

        return SR, epsilon