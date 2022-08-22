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
    mixed_matrix = Matriz().mix_matrix(n,m,amount_mix)
    zero_position = Random_search().random_search(n,m,mixed_matrix)
    Random_search().compare_matrix(mixed_matrix, objective_matrix)
    end = time.process_time()
    print(f"\nThis programme took {end-start} seconds ")



if __name__ == '__main__':
    main()