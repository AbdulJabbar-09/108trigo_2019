#!/usr/bin/python3

import sys
import math

from others import *

def nb_err():
    i = len(sys.argv) - 2
    nb = math.trunc(math.sqrt(i))
    if math.trunc(math.sqrt(i)) ** 2 != i: sys.exit(84)
    return nb

def display_mat(tab):
    for i in range(len(tab)):
        j = 0
        while j < len(tab[i]):
            print("%.2f%c" % (tab[i][j], '\t' if (j != len(tab[i]) - 1)\
                              else '\n'), end="")
            j += 1

def get_trigfunc(tab):
    ave = ["COS", "SIN", "COSH", "SINH", "EXP"]
    fct_tab = [my_cos, my_sin, my_cosh, my_sinh, my_exp]
    i = 0
    while i < len(fct_tab):
        if sys.argv[1] == ave[i]: tab = fct_tab[i](tab)
        i += 1
    return tab

def main():
    tab = []
    check_args()
    nb = nb_err()
    for i in range(int(nb)):
        tab.append([])
        for j in range(int(nb)):
            tab[i].append(sys.argv[i * int(nb) + j + 2])
    tab = get_trigfunc(tab)
    display_mat(tab)

if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception:
        sys.exit(84)
