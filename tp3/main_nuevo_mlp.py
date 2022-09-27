from nuevo_mlp import *

def main():
    LR = 0.1
    iteracion = 0
    xor_table = [[0, 0, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]]

        
    while iteracion < 1000:
        iteracion += 1
        print(f"Iteracion nro-------------------------------------------: {iteracion}")
        for i in xor_table:
            SR1, w0, w1, w2 = Multi_layer_perceptron(i[0],i[1]).neuron_1()
            SR2,w3, w4, w5 = Multi_layer_perceptron(i[0],i[1]).neuron_2()
            SR3, w6, w7, w8 = Multi_layer_perceptron(i[0],i[1]).neuron_3()
            SR4, df = Multi_layer_perceptron(SR1,SR2).neuron_4(SR3)

            print("----Hidden Neuron 1 - Back forward----")
            s_0c1 = SR1 * (1 - (SR1)) * df
            delta_w0_0c1 = LR * 1 * s_0c1
            print(f"s_0c1:{s_0c1}")
            print(f"delta_0c1:{delta_w0_0c1}")

            w0 = delta_w0_0c1 + w0
            print(f"w0: {w0}")

            delta_w1_0c1 = LR * 0 * s_0c1
            print(f"delta_w1_0c1:{delta_w1_0c1}")
            w1 = delta_w1_0c1 + w1
            print(f"w1: {w1}")

            delta_w2_0c1 = LR * 0 * s_0c1
            print(f"delta_w2_0c1:{delta_w2_0c1}")
            w2 = delta_w2_0c1 + w2
            print(f"w2: {w2}")

            print("----Hidden Neuron 2 - Back forward----")
            s_0c2 = SR2 * (1 - (SR2)) * df
            delta_w3_0c2 = LR * 1 * s_0c2
            print(f"s_0c2:{s_0c2}")
            print(f"delta_0c2:{delta_w3_0c2}")

            w3 = delta_w3_0c2 + w3
            print(f"w3: {w3}")

            delta_w4_0c2 = LR * 0 * s_0c2
            print(f"delta_w4_0c2:{delta_w4_0c2}")
            w4 = delta_w4_0c2 + w4
            print(f"w4: {w4}")

            delta_w5_0c2 = LR * 0 * s_0c2
            print(f"delta_w5_0c2:{delta_w5_0c2}")
            w5 = delta_w5_0c2 + w5
            print(f"w5: {w5}")

            print("----Hidden Neuron 3 - Back forward----")
            s_0c3 = SR3 * (1 - (SR3)) * df
            delta_w6_0c3 = LR * 1 * s_0c3
            print(f"s_0c3:{s_0c3}")
            print(f"delta_0c3:{delta_w6_0c3}")

            w6 = delta_w6_0c3 + w6
            print(f"w6: {w6}")

            delta_w7_0c3 = LR * 0 * s_0c3
            print(f"delta_w7_0c3:{delta_w7_0c3}")
            w7 = delta_w7_0c3 + w7
            print(f"w7: {w7}")

            delta_w8_0c3 = LR * 0 * s_0c3
            print(f"delta_w8_0c3:{delta_w8_0c3}")
            w8 = delta_w8_0c3 + w8
            print(f"w8: {w8}")






if __name__ == '__main__':
    main() 