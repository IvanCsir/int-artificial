from nuevo_mlp import *
import matplotlib.pyplot as plt

def main():
    LR = 0.5
    iteracion = 0
    xor_table = [[0, 0, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]]
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
    w0_list = []
    w1_list = []
    w2_list = []
    w3_list = []
    w4_list = []
    w5_list = []
    w6_list = []
    w7_list = []
    w8_list = []
    w9_list = []
    w10_list = []
    w11_list = []
    w12_list = []
    list_counter = []
    list_error_counter = []
    errors_r1 = []
    errors_r2 = []
    errors_r3 = []
    errors_r4 = []    
    

    a = 0
    
    while iteracion < 10000:
        iteracion += 1
        print(f"---------------Iteracion nro {iteracion}------------------")
        list_error_counter.append(iteracion)
        r = 0
        for i in xor_table:
            a += 1
            r += 1
            list_counter.append(a)
            
            
            SR1 = Multi_layer_perceptron(i[0],i[1]).neuron_1(w0,w1,w2, r)
            SR2 = Multi_layer_perceptron(i[0],i[1]).neuron_2(w3,w4,w5,r)
            SR3 = Multi_layer_perceptron(i[0],i[1]).neuron_3(w6,w7,w8,r)
            SR4, df, w9, w10, w11,w12, error= Multi_layer_perceptron(SR1,SR2).neuron_4(i,SR3,w9,w10,w11,w12, r)

            # print("----Hidden Neuron 1 - Back forward----")
            s_0c1 = SR1 * (1 - (SR1)) * df
            delta_w0_0c1 = LR * 1 * s_0c1
            # print(f"s_0c1:{s_0c1}")
            # print(f"delta_0c1:{delta_w0_0c1}")
            # print(f"w0: {w0}") 
            w0 = delta_w0_0c1 + w0
            
            w0 = w0
            w0_list.append(w0)

            delta_w1_0c1 = LR * i[0] * s_0c1
            # print(f"delta_w1_0c1:{delta_w1_0c1}")
            # print(f"w1: {w1}")
            w1 = delta_w1_0c1 + w1
            w1 = w1
            w1_list.append(w1)

            delta_w2_0c1 = LR * i[1] * s_0c1
            # print(f"delta_w2_0c1:{delta_w2_0c1}")
            # print(f"w2: {w2}\n")
            w2 = delta_w2_0c1 + w2
            w2 = w2
            w2_list.append(w2)

            # print("----Hidden Neuron 2 - Back forward----")
            s_0c2 = SR2 * (1 - (SR2)) * df
            delta_w3_0c2 = LR * 1 * s_0c2
            # print(f"s_0c2:{s_0c2}")
            # print(f"delta_0c2:{delta_w3_0c2}")
            # print(f"w3: {w3}")
            w3 = delta_w3_0c2 + w3
            w3 = w3
            w3_list.append(w3)

            delta_w4_0c2 = LR * i[0] * s_0c2
            # print(f"delta_w4_0c2:{delta_w4_0c2}")
            # print(f"w4: {w4}")
            w4 = delta_w4_0c2 + w4
            w4 = w4
            w4_list.append(w4)

            delta_w5_0c2 = LR * i[1] * s_0c2
            # print(f"delta_w5_0c2:{delta_w5_0c2}")
            # print(f"w5: {w5}\n")
            w5 = delta_w5_0c2 + w5
            w5 = w5
            w5_list.append(w5)

            # print("----Hidden Neuron 3 - Back forward----")
            s_0c3 = SR3 * (1 - (SR3)) * df
            delta_w6_0c3 = LR * 1 * s_0c3
            # print(f"s_0c3:{s_0c3}")
            # print(f"delta_0c3:{delta_w6_0c3}")
            # print(f"w6: {w6}")
            w6 = delta_w6_0c3 + w6
            w6 = w6
            w6_list.append(w6)

            delta_w7_0c3 = LR * i[0] * s_0c3
            w7 = delta_w7_0c3 + w7
            # print(f"delta_w7_0c3:{delta_w7_0c3}")
            # print(f"w7: {w7}")
            w7 = w7
            w7_list.append(w7)

            delta_w8_0c3 = LR * i[1] * s_0c3
            w8 = delta_w8_0c3 + w8
            # print(f"delta_w8_0c3:{delta_w8_0c3}")
            # print(f"w8: {w8}")
            w8 = w8
            w9 = w9
            w10 = w10
            w11 = w11
            w12 = w12
            w8_list.append(w8)
            w9_list.append(w9)
            w10_list.append(w10)
            w11_list.append(w11)
            w12_list.append(w12)

            if i == xor_table[0]:
                errors_r1.append(error)
            elif i == xor_table[1]:
                errors_r2.append(error)
            elif i == xor_table[2]:
                errors_r3.append(error)
            elif i == xor_table[3]:
                errors_r4.append(error) 
        
    plt.plot(list_counter, w0_list, label="W0")
    plt.plot(list_counter, w1_list, label="W1")
    plt.plot(list_counter, w2_list, label="W2")
    plt.plot(list_counter, w3_list, label="W3")
    plt.plot(list_counter, w4_list, label="W4")
    plt.plot(list_counter, w5_list, label="W5")
    plt.plot(list_counter, w6_list, label="W6")
    plt.plot(list_counter, w7_list, label="W7")
    plt.plot(list_counter, w8_list, label="W8")
    plt.plot(list_counter, w9_list, label="W9")
    plt.plot(list_counter, w10_list, label="W10")
    plt.plot(list_counter, w11_list, label="W11")
    plt.plot(list_counter, w12_list, label="W12")
    plt.xlabel("Iteracion")
    plt.ylabel("Peso")
    plt.title("PESOS")
    plt.legend()
    plt.show()

    plt.plot(list_error_counter, errors_r1, label = "Error r1")
    plt.plot(list_error_counter, errors_r2, label = "Error r2")
    plt.plot(list_error_counter, errors_r3, label = "Error r3")
    plt.plot(list_error_counter, errors_r4, label = "Error r4")
    plt.xlabel("Iteracion")
    plt.ylabel("Error")

    plt.title("ERRORES")
    plt.legend()
    plt.show()




if __name__ == '__main__':
    main() 