import random
from shutil import move
from turtle import pos
from matriz import *
import time

class Random_search():
    
    def find_zero(self,matrix):

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    print("Zero is in row {} col {}".format(row,col))
        return row, col

    def possible_movements(self,matrix, row_0, col_0):
        
        list_movements = []
        if (row_0+1) <= len(matrix):
            list_movements.append(((row_0+1),col_0))

        if (row_0-1) >= 0:
            list_movements.append(((row_0-1),col_0))

        if (col_0-1) >= 0:
            list_movements.append((row_0,(col_0-1)))
            
        if (col_0+1) <= len(matrix[0]):
            list_movements.append((row_0,(col_0+1)))
        
        movement = random.choice(list_movements)
        row = movement[0]
        col = movement[1]
       
        matrix[row_0][col_0], matrix[row][col] = matrix[row][col],  matrix[row_0][col_0]
        print(matrix)

        return matrix
    


    def find_solution(self,objective_matrix, mixed_matrix):
        a = 0
        new_row, new_column = Random_search().find_zero(mixed_matrix)
        while mixed_matrix != objective_matrix:
            Random_search().possible_movements(mixed_matrix, new_row, new_column)
            a += 1
            if mixed_matrix == objective_matrix:
                print(f"Objective matrix founded in {a} movements")
                break
        
