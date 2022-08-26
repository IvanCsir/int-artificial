from random import Random
import numpy as np1
from matriz import *
from random_search import *
import time

def main():
    start = time.process_time()
    n = 3
    m = 3
    amount_mix = int(input("How many times doy you want to mix the elements?: "))
    objective_matrix = Matriz().crear_matriz(n,m)
    row_0, col_0 = Random_search().find_zero(objective_matrix)
    mixed_matrix = Matriz().mix_matrix(row_0,col_0, amount_mix, objective_matrix)
    
    Random_search().find_solution(objective_matrix, mixed_matrix)

    end = time.process_time()
    print(f"\nThis programme took {end-start} seconds ")



if __name__ == '__main__':
    main()