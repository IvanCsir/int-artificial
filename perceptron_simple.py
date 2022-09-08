import math

class Perceptron():
    def and_or(self):
        and_table = [[0,0,0],
                     [0,1,0],
                     [1,0,0],
                     [1,1,1]]

        or_table = [[0,0,0],
                     [0,1,1],
                     [1,0,1],
                     [1,1,1]]

        w0 = 0.9
        w1 = 0.66
        w2 = -0.2
        error = 1
        LR = 0.1
        iteracion = 0

        while math.fabs(error) > 0.1 :
            print(f"Iteracion nro: {iteracion}")
            iteracion += 1
            for i in and_table:
                input()
                e1 = i[0]
                e2 = i[1]
                x = (1*w0 + e1*w1 + e2*w2)
                print(x)
                SR = 1/(1+(math.e)**-x)
                print(SR)
                error = i[2] - SR
                epsilon = SR*(1-SR)*error
                delta_w0 = LR*1*epsilon
                w0 = w0 + delta_w0

                delta_w1 = LR*e1*epsilon
                w1 = w1 + delta_w1

                delta_w2 = LR*e2*epsilon
                w2 = w2 + delta_w2
                print(f"w0: {w0}")
                print(f"w1: {w1}")
                print(f"w2: {w2}")
                print(f"error: {error}")


