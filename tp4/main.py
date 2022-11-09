from multilayer import *
import random
import matplotlib.pyplot as plt

def main():
    xor_table = [[1,0,0, 0],
                 [1,0,1, 1],
                 [1,1,0, 1],    
                 [1,1,1, 0]]
                
    number_neurons = int(input("How many neurons do you want in the hidden layer?: "))
    iterations = int(input("How many iterations do you want?: "))
    number_pesos = int(number_neurons*3)
    list_pesos_local = []
    list_neurons = []
    list_outputs = [1]
    new_pesos = []
    lista_pesos_ultima_neurona = []
    lista_SR_final_neuron = []
    errors_r1 = []
    errors_r2 = []
    errors_r3 = []
    errors_r4 = []
    list_error_counter = []
    
    for i in range(number_neurons+1):
        peso = random.uniform(-1,1)
        lista_pesos_ultima_neurona.append(peso) 

    for i in range(number_pesos):
        peso = random.uniform(-1,1)
        list_pesos_local.append(peso)

    contador = 0
    while contador != iterations:
        contador += 1
        list_error_counter.append(contador)
        for i in xor_table:
            a = 0
            # b = 1
            # c = 2
            for j in range(number_neurons):        
                neuron = Neuron()
                # neuron.entradas.append(i[0])
                # neuron.entradas.append(i[1])
                # neuron.entradas.append(i[2])           
                # neuron.list_pesos.append(list_pesos_local[a])
                # a += 3
                # neuron.list_pesos.append(list_pesos_local[b])
                # b += 3
                # neuron.list_pesos.append(list_pesos_local[c])
                # c += 3
                for entry in range((len(xor_table[0]))-1): #Para saber el nro de entradas
                    neuron.entradas.append(i[entry])           
                    neuron.list_pesos.append(list_pesos_local[a])
                    a += 1
                SR = neuron.calculate()
                neuron.salida = SR
                list_outputs.append(SR)
                list_neurons.append(neuron)

            final_neuron = Neuron()
            for x in range(len(list_outputs)):
                final_neuron.entradas.append(list_outputs[x])
                final_neuron.list_pesos.append(lista_pesos_ultima_neurona[x])
        
            SR_final, epsilon, new_final_pesos, error = final_neuron.calculate_final_neuron(i)

            if i == xor_table[0]:
                errors_r1.append(error)
            elif i == xor_table[1]:
                errors_r2.append(error)
            elif i == xor_table[2]:
                errors_r3.append(error)
            elif i == xor_table[3]:
                errors_r4.append(error) 
            lista_SR_final_neuron.append(SR_final)
            print(f"ITERACION {contador} \n FILA {i} \n Salida Real: {SR_final}")
            list_outputs.clear()
            list_outputs.append(1)

            list_pesos_local.clear()
            for neuron in list_neurons:
                new_peso = neuron.calculate_pesos(epsilon)
                for valor in new_peso:
                    new_pesos.append(valor)

            list_pesos_local = new_pesos
            lista_pesos_ultima_neurona.clear()
            lista_pesos_ultima_neurona = new_final_pesos
            list_neurons.clear()
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