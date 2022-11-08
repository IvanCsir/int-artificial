import cv2
from tasks import *
import random
from tasks_image import *



def main():
    table = read_images()
    aaa = len(table[0])
    number_neurons = int(input("How many neurons do you want in the hidden layer?: "))
    iterations = int(input("How many iterations do you have?: "))
    number_pesos = int((len(table[0])-1)*number_neurons)
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
        peso = random.uniform(-0.1,0.11)
        lista_pesos_ultima_neurona.append(peso) 

    for i in range(number_pesos):
        peso = random.uniform(-0.1,0.1)
        list_pesos_local.append(peso)

    contador = 0
    while contador != iterations:
        contador += 1
        list_error_counter.append(contador)
        for i in table:
            a = 0
            b = 1
            c = 2
            for j in range(number_neurons):        
                neuron = Neuron()
                for entry in range((len(table[0]))-1): #Para saber el nro de entradas
                    neuron.entradas.append(i[entry])           
                    neuron.list_pesos.append(list_pesos_local[entry])

                SR = neuron.calculate()
                neuron.salida = SR
                list_outputs.append(SR)
                list_neurons.append(neuron)

            final_neuron = Neuron()
            for x in range(len(list_outputs)):
                final_neuron.entradas.append(list_outputs[x])
                final_neuron.list_pesos.append(lista_pesos_ultima_neurona[x])
        
            SR_final, epsilon, new_final_pesos, error = final_neuron.calculate_final_neuron(i)

            lista_SR_final_neuron.append(SR_final)
            # print(f"ITERACION {contador} \n FILA {i} \n Salida Real: {SR_final}")
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
    print(lista_SR_final_neuron[-1])
    print(lista_SR_final_neuron[-2])

if __name__ == '__main__':
    main()