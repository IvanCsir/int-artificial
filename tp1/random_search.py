class Random_search():
    
    def random_search(self,n,m,mixed_matrix):

        zero_position = ""
        for row in range(n):
            for col in range(m):
                if mixed_matrix[row][col] == 0:
                    zero_position = str(row)+ str(col)
                    print("Zero is in row {} col {}".format(row,col))
                    print(zero_position)

        return zero_position

    def possible_movements(self,mixed_matrix, zero_position):
        pass
        

