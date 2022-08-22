import random
from turtle import pos
from matriz import *
import time

class Random_search():
    
    def random_search(self,n,m,mixed_matrix):

        for row in range(n):
            for col in range(m):
                if mixed_matrix[row][col] == 0:
                    zero_position = str(row)+ str(col)
                    print("Zero is in row {} col {}".format(row,col))
        return row, col

    def possible_movements(self,mixed_matrix):
        '''ROW 0'''
        # Position 00
        if mixed_matrix[0][0] == 0:
            possible_movements = [0,1]
            mov = random.choice(possible_movements)
            if mov == 0:
                mixed_matrix[0][0], mixed_matrix[0][1] = mixed_matrix[0][1],  mixed_matrix[0][0]
            else:
                mixed_matrix[0][0], mixed_matrix[1][0] = mixed_matrix[1][0], mixed_matrix[0][0]

        # Position 01 
        if mixed_matrix[0][1] == 0:
            possible_movements = [0,1,2]
            mov = random.choice(possible_movements)
            if mov == 0:
                mixed_matrix[0][1],mixed_matrix[0][0] = mixed_matrix[0][0], mixed_matrix[0][1]
            elif mov == 1:
                 mixed_matrix[0][1], mixed_matrix[1][1] = mixed_matrix[1][1],mixed_matrix[0][1]
            else:
                 mixed_matrix[0][1], mixed_matrix[0][2] = mixed_matrix[0][2],  mixed_matrix[0][1]
        
        # Position 01 

        if mixed_matrix[0][2] == 0:
            possible_movements = [0,1]
            mov = random.choice(possible_movements)
            if mov == 0:
                mixed_matrix[0][2], mixed_matrix[0][1] = mixed_matrix[0][1],  mixed_matrix[0][2]
            else:
                mixed_matrix[0][2], mixed_matrix[1][2] = mixed_matrix[1][2],mixed_matrix[0][2]

        '''ROW 1'''
        # Position 10 
        if mixed_matrix[1][0] == 0:
            possible_movements = [0,1,2]
            mov = random.choice(possible_movements)
            if mov == 0:
                mixed_matrix[1][0],mixed_matrix[0][0] = mixed_matrix[0][0], mixed_matrix[1][0]
            elif mov == 1:
                mixed_matrix[1][0], mixed_matrix[1][1] = mixed_matrix[1][1],  mixed_matrix[1][0]
            else: 
                mixed_matrix[1][0],mixed_matrix[2][0] = mixed_matrix[2][0],  mixed_matrix[1][0]

        # Position 11
        if mixed_matrix[1][1] == 0:
            possible_movements = [0,1,2,3]
            mov = random.choice(possible_movements)
            if mov == 0:
                mixed_matrix[1][1], mixed_matrix[0][1] = mixed_matrix[0][1],mixed_matrix[1][1]
            elif mov == 1:
                mixed_matrix[1][1], mixed_matrix[1][2] = mixed_matrix[1][2], mixed_matrix[1][1]
            elif mov == 2:
                mixed_matrix[1][1], mixed_matrix[2][1] = mixed_matrix[2][1],  mixed_matrix[1][1]
            else:
                mixed_matrix[1][1], mixed_matrix[1][0] = mixed_matrix[1][0],  mixed_matrix[1][1]

        # Position 12
        if mixed_matrix[1][2] == 0:
            possible_movements = [0,1,2]
            mov = random.choice(possible_movements)
            if mov == 0:
                mixed_matrix[1][2], mixed_matrix[0][2] = mixed_matrix[0][2],  mixed_matrix[1][2]
            elif mov == 1:
                mixed_matrix[1][2], mixed_matrix[2][2] = mixed_matrix[2][2],  mixed_matrix[1][2]
            else: 
                mixed_matrix[1][2], mixed_matrix[1][1] = mixed_matrix[1][1], mixed_matrix[1][2]
        
        '''ROW 2'''
        # Position 20
        if mixed_matrix[2][0] == 0:
            possible_movements = [0,1]
            mov = random.choice(possible_movements)
            if mov == 0:
                mixed_matrix[2][0], mixed_matrix[1][0] = mixed_matrix[1][0], mixed_matrix[2][0]
            else:
                mixed_matrix[2][0], mixed_matrix[2][1] = mixed_matrix[2][1], mixed_matrix[2][0]
            
        # Position 21
        if mixed_matrix[2][1] == 0:
            print("++++++++++++++++++++++++++++++++")
            possible_movements = [1]
            mov = random.choice(possible_movements)
            print(mov)
            # if mov == 0:
            #     mixed_matrix[2][1], mixed_matrix[1][1] = mixed_matrix[1][1], mixed_matrix[2][1]
            # elif mov == 1:
            #     mixed_matrix[2][1], mixed_matrix[2][2] = mixed_matrix[2][2],  mixed_matrix[2][1]
            if mov == 1:
                mixed_matrix[2][1] = mixed_matrix[2][2]
                mixed_matrix[2][2] =  0
            # else:
            #     mixed_matrix[2][1], mixed_matrix[2][0] = mixed_matrix[2][0],  mixed_matrix[2][1]
        
        # Position 22
        if mixed_matrix[2][2] == 0:
            possible_movements = [0,1]
            mov = random.choice(possible_movements)
            if mov == 0:
                mixed_matrix[2][2], mixed_matrix[1][2] = mixed_matrix[1][2],  mixed_matrix[2][2]
            else:
                mixed_matrix[2][2], mixed_matrix[2][1] = mixed_matrix[2][1],  mixed_matrix[2][2]

        return mixed_matrix

    def compare_matrix(self, mixed_matrix, objective_matrix):
        a = 0
        mixed_matrix = Random_search().possible_movements(mixed_matrix)
        print(mixed_matrix)
        # while mixed_matrix != objective_matrix:
        #     mixed_matrix = Random_search().possible_movements(mixed_matrix)
        #     print(mixed_matrix)
        #     a += 1
        #     if mixed_matrix == objective_matrix:
        #         print(f"Objective matrix founded in {a} movements")
        #         break
        
