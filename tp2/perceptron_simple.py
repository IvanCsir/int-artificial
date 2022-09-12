import math
import matplotlib.pyplot as plt

class Perceptron():
    def and_or(self):
        or_table = [[0,0,0],
                     [0,1,1],
                     [1,0,1],
                     [1,1,1]]

        and_table = [[0,0,0],
                     [0,1,0],
                     [1,0,0],
                     [1,1,1]]

        xor_table = [[0, 0, 0],
                     [0, 1, 1],
                     [1, 0, 1],
                     [1, 1, 0]]

        

        w0 = 0.9
        w1 = 0.66
        w2 = -0.2
        error = 1
        LR = 0.1
        iteracion = 0
        w0_list = []
        w1_list = []
        w2_list = []
        list_counter = []
        list_error_counter = []
        errors_r1 = []
        errors_r2 = []
        errors_r3 = []
        errors_r4 = []
        
        
        opcion = int(input("Which table do you want to use?\nPress 1: or_table \nPress 2: and_table\n Press 3: xor_table\n"))
        if opcion == 1:
            table = or_table

        elif opcion == 2:
            table = and_table

        elif opcion == 3:
            table = xor_table

        


        a = 0
        error_counter = 0

        # while math.fabs(error) > 0.1:
        while iteracion < 1000:
            r = 0
            iteracion += 1
            list_error_counter.append(error_counter)
            for i in table:
                error_counter += 1
                a += 1
                list_counter.append(a)
                r += 1
                e1 = i[0]
                e2 = i[1]
                x = (1*w0 + e1*w1 + e2*w2)
                SR = 1/(1+(math.e)**(-x))
                error = i[2] - SR
                epsilon = SR*(1-(SR))*error
                delta_w0 = LR*1*epsilon
                w0 = w0 + delta_w0

                delta_w1 = LR*e1*epsilon
                w1 = w1 + delta_w1

                delta_w2 = LR*e2*epsilon
                w2 = w2 + delta_w2

                w0_list.append(w0)
                w1_list.append(w1)
                w2_list.append(w2)

                if i == table[0]:
                    errors_r1.append(error)
                elif i == table[1]:
                    errors_r2.append(error)
                elif i == table[2]:
                    errors_r3.append(error)
                elif i == table[3]:
                    errors_r4.append(error)  

                print(f"Iteracion nro: {iteracion} - R{r}")
                print(f"W0: {w0}")
                print(f"W1: {w1}")
                print(f"W2: {w2}")
                print(f"Error: {error} \n")
            


        plt.plot(list_counter, w0_list, label="W0")
        plt.plot(list_counter, w1_list, label="W1")
        plt.plot(list_counter, w2_list, label="W2")
        plt.xlabel("Iteracion")
        plt.ylabel("Peso")
        plt.title("PESOS")
        plt.legend()
        plt.savefig("Grafica_pesos.jpg")
        plt.show()
        
        

        plt.plot(list_error_counter, errors_r1, label = "Error r1")
        plt.plot(list_error_counter, errors_r2, label = "Error r2")
        plt.plot(list_error_counter, errors_r3, label = "Error r3")
        plt.plot(list_error_counter, errors_r4, label = "Error r4")
        plt.xlabel("Iteracion")
        plt.ylabel("Error")

        plt.title("ERRORES")
        plt.legend()
        plt.savefig("Grafica_errores.jpg")
        plt.show()
        


    
       

        
        


