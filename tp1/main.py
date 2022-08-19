import numpy as np1
from matriz import *

def main():
    n = int(input("How many rows will the matrix have?: "))
    m = int(input("How many columns will the matrix have?: "))
    amount_mix = int(input("How many times doy you want to mix the elements?:" ))

    Matriz.crear_matriz(n,m,amount_mix)


if __name__ == '__main__':
    main()