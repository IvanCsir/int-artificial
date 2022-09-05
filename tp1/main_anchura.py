from matriz import *
from busqueda_anchura import *

def main():
    n = int(input("How many rows matrix do you want?: "))
    m = int(input("How many columns matrix do you want?: "))
    amount_mix = int(input("How many times doy you want to mix the elements?: "))

    objective_matrix = [[1,2,3],[4,5,6],[7,8,0]]
    matrix = Matriz().crear_matriz(n,m)
    mixed_matrix = Matriz().mix_matrix(amount_mix, matrix) 
    
    
if __name__ == '__main__':
    main()