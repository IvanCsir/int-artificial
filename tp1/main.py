import numpy as np1
from matriz import *
from random_search import *

def main():
    n = int(input("How many rows will the matrix have?: "))
    m = int(input("How many columns will the matrix have?: "))
    amount_mix = int(input("How many times doy you want to mix the elements?:" ))

    objective_matrix = Matriz().crear_matriz(n,m)
    mixed_matrix = Matriz().mix_matrix(n,m,amount_mix)
    Random_search().random_search(n,m,mixed_matrix)



if __name__ == '__main__':
    main()