from random import Random
from matriz import *
from random_search import *
from busqueda_anchura import *
import time

def main():
    n = int(input("How many rows matrix do you want?: "))
    m = int(input("How many columns matrix do you want?: "))
    amount_mix = int(input("How many times doy you want to mix the elements?: "))
    start = time.process_time()
    matrix = Matriz().crear_matriz(n,m)
    mixed_matrix = Matriz().mix_matrix(amount_mix, matrix)
    objective_matrix = Matriz().crear_matriz(n,m)


    Random_search().find_solution(objective_matrix, mixed_matrix)

    end = time.process_time()
    print(f"\nThis programme took {end-start} seconds ")




if __name__ == '__main__':
    main()