import numpy as np
from sklearn.utils import shuffle
import random

class Matriz():

    def crear_matriz(self,n,m):
        a = 0
        objective_matrix = []

        """ #Matrix without numpy """
        # for fil in range(n):
        #     objective_matrix.append([])
        #     for col in range(m):
        #         a+=1
        #         objective_matrix[fil].append(a)
        
        # objective_matrix[fil-1][col-1]=0

        """ #Matrix with numpy """
        objective_matrix = np.zeros((n,m),int)
        for fil in range(n):
            for col in range(m):
                a += 1
                objective_matrix[fil][col] = a
        
        objective_matrix[fil][col] = 0
                
        print(f"Objective matrix: \n{objective_matrix}")
        return objective_matrix

       


    def mix_matrix(self,n,m,amount_mix):
        amount_elements = n*m
        list_elements = []
        a = 0
        for i in range(amount_elements):
            list_elements.append(a)
            a += 1
        for i in range(amount_mix):
            random.shuffle(list_elements)

        """ #Matrix with numpy """
        matriz = np.zeros((n,m),int)
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
        print(f"Mixed matrix: \n{matriz}")         
        return matriz