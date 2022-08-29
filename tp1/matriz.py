import numpy as np
import random
from random_search import *

class Matriz():

    def crear_matriz(self,n,m):
        a = 0
        objective_matrix = []

        """ #Matrix without numpy """
        for fil in range(n):
            objective_matrix.append([])
            for col in range(m):
                a+=1
                objective_matrix[fil].append(a)
        
        objective_matrix[-1][-1]=0
                
        return objective_matrix

    def mix_matrix(self, amount_mix, matrix):

        for i in range(amount_mix):
            matriz = Random_search().possible_movements(matrix)     

        return matriz