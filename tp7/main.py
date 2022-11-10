import cv2
from tasks import *
import random
import matplotlib.pyplot as plt



def main():
    table = Task_images.read_images()
    number_neurons = int(input("How many neurons do you want in the hidden layer?: "))
    iterations = int(input("How many iterations do you want?: "))
    number_pesos = int((len(table[0])-1)*number_neurons)
    list_pesos_local,lista_pesos_ultima_neurona = Task_images.read_pesos()
    list_neurons = []
    list_outputs = [1]
    new_pesos = []
    lista_SR_final_neuron = []
    lista_errores = [ [] for i in range(len(table))]
    list_error_counter = []

    contador = 0
    while contador != iterations:
        contador += 1
        error_counter = 0
        list_error_counter.append(contador)
        print(f"-------------------------Iteración: {contador}---------------------")
        for i in table:
            a = 0
            for j in range(number_neurons):        
                neuron = Neuron()
                for entry in range((len(table[0]))-1): #Para saber el nro de entradas
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
            lista_errores[error_counter].append(error)
            error_counter += 1
    
            lista_SR_final_neuron.append(SR_final)
            print(f"Salida Real: {SR_final}")
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
    
    # with open('pesos_co.txt', 'w') as f:
    #     for peso in list_pesos_local:
    #         f.write(str(peso) + "\n")

    # with open('pesos_fn.txt', 'w') as f:
    #     for peso in lista_pesos_ultima_neurona:
    #         f.write(str(peso) + "\n")
            
    for i in range(len(lista_errores)):
        plt.plot(list_error_counter, lista_errores[i], label = f"Error r{i}")
    
    plt.title("ERRORES")
    plt.legend()
    plt.savefig( "C:/Users/ivanf/OneDrive/Escritorio/Facultad/4Ano/int-artificial/tp7/" + "grafico_errores_tp7.jpg")
    plt.show()
if __name__ == '__main__':
    main()