import numpy as np1
from matriz import *
from random_search import *

def main():
    n = 3
    m = 3
    amount_mix = int(input("How many times doy you want to mix the elements?: "))

    objective_matrix = Matriz().crear_matriz(n,m)
    mixed_matrix = Matriz().mix_matrix(n,m,amount_mix)
    zero_position = Random_search().random_search(n,m,mixed_matrix)
    Random_search().possible_movements(mixed_matrix, zero_position)



if __name__ == '__main__':
    main()