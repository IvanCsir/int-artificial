from matriz import *
from busqueda_anchura import *

def main():
    n = int(input("How many rows matrix do you want?: "))
    m = int(input("How many columns matrix do you want?: "))
    amount_mix = int(input("How many times doy you want to mix the elements?: "))
    matrix = Matriz().crear_matriz(n,m)
    mixed_matrix = Matriz().mix_matrix(matrix) 
    Busqueda_anchura().busqueda_anchura(mixed_matrix)