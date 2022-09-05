from tree import TreeNode
import copy


class Busqueda_anchura():
    
    objective_matrix = [[1,2,3],[4,5,6],[7,8,0]]
    
    def find_zero(self,matrix):
        
        row1 = 0
        col1 = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    row1 = row
                    col1 = col
                    return row1, col1

    def possible_movements(self,matrix):
        
        row_0, col_0 = self.find_zero(matrix)

        list_movements = []
        if (row_0+1) < len(matrix):
            list_movements.append([row_0+1,col_0])

        if (row_0-1) >= 0:
            list_movements.append([row_0-1,col_0])

        if (col_0-1) >= 0:
            list_movements.append([row_0,col_0-1])
            
        if (col_0+1) < len(matrix[0]):
            list_movements.append([row_0,col_0+1])
       
        return list_movements

    def do_movement(self, matrix, new_row, new_col):
        row_0, col_0 = self.find_zero(matrix)
        matrix[row_0][col_0], matrix[new_row][new_col] = matrix[new_row][new_col],  matrix[row_0][col_0]
        return matrix


    def busqueda_anchura(self,matrix):
        pass