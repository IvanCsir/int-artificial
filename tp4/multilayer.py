import math
class Multi_layer_perceptron():

    def __init__(self,e1, e2, w0, w1, w2):
        self.e1 = e1
        self.e2 = e2
        self.w0 = w0
        self.w1 = w1
        self.w2 = w2
        self.LR = 0.5

    def calculate(self):
        x = (1*self.w0 + self.e1*self.w1 + self.e2*self.w2)
        SR = 1/(1+(math.e)**(-x))
        print(SR)
        return SR
