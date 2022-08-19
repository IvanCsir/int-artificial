class Random_search():
    
    def random_search(self,n,m,mixed_matrix):

        for row in range(n):
            for col in range(m):
                if mixed_matrix[row][col] == 0:
                    print("Zero is in row {} col {}".format(row+1,col+1))

    
        return mixed_matrix