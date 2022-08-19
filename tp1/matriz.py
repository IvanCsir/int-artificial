import numpy as np
from sklearn.utils import shuffle
import random

class Matriz:

    matriz2 = 0
    def crear_matriz(n,m,amount_mix):
        amount_elements = n*m
        list_elements = []

        for i in range(amount_elements):
            list_elements.append(i)
        print(list_elements)

        for i in range(amount_mix):
            random.shuffle(list_elements)
        print(list_elements)

        """ #Matrix with numpy """
        matriz = np.zeros((n,m))
        a = 0
        for fil in range(n):
            for col in range(m):
                matriz[fil][col] = list_elements[a]
                a += 1
        
        """ Matriz without numpy """
        # matriz = []
        # a=0
        # for fil in range(n):
        #     matriz.append([])
        #     for col in range(m):
        #         matriz[fil].append(list_elements[a])
        #         a+=1
        print(matriz)
    
        return matriz
        
        


        
        # global matriz2
        # matriz2 = matriz
        # return matriz
        

    def mezclar_matriz():
        # global matriz2
        # sample = int(input("How many time do you like to shuffle the matrix?: "))
        # for i in range(sample):
        #     random.shuffle(matriz)
        # print(matriz)
        # print(matriz2)
        pass

